# Maoxuan Product Agent

### A Chinese product decision agent distilled from *On Contradiction* and *On Practice*

[中文](README.md) · [Website](https://atdy.github.io/maoxuan-product-agent/) · [Case Library](https://atdy.github.io/maoxuan-product-agent/cases/) · [skills.sh](https://www.skills.sh/atdy/maoxuan-product-agent/product-decision-agent) · [Agent Skills](https://agent-skills.md/skills/atdy/maoxuan-product-agent/product-decision-agent) · [Skillstore](https://skillstore.io/skills/atdy-product-decision-agent) · [Install](#install) · [Evaluation](evaluation/self_test_report.md)

[![GitHub stars](https://img.shields.io/github/stars/atdy/maoxuan-product-agent?style=flat&color=c2332d)](https://github.com/atdy/maoxuan-product-agent/stargazers)
[![Validate skill](https://github.com/atdy/maoxuan-product-agent/actions/workflows/validate.yml/badge.svg)](https://github.com/atdy/maoxuan-product-agent/actions/workflows/validate.yml)
[![skills.sh](https://img.shields.io/badge/skills.sh-product--decision--agent-111827.svg)](https://www.skills.sh/atdy/maoxuan-product-agent/product-decision-agent)
[![Skillstore quality](https://img.shields.io/badge/Skillstore_quality-83%2F100-d4a72c.svg)](https://skillstore.io/skills/atdy-product-decision-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-2f6f4e.svg)](LICENSE)

![Maoxuan Product Agent social preview](docs/assets/social-preview.png)

> Complex product problems are often not short of solutions. They are short of a clear judgment about which problem matters now.

Maoxuan Product Agent is an open-source Agent Skill for product managers, operators, growth teams, founders, and business owners working in Chinese internet contexts.

Its reasoning engine was designed after a complete reading of *On Practice*, *On Contradiction*, and related essays in Volume I of the selected works. It distills the underlying decision method rather than quotations: start from observable facts, identify the current bottleneck and the mechanism driving it, focus scarce resources, take the smallest useful action, and update the judgment from real results.

The theory stays in the background. Default answers:

- use modern product and business language;
- do not quote source texts or discuss history;
- do not perform political role-play;
- identify the real constraint before recommending tactics;
- end with a concrete next step, a decision signal, and a stop list.

The agent answers primarily in Simplified Chinese because it is built for day-to-day work in mainland China. English product terms such as DAU, GMV, CAC, LTV, ROI, MVP, A/B Test, OKR, KPI, and Roadmap are retained where useful.

## What It Solves

The skill covers 36 recurring product-work scenarios:

- product strategy, Roadmap, version planning, and prioritization;
- growth, acquisition, activation, retention, conversion, and monetization;
- content, community, creator, user, and campaign operations;
- metric anomalies, data definitions, tracking, and A/B Test decisions;
- customer feedback, competitor pressure, and enterprise requests;
- resource conflicts, executive interruptions, delays, and scope churn;
- cross-functional collaboration, OKR/KPI design, and retrospectives.

Typical output:

1. **Problem judgment**: the real issue in one sentence.
2. **Why it matters**: the mechanism and evidence behind that judgment.
3. **Next actions**: one to three actions with an owner, time window, metric, or decision rule.
4. **Risk warning**: what not to do yet.
5. **Need to confirm**: no more than three facts, only when they can change the decision.

## Searchable Case Library

The website includes [12 standalone Chinese product-decision cases](https://atdy.github.io/maoxuan-product-agent/cases/), including [requirements prioritization](https://atdy.github.io/maoxuan-product-agent/cases/requirement-prioritization.html), [growth stagnation](https://atdy.github.io/maoxuan-product-agent/cases/growth-stagnation.html), [retention decline after a release](https://atdy.github.io/maoxuan-product-agent/cases/retention-drop-after-release.html), [community cold start](https://atdy.github.io/maoxuan-product-agent/cases/community-cold-start.html), [content supply](https://atdy.github.io/maoxuan-product-agent/cases/content-supply-shortage.html), [campaign performance](https://atdy.github.io/maoxuan-product-agent/cases/campaign-low-participation.html), [data-definition conflicts](https://atdy.github.io/maoxuan-product-agent/cases/data-definition-conflict.html), and [conflicting user feedback](https://atdy.github.io/maoxuan-product-agent/cases/conflicting-user-feedback.html). Each page provides a judgment, action order, stop list, and decision conditions.

## Install

### Universal Agent Skills installer

Install globally for Codex, Claude Code, and Cursor:

```bash
npx skills add atdy/maoxuan-product-agent --skill product-decision-agent --agent codex claude-code cursor -g -y
```

List the available skill without installing it:

```bash
npx skills add atdy/maoxuan-product-agent --list
```

### Repository installer

```bash
git clone https://github.com/atdy/maoxuan-product-agent.git
cd maoxuan-product-agent

./scripts/install.sh codex
./scripts/install.sh claude
./scripts/install.sh cursor
```

Install into one project instead of the current user account:

```bash
./scripts/install.sh claude /path/to/project
```

The canonical skill package is [`product-decision-agent/`](product-decision-agent/).

Independent listings are available on [skills.sh](https://www.skills.sh/atdy/maoxuan-product-agent/product-decision-agent), [Agent Skills](https://agent-skills.md/skills/atdy/maoxuan-product-agent/product-decision-agent), [Skillstore](https://skillstore.io/skills/atdy-product-decision-agent) with a safe security audit and 83/100 quality score, and the 42k-star [Agentic Awesome Skills](https://github.com/sickn33/agentic-awesome-skills/tree/main/skills/product-decision-agent). Each listing links back to this repository for provenance and security review.

## Use

Codex:

```text
Use $product-decision-agent to decide whether we should ship an A/B Test whose CTR rose 12% but orders did not.
```

Claude Code or Cursor:

```text
/product-decision-agent We have 20 requests competing for two engineers. What should the next version include?
```

You do not need to mention the source methodology. A real product, growth, data, operations, or collaboration problem is the trigger.

## Why It Is Different

| Generic product prompt | Maoxuan Product Agent |
|---|---|
| Lists every plausible tactic | Identifies the current bottleneck |
| Applies a universal framework | Checks stage, segment, evidence, and constraints |
| Treats metrics or feedback as conclusions | Separates facts, hypotheses, and isolated cases |
| Recommends a large complete solution | Uses a minimum diagnostic or reversible test when evidence is weak |
| Says only what to do | Also states what to stop and when to change course |

## Evidence and Quality

- 36/36 documented product cases pass the project quality gate.
- Four clean-session forward tests were run with Claude Code.
- The skill package includes a reasoning engine, 36 playbooks, response examples, and automated checks.
- The source-reading audit records the exact anthology and reference-project revisions used in the latest review.

Run all checks:

```bash
./scripts/validate.sh
```

See [self_test_report.md](evaluation/self_test_report.md), [forward_test_report.md](evaluation/forward_test_report.md), and [source_reading_audit.md](evaluation/source_reading_audit.md).

## Contributing

- Report installation, triggering, judgment, or output problems with the [Chinese-first bug form](https://github.com/atdy/maoxuan-product-agent/issues/new?template=bug_report.yml).
- Submit a sanitized real-world scenario through the [product case form](https://github.com/atdy/maoxuan-product-agent/issues/new?template=product_case.yml).
- Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [community code of conduct](CODE_OF_CONDUCT.md) before opening a pull request.
- Report prompt injection, unsafe defaults, or supply-chain concerns privately under the [security policy](SECURITY.md).

Do not publish company secrets, user data, credentials, or restricted internal metrics.

## Scope

This repository is not a political knowledge base, quotation generator, history tool, or philosophy tutor. It does not contain the full anthology and does not retrieve source passages. The source methodology is exposed only in maintenance documentation for auditability.

## Acknowledgements

The research and comparison phase benefited from these open-source projects and their contributors:

- [leezythu/maoxuan-skill](https://github.com/leezythu/maoxuan-skill)
- [zhangtianruiwork-droid/Maoxuan-Changzheng](https://github.com/zhangtianruiwork-droid/Maoxuan-Changzheng)
- [weiyinfu/MaoZeDongAnthology](https://github.com/weiyinfu/MaoZeDongAnthology)

This project does not copy their skill prompts or application code. It redesigns the reasoning workflow for modern product work.

## License

[MIT License](LICENSE)
