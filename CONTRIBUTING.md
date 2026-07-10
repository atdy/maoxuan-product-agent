# 参与贡献

这个项目维护的是一个产品决策 Agent，不是原文知识库。提交修改时，优先证明它能让真实产品问题得到更准确、更短、更可执行的回答。

## 修改原则

- 默认输出继续使用现代中文产品语言，不暴露原文、人物、历史语境或政治化表达。
- 新框架必须改变判断或行动，不能只增加术语。
- 新场景优先补到 `product-decision-agent/references/product-playbooks.md`，不要把 `SKILL.md` 写成大而全的手册。
- 详细方法依据放在 `methodology-basis.md`，运行时规则放在 `reasoning-engine.md`，两处不要重复大段内容。
- 修改触发描述时，同时检查 Codex、Claude Code 和 Cursor 的自动调用是否仍然准确。

## 提交前验证

运行：

```bash
./scripts/validate.sh
```

如果本机安装了 Codex 的 `skill-creator`，再运行：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py product-decision-agent
```

内容修改至少补一个真实案例，并检查：

1. 是否一句话指出了真正问题。
2. 是否明确了当前阶段和主导结果的机制。
3. 是否给出 1-3 个下一步动作及决策信号。
4. 是否说明现在不要做什么。
5. 是否避免空话、理论说明和来源暴露。

## Pull Request

PR 请说明：

- 解决了什么真实使用问题。
- 修改前可能产生什么错误判断。
- 用哪些案例验证了修改后的行为。
- 是否改变触发范围、输出格式或兼容性。
