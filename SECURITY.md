# 安全策略

## 本项目包含什么

Maoxuan Product Agent 主要发布可审计的 Markdown Skill，同时包含少量本地工具：

- `product-decision-agent/`：Agent 指令、参考资料、回答样例和质量门禁脚本。
- `scripts/install.sh`：把 Skill 文件复制到用户或项目目录，不访问网络，不执行下载内容。
- `scripts/validate.sh` 与 Python 校验器：在本地或 GitHub Actions 中检查输出和发布资产。
- `docs/`：GitHub Pages 静态页面，不接收账号、表单或用户数据。

安装 Skill 本身不会自动执行远程代码。真正的文件读取、命令或网络访问仍由所使用的 Agent 及其权限模型控制。使用前请像审查代码一样审查 Skill 和脚本，并从本仓库或已标明来源的目录安装。

## 支持版本

| 版本 | 安全修复支持 |
|---|---|
| 最新 `1.x` 版本 | 支持 |
| 更早版本 | 仅尽力支持，建议先升级 |

## 私密报告漏洞

请不要在公开 Issue 中披露可利用细节、密钥、个人信息或内部数据。

优先使用 GitHub Private Vulnerability Reporting：

<https://github.com/atdy/maoxuan-product-agent/security/advisories/new>

报告请尽量包含：

1. 受影响的文件、版本或 Commit。
2. 最小复现步骤和所需环境。
3. 可能造成的影响与攻击前提。
4. 已知缓解方式或修复建议。

维护者会尽量在 5 个工作日内确认报告，并在修复或缓解措施可用后协调披露时间。

## 安全范围

包括：

- Skill 或参考文件中的提示注入、危险默认行为或误导性权限要求。
- 安装脚本、质量门禁、发布校验器和 GitHub Actions 的漏洞。
- 发布包、来源链接、版本信息或文档导致的供应链风险。
- GitHub Pages 中可由本项目修复的安全问题。

通常不包括：

- Codex、Claude Code、Cursor 或其他第三方 Agent 本身的漏洞。
- 用户主动授予 Agent 的高风险权限或未脱敏输入。
- 不由本项目维护的镜像、目录、模型服务和第三方网站。
- 单纯的产品建议分歧，且不涉及可利用的安全影响。
