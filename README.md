# Product Decision Agent

一个中文优先的产品决策 Skill，面向中国大陆互联网产品、运营、增长、数据和组织协作场景。

它不是《毛选》知识库，不是语录生成器，不是哲学解释器，也不是历史研究工具。它的目标是：把《实践论》《矛盾论》以及《毛泽东选集》第一卷中与调查、判断、阶段、资源、组织相关的方法，转译成一个日常可用的 Product Decision Agent。

用户不需要学习任何理论，只需要提出真实产品问题。Agent 会像一位经验丰富的产品负责人一样，快速判断真正卡点，并给出下一步最值得执行的方案。

## 这个项目解决什么

产品工作里最常见的困难不是“没有框架”，而是：

- 症状很多，但不知道真正卡住结果的是什么。
- 需求很多，但不知道当前阶段该保哪一个。
- 数据在波动，但不知道该先查口径还是先做业务动作。
- 老板、销售、运营、研发都很急，但没人把取舍讲清楚。
- 竞品、增长、留存、转化、资源、延期、协作混在一起，最后变成泛泛讨论。

这个 Skill 的默认工作方式是：

1. 先判断用户真正想改变的结果。
2. 区分事实、假设和解决方案诉求。
3. 找出当前阶段最影响结果的核心阻塞。
4. 判断产品/业务/项目/组织所处阶段。
5. 识别关键约束和相关方。
6. 判断证据是否足够。
7. 给出可执行动作、风险提醒和必要确认项。

## 设计原则

### 1. 永远解决问题

用户提出产品问题后，Agent 不解释理论，不讲历史，不做概念科普，而是直接帮用户定位问题、判断取舍、推进下一步。

### 2. 方法来源隐藏在后台

默认回答中不会出现“某篇文章认为”“某人物指出”“经典原文”等表达。用户看到的只应该是现代产品语言。

### 3. 不蒸馏文字，蒸馏思维方式

这个项目不是摘抄观点，而是把方法转成产品工作中的判断动作，例如：

| 方法来源中的抽象概念 | 产品工作中的表达 |
|---|---|
| 实践 | MVP、灰度、A/B Test、用户验证、数据验证、一线调研 |
| 认识 | 认知升级、策略修正、信息校准、复盘结论 |
| 矛盾 | 问题、瓶颈、资源冲突、关键阻塞 |
| 主要矛盾 | 当前阶段最影响结果的主问题 |
| 阶段 | 产品阶段、业务阶段、项目阶段、团队阶段 |
| 群众/阶层分析 | 用户分层、相关方地图、受益人/成本承担者/否决人 |

### 4. 中文产品工作语境优先

这个 Skill 默认服务中文工作场景，覆盖中国大陆互联网语境中的产品、运营、增长、商业化、项目推进和组织协作问题。

## 适用场景

包括但不限于：

- 产品规划、需求分析、PRD、需求优先级、排期、版本规划、Roadmap。
- MVP、灰度、上线、迭代、用户研究、产品探索。
- 增长停滞、拉新、投放、渠道、裂变、CAC、LTV、ROI。
- DAU/MAU、GMV、漏斗、激活、留存、转化、会员、定价。
- 社区运营、内容供给、创作者、用户运营、活动运营、私域。
- 指标异常、数据口径、埋点、A/B Test、用户反馈、客服/销售反馈。
- 竞品冲击、资源不足、项目延期、需求反复、老板临时插需求。
- 跨部门协作、团队冲突、OKR/KPI、目标拆解、复盘。

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

核心文件说明：

- `skill-source/SKILL.md`：Skill 入口，包含触发描述、角色、后台推理流程、输出结构和禁止事项。
- `skill-source/references/reasoning-engine.md`：复杂问题的后台推理引擎。
- `skill-source/references/product-playbooks.md`：36 个现代产品工作场景手册。
- `skill-source/references/response-examples.md`：中文输出样例。
- `skill-source/references/methodology-basis.md`：方法来源与产品化映射，主要供维护和审查使用。
- `skill-source/scripts/quality_gate.py`：样例输出质量门禁。
- `evaluation/`：自测报告、边界样例和失败样例。

## 安装使用

### 方式一：复制到 Codex Skills 目录

```bash
git clone https://github.com/<your-name>/<repo-name>.git
cd <repo-name>

mkdir -p ~/.codex/skills/product-decision-agent
rsync -a skill-source/ ~/.codex/skills/product-decision-agent/
```

然后在 Codex 里直接使用：

```text
使用 $product-decision-agent 帮我诊断这个产品问题：我们社区 DAU 连续两周下降，运营想上活动拉回来，应该怎么判断？
```

也可以直接提出自然语言问题，符合触发场景时会自动调用：

```text
老板临时插了一个会员积分商城，但这个版本原本在做新手转化，我该怎么处理？
```

### 方式二：在本地验证 Skill

```bash
python3 skill-source/scripts/quality_gate.py evaluation/sample_output_case_*.md
```

预期：正常样例全部 `PASS`。

验证失败样例：

```bash
python3 skill-source/scripts/quality_gate.py evaluation/sample_output_bad_example.md
```

预期：该样例 `FAIL`，用于确认门禁能抓到来源暴露、空话和缺少行动信号的问题。

### 验证 Skill 结构

如果你本地有 Codex 的 `skill-creator` 校验脚本，可以运行：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill-source
```

## 输出形式

默认输出结构：

1. **问题判断**：一句话指出真正问题。
2. **原因分析**：说明为什么这是关键。
3. **行动建议**：给出 1-3 个下一步动作，尽量包含时间窗口、负责人/相关方、指标或后续决策口径。
4. **风险提醒**：指出现在不要做什么。
5. **需要确认**：仅在会改变判断时提出，最多 3 个问题。

## 示例

用户：

```text
我们社区 DAU 连续两周下降 15%，运营觉得要加活动拉回来。
```

Agent：

```text
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

## 自测覆盖

当前自测覆盖 36 个核心中文产品案例，包含：

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
