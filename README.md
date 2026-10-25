# 何家语 · 个人作品集

原生 HTML / CSS / JavaScript 作品集，包含全部作品图片、展览照片、黑白背景、动效及简历 PDF，无安装依赖或构建依赖。

正式网址（启用 Pages 并部署成功后可访问）：**https://hef81891-coder.github.io/Portfolio/**

## 你现在只需要点击

1. 打开 [Settings → Pages](https://github.com/hef81891-coder/Portfolio/settings/pages)。
2. 在 **Build and deployment → Source** 选择 **GitHub Actions**。
3. 打开 [Actions](https://github.com/hef81891-coder/Portfolio/actions)，选择 **Deploy portfolio to GitHub Pages**。若当前部署失败，点 **Re-run all jobs**；也可以选择 **Run workflow → main → Run workflow**。
4. 等待 build 和 deploy 均变绿，再打开上面的正式网址。

以后每次提交或合并到 main，网站都会自动更新，不需要再次上传文件或更改 Pages 设置。

## 完整 ZIP 里有什么

[下载完整网站部署包](downloads/Portfolio-deploy.zip)（在 GitHub 文件页面点击 Download raw file）。

解压后的最外层就是网站根目录，包含：

- `index.html`：已经完成的视觉设计、文字、CSS 和 JavaScript 动效。
- `assets/`：所有作品图、展览原图、黑白背景使用的原素材，以及简历 `resume-he-jiayu.pdf`。
- `.nojekyll`：告诉 GitHub Pages 按静态文件发布。
- `.github/workflows/deploy.yml`：main 自动部署和手动部署的官方 Actions 配置。
- `scripts/build_pages.py`：自动检查资源、生成干净发布目录，不需要你执行。
- `.gitignore`、`README.md`：忽略生成文件及使用说明。

**不要只拿出 index.html 而丢掉 assets 文件夹。** 下载 ZIP 后解压，直接双击 index.html 可以查看；若部署到其他静态托管服务，将 index.html 和 assets 放在该服务的发布根目录即可。GitHub 自动部署已经为你配置，无需在电脑安装软件。

## 发布范围与维护

工作流只发布 index.html、assets、.nojekyll，不发布 ZIP、说明文档、脚本、历史备份或需求文件。资源使用相对路径，支持 /Portfolio/ 子路径，四个页面采用 hash 导航，不需要服务器重写规则。字体为系统字体，无外部字体、视频或动画服务依赖。

编辑网站时，在本仓库修改 index.html 或替换 assets 中对应文件，提交到 main。当前版本已按要求移除文字编辑与导出功能。后台暂停动画，系统减少动态效果偏好静默生效，不显示设置状态按钮。

工作流使用官方 checkout、configure-pages、upload-pages-artifact、deploy-pages Actions；部署任务仅使用 GitHub 提供的 pages:write、id-token:write 权限。无需保存 API Key 或个人访问令牌。

## 验证范围

生产目录已检查本地资源和锚点，并按 /Portfolio/ 子路径检查桌面、手机、页面导航、图片、简历、放大预览和减少动态效果。公众号链接地址保留，但不能保证第三方平台的可用性。网站实际是否上线以 GitHub Actions 部署成功及公网检查结果为准。
