# Product Decision Agent

> 把《矛盾论》《实践论》蒸馏成一个中文产品决策 Agent。  
> 不输出原文，不讲历史，不做政治表达，只帮你解决真实产品问题。

这是一个面向中文互联网产品工作的 Agent Skill。

它的底层推理来源，是对《矛盾论》《实践论》的完整阅读、提炼和产品化转译；同时吸收了《毛泽东选集》第一卷中关于调查研究、阶段判断、资源集中、相关方分析、组织协作和行动验证的相关方法。

但它不是《毛选》知识库，也不是语录生成器。

用户不需要学习《毛选》，也不会在默认回答里看到原文引用。你只需要提出真实产品问题，它会像一位经验丰富的产品负责人一样，帮你判断真正卡点，并给出下一步最值得执行的方案。

## 一句话说明

**这是一个把《矛盾论》《实践论》的思维方式隐藏在后台，用现代产品语言输出决策建议的 Product Decision Agent。**

它会做的不是：

- 解释《毛选》。
- 复述原文。
- 输出政治化话术。
- 给你一堆抽象框架。

它会做的是：

- 找出当前阶段真正的核心阻塞。
- 判断问题属于需求、增长、留存、转化、数据、资源、协作还是交付问题。
- 区分事实、假设和解决方案诉求。
- 判断证据够不够，够就行动，不够就做最小验证。
- 告诉你现在最该做什么，以及哪些事暂时不要做。

## 为什么是《矛盾论》和《实践论》

产品工作里最难的，往往不是“缺方法论”，而是：

- 表面问题太多，不知道哪个才是主问题。
- 需求、资源、数据、老板、竞品、用户反馈互相打架。
- 团队在会议里讨论很久，却没有回到真实用户和真实结果。
- 方案看起来都对，但当前阶段只能做一件最关键的事。

《矛盾论》给这个 Agent 的核心能力是：

- 不平均看待所有问题，先找当前阶段的主要问题。
- 不套万能公式，具体问题具体分析。
- 不只看外部原因，而是追到产品、用户、组织内部的真实机制。
- 看阶段变化，知道什么时候该换打法。

《实践论》给这个 Agent 的核心能力是：

- 判断必须来自事实、一线材料和真实行为。
- 先区分现象、假设和结论。
- 方案必须回到 MVP、灰度、A/B Test、用户验证、数据验证中检验。
- 认识要随着实践结果不断修正。

所以，这个 Skill 的价值不是告诉你“《毛选》说了什么”，而是让你面对复杂产品问题时，获得一种更强的问题定位、取舍和行动能力。

## 它怎么回答问题

默认输出结构：

1. **问题判断**：一句话指出真正问题。
2. **原因分析**：说明为什么这是关键。
3. **行动建议**：给出 1-3 个下一步动作，尽量包含时间窗口、负责人/相关方、指标或后续决策口径。
4. **风险提醒**：指出现在不要做什么。
5. **需要确认**：仅在会改变判断时提出，最多 3 个问题。

示例：

```text
用户：
我们社区 DAU 连续两周下降 15%，运营觉得要加活动拉回来。

Agent：
问题判断
先不要用活动拉 DAU，当前最关键的是确认下滑来自哪类用户和哪个环节。

原因分析
- 连续两周下降 15% 已经不像普通波动。
- 社区 DAU 可能受新用户、老用户、内容供给、分发规则、Push、版本问题影响。
- 没拆来源就做活动，只会制造短期噪音，掩盖真正原因。

行动建议
1. 24 小时内按新老用户、渠道、平台、版本、核心内容供给拆下降贡献。
2. 找贡献最大的 1-2 个群体，看行为路径和最近反馈。
3. 如果是老用户下降，先做召回和内容修复；如果是渠道下降，再做拉新活动，并用 72 小时 DAU 恢复率和 D7 留存判断是否继续。

风险提醒
不要先上全站活动，也不要看总 DAU 做判断。
```

注意：默认回答里不会说“《矛盾论》认为……”或“《实践论》指出……”。方法在后台，输出是产品语言。

## 适用场景

这个 Agent 适合处理中国大陆互联网日常工作中的真实问题，包括：

- 产品规划、需求分析、PRD、需求优先级、排期、版本规划、Roadmap。
- MVP、灰度、上线、迭代、用户研究、产品探索。
- 增长停滞、拉新、投放、渠道、裂变、CAC、LTV、ROI。
- DAU/MAU、GMV、漏斗、激活、留存、转化、会员、定价。
- 社区运营、内容供给、创作者、用户运营、活动运营、私域。
- 指标异常、数据口径、埋点、A/B Test、用户反馈、客服/销售反馈。
- 竞品冲击、资源不足、项目延期、需求反复、老板临时插需求。
- 跨部门协作、团队冲突、OKR/KPI、目标拆解、复盘。

## 方法转译

这个项目不是把原文摘出来，而是把方法转成现代产品工作中的判断动作：

| 方法来源中的概念 | 产品工作中的表达 |
|---|---|
| 实践 | MVP、灰度、A/B Test、用户验证、数据验证、一线调研 |
| 认识 | 认知升级、策略修正、信息校准、复盘结论 |
| 矛盾 | 问题、瓶颈、资源冲突、关键阻塞 |
| 主要矛盾 | 当前阶段最影响结果的主问题 |
| 矛盾特殊性 | 具体场景、具体阶段、具体人群、具体链路 |
| 转化条件 | 阶段变化、资源变化、用户结构变化、组织权责变化 |
| 群众/阶层分析 | 用户分层、相关方地图、受益人/成本承担者/否决人 |
| 根据地 | 核心场景、核心人群、核心链路、可防守阵地 |

## 项目结构

```text
.
├── README.md
├── LICENSE
├── skill-source/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   ├── references/
│   │   ├── methodology-basis.md
│   │   ├── reasoning-engine.md
│   │   ├── product-playbooks.md
│   │   └── response-examples.md
│   └── scripts/
│       └── quality_gate.py
└── evaluation/
    ├── design_summary.md
    ├── self_test_report.md
    ├── source_reading_audit.md
    ├── sample_output_case_*.md
    └── sample_output_bad_example.md
```

核心文件：

- `skill-source/SKILL.md`：Agent 入口，包含触发描述、角色、后台推理流程、输出结构和禁止事项。
- `skill-source/references/reasoning-engine.md`：复杂问题的后台推理引擎。
- `skill-source/references/product-playbooks.md`：36 个现代产品工作场景手册。
- `skill-source/references/response-examples.md`：中文输出样例。
- `skill-source/references/methodology-basis.md`：方法来源与产品化映射，供维护和审查使用。
- `skill-source/scripts/quality_gate.py`：样例输出质量门禁。

## 怎么使用

这个项目不只适用于 Codex。只要你的 Agent 支持读取本地上下文、项目规则、Skill、Rules 或自定义系统提示，都可以使用。

### 方式一：Codex

复制到 Codex Skills 目录：

```bash
git clone https://github.com/<your-name>/<repo-name>.git
cd <repo-name>

mkdir -p ~/.codex/skills/product-decision-agent
rsync -a skill-source/ ~/.codex/skills/product-decision-agent/
```

使用：

```text
使用 $product-decision-agent 帮我诊断这个产品问题：老板临时插了一个会员积分商城，但这个版本原本在做新手转化，我该怎么处理？
```

### 方式二：Claude Code

如果你的 Claude Code 环境支持 Skills，可以把 `skill-source/` 放到对应的 Skills 目录，并用 `product-decision-agent` 调用。

如果暂时没有 Skills 目录，也可以用项目规则方式接入。在你的项目根目录新建或修改 `CLAUDE.md`：

```md
当我提出产品、运营、增长、数据或组织协作问题时，请先阅读并遵循：

./skill-source/SKILL.md

如果问题复杂，再按需读取：

- ./skill-source/references/reasoning-engine.md
- ./skill-source/references/product-playbooks.md
- ./skill-source/references/response-examples.md

默认用中文回答。不要引用原文，不要解释理论来源，直接给问题判断、原因分析、行动建议、风险提醒和必要确认项。
```

然后把 `skill-source/` 放进你的项目，直接向 Claude Code 提问即可。

### 方式三：Cursor

Cursor 可以用 Rules 方式接入。把本项目放到你的工作区后，新建：

```text
.cursor/rules/product-decision-agent.mdc
```

内容示例：

```md
---
description: 中文产品决策 Agent，用于产品、运营、增长、数据和协作问题
alwaysApply: false
---

当用户提出产品、运营、增长、数据、项目推进或组织协作问题时，按照 `skill-source/SKILL.md` 的规则回答。

复杂问题按需参考：

- `skill-source/references/reasoning-engine.md`
- `skill-source/references/product-playbooks.md`
- `skill-source/references/response-examples.md`

默认中文输出。不要讲理论，不要引用原文，不要输出历史或政治化话术。重点给出真正问题、原因、行动、风险和必要确认项。
```

之后你可以在 Cursor 里直接问：

```text
用产品决策 Agent 帮我看一下：我们 A/B Test 点击率涨了，但订单没涨，要不要全量？
```

### 方式四：任意 Agent / 自定义 GPT / OpenAI Assistants

通用接入方式：

1. 把 `skill-source/SKILL.md` 作为主系统提示或主规则。
2. 把 `skill-source/references/*.md` 作为知识文件或可检索上下文。
3. 告诉 Agent：默认不要暴露方法来源，只输出现代产品语言。
4. 如果平台支持工具调用，可以把 `skill-source/scripts/quality_gate.py` 作为输出质量检查脚本。

最小系统提示可以这样写：

```text
你是中文产品决策 Agent。请遵循 skill-source/SKILL.md 的工作方式：
先判断真实问题、当前阶段、核心阻塞、关键约束和证据充分性，再给出最值得执行的下一步。
默认中文回答。不要引用原文，不要解释理论来源，不要讲历史或政治化表达。
```

## 本地验证

正常样例：

```bash
python3 skill-source/scripts/quality_gate.py evaluation/sample_output_case_*.md
```

预期：全部 `PASS`。

失败样例：

```bash
python3 skill-source/scripts/quality_gate.py evaluation/sample_output_bad_example.md
```

预期：该样例 `FAIL`，用于确认门禁能抓到来源暴露、空话和缺少行动信号。

如果你本地有 Codex 的 `skill-creator` 校验脚本，可以运行：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill-source
```

## 自测覆盖

当前自测覆盖 36 个核心中文产品案例，并额外包含“需要确认”边界样例和失败样例。

覆盖场景包括：

- 需求优先级、老板插需求、版本规划、Roadmap。
- 增长停滞、DAU 下滑、留存下降、转化问题、活动效果差。
- 社区冷启动、内容供给不足、竞品冲击、资源不足。
- 跨部门合作、数据冲突、A/B Test 异常、项目延期。
- 用户反馈冲突、OKR/KPI、复盘、AI 功能冲动、合规、出海等。

详见：

- `evaluation/self_test_report.md`
- `evaluation/sample_output_case_*.md`

## 致谢

这个项目在阅读和研究阶段参考、学习并受到以下开源项目启发。感谢这些项目的作者和维护者：

- [leezythu/maoxuan-skill](https://github.com/leezythu/maoxuan-skill)
- [zhangtianruiwork-droid/Maoxuan-Changzheng](https://github.com/zhangtianruiwork-droid/Maoxuan-Changzheng)
- [weiyinfu/MaoZeDongAnthology](https://github.com/weiyinfu/MaoZeDongAnthology)

本项目没有复制这些项目的 Skill prompt 或应用代码，而是重新面向现代互联网产品工作场景设计了隐藏理论来源的产品决策 Agent。上述项目对本项目的研究、对照和方法校准很有帮助。

## 许可证

本项目以 MIT License 开源。详见 [LICENSE](LICENSE)。

请注意：本项目不包含《毛泽东选集》全文，不提供原文检索能力，也不作为政治、历史或哲学知识库使用。
