# 课程标准版本库

本目录保存 **Math_Lessons 的版本化课程标准**，用于避免课程要求因会话、模型或临时讨论发生隐性漂移。

## 当前版本

先读取：[CURRENT.md](./CURRENT.md)

当前规范由 **v1.3～v1.9 + v2.0 + v2.1** 共同组成：

- [v2.1｜2026-09-05](./course-standard-v2.1.md) — **当前增量标准**；题目级官方原题/解答链接、SYNTHESIS 结构来源、R7.5 可追溯性门禁
- [v2.0｜2026-09-02](./course-standard-v2.0.md) — Ceiling Builder 能力上限提升体系、T0/T1/T2 迁移验证、R3.6 门禁
- [v1.9｜2026-09-02](./course-standard-v1.9.md) — 最高深度覆盖、Ceiling Diagnostic、R3.5 能力上限诊断门禁
- [v1.8｜2026-09-01](./course-standard-v1.8.md) — provenance 候选权威题源池审查可见性、简单变量/符号表达文本化
- [v1.7｜2026-09-01](./course-standard-v1.7.md) — 36讲教材映射、R0.5 教材映射门禁
- [v1.6｜2026-09-01](./course-standard-v1.6.md) — Markdown / LaTeX 渲染稳健性、R11 自动检查
- [v1.5｜2026-09-01](./course-standard-v1.5.md) — Mainline / Extension 分层、需要时提示学习机制、R0 主线定位审查
- [v1.4｜2026-08-31](./course-standard-v1.4.md) — AMC / IMO / CMO 等国内外权威奥赛题源池及适龄筛选规则
- [v1.3｜2026-08-31](./course-standard-v1.3.md) — 完整基础标准；权威一手来源门槛 + 每讲 Release Review 强制门禁
- **v1.2｜2026-08-31** — 过渡版本；未单独保留快照，规则已由 v1.3 继承
- [v1.1｜2026-08-31](./course-standard-v1.1.md)
- [v1.0｜2026-08-31](./course-standard-v1.0.md)

> 已归档版本只读；`CURRENT.md` 唯一指定当前生效规范。全局规则变化必须新增版本，不覆盖历史版本。

---

## v2.1｜题目级原题链接可追溯性

provenance 记录来源不再视为足够。

凡题目使用真实考试/竞赛来源：

- `SOURCE`：题目旁直接给官方原题链接；
- `ADAPTED`：题目旁直接给官方原题链接，并明确是改编；
- 有官方解答时同时给官方解答链接；
- `SYNTHESIS`：明确“无单一原题”，若来自具体题目结构则直接列出结构来源链接；
- `DESIGNED / TEXTBOOK-MODEL` 不伪造原题链接。

Release Review 新增 **R7.5 题目级原题链接可追溯性**。

从 Lesson 7 起原生执行；Lesson 3～6 的已有来源题回填官方链接。

---

## v2.0｜能力上限提升体系

核心原则：

> **课标和人教版决定知识边界、主线和不可遗漏内容，但不作为课程深度上限。**

每个 Mainline Lesson 必须覆盖六层：

1. L1 教材完整；
2. L2 概念深度；
3. L3 校内高阶；
4. L4 竞赛/信息学陌生迁移；
5. L5 Ceiling Diagnostic：测当前独立发现上限；
6. L6 Ceiling Builder：针对真实卡点系统训练并提高上限。

三种高阶任务必须分离：

- **Ceiling Diagnostic**：方法尚未完整教学时测上限；
- **Ceiling Builder**：训练表示转换、条件变化、反例、逆向构造、多方法、一般化、陌生迁移；
- **Mastery / Final Challenge**：教学后检验稳定迁移和一般化。

能力变化记录：

```text
T0 冷启动
→ T1 教学后新题迁移
→ T2 约7天后不同表面结构迁移
```

主要观察 Hint 是否减少、结构识别是否更早、是否能主动换表示/构造反例/一般化，以及 H1～H10 是否下降。

---

## Lesson 1～4 v2.0 迁移状态

[查看完整审计](../audits/lessons-01-04-ceiling-building-audit-v2.0.md)

当前状态：

> **Lesson 1～4 已完成 v2.0 迁移，L1～L6、Diagnostic / Builder / Mastery、T0/T1/T2、题源补充和 v2.0 Review 均已建立。**

Lesson 5 起必须从首次建设就原生采用 v2.0，不再事后补 Ceiling 模块。

---

## 题源与候选池可见性

每个 Lesson provenance 必须明确：

- 实际采用来源；
- AMC / IMO / CMO / CEMC / UKMT / 国内正式考试等候选权威题源池审查；
- Ceiling Diagnostic 的来源与诊断区分度；
- Ceiling Builder 的训练目标/来源；
- Mastery Challenge 与前述任务的结构差异。

赛事越高级不等于越适合当前阶段。选择按：

```text
教学匹配度
+ 权威性
+ 当前可解性
+ 结构新颖度
+ 诊断区分度
+ 训练增益价值
+ 一般化价值
```

---

## 教材映射与 Mainline / Extension

七上 Mainline 必须读取：

- [36讲 ↔ 当前人教版教材映射](../textbook-mapping-grade-07-semester-1.md)

正式 Lesson 优先保持课标、人教版顺序、知识依赖和认知连续性。主要属于方法论、竞赛或信息学的专题优先进入 `extensions/`，后续需要时再显式提示学习。

---

## Markdown / LaTeX 稳健性

- 标题禁止 `$...$`；
- 简单数值、单位、简单变量/带符号变量使用普通文本；
- LaTeX 留给真正需要数学结构的表达；
- 发布前运行 `tools/lint_markdown_rendering.py`；
- GitHub Actions 自动检查；
- Release Review 包含 R11。

---

## Release Review 完整顺序

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
- **R7.5 题目级官方原题链接可追溯性**；
- R8 错误习惯；
- R9 Mastery / Final Challenge；
- R10 前后衔接；
- R11 Markdown / LaTeX。

只有 R3.5、R3.6、R7.5 都通过，且其余 Release Review 项通过，才能标记课程发布完成。