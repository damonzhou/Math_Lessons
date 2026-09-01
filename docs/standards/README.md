# 课程标准版本库

本目录保存 **Math_Lessons 的版本化课程标准**，用于避免课程要求因会话、模型或临时讨论发生隐性漂移。

## 当前版本

先读取：[CURRENT.md](./CURRENT.md)

当前规范由 **v1.3 + v1.4 + v1.5 + v1.6 + v1.7** 共同组成：

- [v1.7｜2026-09-01](./course-standard-v1.7.md) — **当前增量标准**；36讲教材映射、R0.5 教材映射门禁
- [v1.6｜2026-09-01](./course-standard-v1.6.md) — Markdown / LaTeX 渲染稳健性、简单数值/单位文本化、R11 自动检查
- [v1.5｜2026-09-01](./course-standard-v1.5.md) — Mainline / Extension 分层、需要时提示学习机制、R0 主线定位审查
- [v1.4｜2026-08-31](./course-standard-v1.4.md) — AMC / IMO / CMO 等国内外权威奥赛题源池及适龄筛选规则
- [v1.3｜2026-08-31](./course-standard-v1.3.md) — 当前完整基础标准；权威一手来源门槛 + 每讲 Release Review 强制门禁
- **v1.2｜2026-08-31** — 过渡版本：引入“每讲发布前整体 Review”；当时未单独保留版本快照，相关规则已完整继承并固化于 v1.3
- [v1.1｜2026-08-31](./course-standard-v1.1.md) — 扩展国内权威竞赛/奥赛与历年真实考试题源
- [v1.0｜2026-08-31](./course-standard-v1.0.md) — 初始完整标准快照

> **历史完整性说明**：不事后伪造缺失的 v1.2 快照。版本索引如实记录其为过渡版本；当前和未来工作只依赖实际存在并由 `CURRENT.md` 指定的版本文件。

## 版本管理原则

1. 已归档版本只读，不覆盖；
2. 细则升级创建 v1.x；
3. 课程理念、难度体系、主线或诊断体系实质变化时升级主版本；
4. `CURRENT.md` 唯一指定当前生效规范；
5. 跨会话继续课程时，以本目录为准，不依赖聊天记忆；
6. 不为补齐编号而事后伪造历史标准快照。

## 教材映射门禁｜v1.7

七上 Mainline 必须同时读取：

- [36讲 ↔ 当前人教版教材映射](../textbook-mapping-grade-07-semester-1.md)

每个正式 Lesson 必须记录：

- 当前教材章/知识节点；
- DIRECT / SPLIT / INTEGRATED / BRIDGE 映射类型；
- Core 与 Advanced/Olympiad 的边界。

人教社未公开完整新版细小节编号时，只写可权威核实的章名/知识节点，不猜编号。

Release Review 从 v1.7 起新增 **R0.5 教材映射**。

## Mainline / Extension 原则｜v1.5

正式编号 Lesson 优先保持：

$$
\boxed{\text{课标要求}+\text{人教版顺序}+\text{知识依赖}+\text{认知连续性}}
$$

Advanced / Olympiad / Informatics 内容可以加深课程，但不能只因为“数学上有关联”就打断更强的主线依赖。

主要属于方法论、竞赛或信息学的专题优先放入 `extensions/`，后续真正需要时由 Mainline 显式提示学习。

## Markdown / LaTeX 稳健性｜v1.6

课程以 GitHub Web / Mobile 稳定显示为优先：

- 标题禁止 `$...$`；
- 简单数值/单位优先普通文本，如 `−5`、`0 ℃`、`3 cm`、`20%`；
- LaTeX 留给分数、变量、方程、不等式、根式等真正需要数学结构的内容；
- 发布前运行 `tools/lint_markdown_rendering.py`；
- GitHub Actions 自动检查本次变更的 Markdown；
- Release Review 包含 **R11 Markdown / LaTeX 渲染稳健性**。

## 权威来源原则

课程设计依据必须回到权威一手资料：

- 教育部、人教社等官方课程/教材资料；
- MAA AMC、IMO 官方站、CEMC、UKMT 等赛事主办方官方题目和解答；
- 中国数学会官方 CMO / 全国高中数学联赛等正式竞赛资料；
- 教育主管部门、考试机构、学校正式试卷或可靠正式出版物。

新闻、自媒体、商业题库转载、论坛和搜索摘要不得作为课程事实依据或真题认证依据。搜索工具只用于定位一手资料。

## Release Review

每个 Mainline Lesson 首次发布或重大更新前必须整体 Review：

- R0 主线定位；
- **R0.5 教材映射**；
- R1 课程逻辑；
- R2 知识覆盖；
- R3 概念深度；
- R4 知识边界；
- R5 应用场景；
- R6 例题梯度；
- R7 题源；
- R8 错误习惯；
- R9 Final Challenge；
- R10 前后衔接；
- R11 Markdown / LaTeX 渲染稳健性。

正式 Review 存入：

```text
reviews/XX-lesson-release-review-vX.Y.md
```
