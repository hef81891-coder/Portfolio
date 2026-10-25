#!/usr/bin/env python3
"""Validate local references and stage only public website files for Pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT
OUTPUT = ROOT / '_site'


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('src', 'href', 'poster'):
            if attrs.get(key):
                self.urls.append(attrs[key])
        if attrs.get('data-go'):
            self.urls.append('#' + attrs['data-go'])
        if attrs.get('srcset'):
            self.urls.extend(item.strip().split()[0] for item in attrs['srcset'].split(','))


def main():
    html = (SITE / 'index.html').read_text(encoding='utf-8')
    refs = References()
    refs.feed(html)
    # Quoted CSS data URLs can contain parentheses; consume quotes first.
    for match in re.finditer(r'''url\(\s*(?:'([^']*)'|"([^"]*)"|([^\s)]+))\s*\)''', html):
        refs.urls.append(next(value for value in match.groups() if value is not None))
    checked = set()
    for value in refs.urls:
        if value.startswith(('https://', 'mailto:', 'data:')):
            continue
        url = urlsplit(value)
        if url.scheme or value.startswith('/'):
            raise SystemExit(f'Nonportable resource URL: {value}')
        if not url.path:
            if url.fragment and unquote(url.fragment) not in refs.ids:
                raise SystemExit(f'Missing anchor: {value}')
            continue
        local = (SITE / unquote(url.path)).resolve()
        if not local.is_relative_to(SITE.resolve()) or not local.is_file():
            raise SystemExit(f'Missing or unsafe resource: {value}')
        checked.add(local.relative_to(SITE.resolve()).as_posix())
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    shutil.copy2(SITE / 'index.html', OUTPUT / 'index.html')
    shutil.copytree(SITE / 'assets', OUTPUT / 'assets')
    shutil.copy2(ROOT / '.nojekyll', OUTPUT / '.nojekyll')
    assert not (OUTPUT / 'reference').exists()
    assert not (OUTPUT / 'artifacts').exists()
    print(f'Validated {len(checked)} unique local resources and navigation anchors.')
    print('Staged _site/: index.html, assets/, .nojekyll (no backups or documentation).')


if __name__ == '__main__':
    main()
