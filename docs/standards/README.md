# 课程标准版本库

本目录保存 **Math_Lessons 的版本化课程标准**，用于避免课程要求因会话、模型或临时讨论发生隐性漂移。

## 当前版本

先读取：[CURRENT.md](./CURRENT.md)

当前规范由 **v1.3～v1.9 + v2.0** 共同组成：

- [v2.0｜2026-09-02](./course-standard-v2.0.md) — **当前增量标准**；Ceiling Builder 能力上限提升体系、T0/T1/T2 迁移验证、R3.6 门禁
- [v1.9｜2026-09-02](./course-standard-v1.9.md) — 最高深度覆盖、Ceiling Diagnostic、R3.5 能力上限诊断门禁
- [v1.8｜2026-09-01](./course-standard-v1.8.md) — provenance 候选权威题源池审查可见性、简单变量/符号表达文本化
- [v1.7｜2026-09-01](./course-standard-v1.7.md) — 36讲教材映射、R0.5 教材映射门禁
- [v1.6｜2026-09-01](./course-standard-v1.6.md) — Markdown / LaTeX 渲染稳健性、R11 自动检查
- [v1.5｜2026-09-01](./course-standard-v1.5.md) — Mainline / Extension 分层、需要时提示学习机制、R0 主线定位审查
- [v1.4｜2026-08-31](./course-standard-v1.4.md) — AMC / IMO / CMO 等国内外权威奥赛题源池及适龄筛选规则
- [v1.3｜2026-08-31](./course-standard-v1.3.md) — 完整基础标准；权威一手来源门槛 + 每讲 Release Review 强制门禁
- **v1.2｜2026-08-31** — 过渡版本：引入“每讲发布前整体 Review”；未单独保留快照，规则已由 v1.3 继承
- [v1.1｜2026-08-31](./course-standard-v1.1.md) — 扩展国内权威竞赛/奥赛与历年真实考试题源
- [v1.0｜2026-08-31](./course-standard-v1.0.md) — 初始完整标准快照

> **历史完整性说明**：不事后伪造缺失的 v1.2 快照。

## 版本管理原则

1. 已归档版本只读，不覆盖；
2. 细则升级创建 v1.x；
3. 课程理念、难度体系、主线或诊断/训练体系发生实质变化时升级主版本；
4. `CURRENT.md` 唯一指定当前生效规范；
5. 跨会话继续课程时，以仓库标准为准；
6. 不为补齐编号而伪造历史标准。

---

## 能力上限提升体系｜v2.0

v1.9 解决“测得准”，v2.0 进一步要求“练得高”。

每讲从五层升级为六层：

1. L1 教材完整；
2. L2 概念深度；
3. L3 校内高阶；
4. L4 竞赛/信息学陌生迁移；
5. L5 Ceiling Diagnostic：测当前独立发现上限；
6. **L6 Ceiling Builder：针对真实卡点系统训练并提高上限。**

三种高阶任务必须区分：

- **Ceiling Diagnostic**：方法尚未完整教学时测上限；
- **Ceiling Builder**：针对卡点训练表示转换、条件变化、反例、逆向构造、多方法、一般化、陌生迁移；
- **Mastery / Final Challenge**：教学后测迁移和一般化。

能力变化建议记录：

```text
T0 冷启动
→ T1 教学后新题迁移
→ T2 约7天后不同表面结构迁移
```

真正的提升不只看最终正确率，还看：Hint 是否减少、结构识别是否更早、能否构造反例、能否一般化、同类 H 错误是否下降。

前4课 v2.0 审计：

- [Lesson 1～4 能力上限提升审计](../audits/lessons-01-04-ceiling-building-audit-v2.0.md)

当前结论：原教学内容仍 PASS；L5 Diagnostic 和 L6 Builder 需要系统补齐后，才能标记“最高深度 + 能力上限提升体系完成”。

---

## 最高深度与上限诊断｜v1.9

核心原则：

> **课标是底线和边界，不是课程深度上限。**

Ceiling Diagnostic 必须在 Advanced/Olympiad 方法完整教学前冷启动，第一次不开放 Hint，并按 C5-A～F 记录学生独立发现程度。

历史兼容审计：

- [Lesson 1～4 最高深度/上限诊断审计](../audits/lessons-01-04-depth-ceiling-audit-v1.9.md)

---

## 题源候选池可见性｜v1.8+

每个 Lesson provenance 必须明确：

- 实际采用来源；
- 候选权威题源池审查；
- Ceiling Diagnostic 来源与区分度；
- 从 v2.0 起还要记录 Ceiling Builder 的训练目标/来源，以及 Mastery Challenge 与前述任务的结构差异。

即使某讲没有实际使用 AMC / IMO / CMO，也要写明已经审查以及为什么没有选用。

---

## 教材映射门禁｜v1.7

七上 Mainline 必须读取：

- [36讲 ↔ 当前人教版教材映射](../textbook-mapping-grade-07-semester-1.md)

每个正式 Lesson 必须记录教材章/知识节点、映射类型、Core 与 Advanced/Olympiad 边界。

---

## Mainline / Extension 原则｜v1.5

正式编号 Lesson 优先保持课标、人教版顺序、知识依赖和认知连续性。主要属于方法论、竞赛或信息学的专题优先进入 `extensions/`，后续需要时再显式提示学习。

---

## Markdown / LaTeX 稳健性｜v1.6 + v1.8

- 标题禁止 `$...$`；
- 简单数值/单位使用普通文本；
- 简单变量/带符号变量/与0简单比较使用普通文本；
- LaTeX 留给真正需要数学结构的表达；
- 发布前运行 lint；
- GitHub Actions 自动检查；
- Release Review 包含 R11。

---

## 权威来源原则

课程设计和题源认证必须回到权威一手资料：教育部、人教社、MAA AMC、IMO、CEMC、UKMT、中国数学会 CMO / 全国高中数学联赛、正式考试原卷及可靠正式出版物。

新闻、自媒体、商业题库转载、论坛和搜索摘要不得作为课程事实依据或真题认证依据。

---

## Release Review

当前完整顺序：

- R0 主线定位；
- R0.5 教材映射；
- R1 课程逻辑；
- R2 知识完整覆盖；
- R3 概念深度；
- **R3.5 最高深度与能力上限诊断**；
- **R3.6 能力上限提升设计**；
- R4 知识边界；
- R5 应用场景；
- R6 例题梯度；
- R7 题源及候选池；
- R8 错误习惯；
- R9 Mastery / Final Challenge；
- R10 前后衔接；
- R11 Markdown / LaTeX。

只有 R3.5 和 R3.6 都通过，才可以标记：

> **最高深度 + 能力上限提升体系完成。**
