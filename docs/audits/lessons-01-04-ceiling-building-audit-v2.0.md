# Lesson 1～4 能力上限提升与全课程包审计｜v2.0

> **审计标准**：课程标准 v2.0  
> **审计日期**：2026-09-02  
> **范围**：Lesson 1～4 Mainline 全课程包  
> **状态**：COMPLETE / PASS

---

# 1. 总结论

Lesson 1～4 已完成**完整 v2.0 迁移**，不是只更新主课。

每讲现在均包括并已对齐：

- 主课；
- 当堂训练答案；
- 课后练习；
- 课后练习答案；
- Ceiling Diagnostic 答案与 C5 / T0-T1-T2 记录；
- diagnostics 做题习惯诊断；
- 原 provenance + v2.0 provenance addendum；
- v2.0 Release Review。

因此当前统一状态：

> **Lesson 1～4：教材完整、最高深度、能力上限诊断、能力上限提升和配套文档一致性均 PASS。**

---

# 2. 六层覆盖

| Lesson | L1 教材完整 | L2 概念深度 | L3 校内高阶 | L4 竞赛/信息学 | L5 Diagnostic | L6 Builder | 状态 |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 正数和负数 | PASS | PASS | PASS | PASS | PASS | PASS | COMPLETE |
| 2 有理数 | PASS | PASS | PASS | PASS | PASS | PASS | COMPLETE |
| 3 数轴 | PASS | PASS | PASS | PASS | PASS | PASS | COMPLETE |
| 4 相反数 | PASS | PASS | PASS | PASS | PASS | PASS | COMPLETE |

---

# 3. Lesson 1

### Diagnostic

基准50→52、总偏差 +18→−6，冷启动检查学生能否自行发现“每个记录统一变化 → 整体变化”。

### Builder

训练：

- 基准/表示转换；
- 条件充分性；
- 反例；
- 逆向构造；
- n 个数据、基准移动 k 的一般化。

### Mastery / T2

原整体偏差挑战作为教学后 Mastery；约7天后用评分系统换基准题迁移。

### 配套一致性

homework 与答案已经同步 v2.0，旧 `$-2^\circ\mathrm C$` 等温度 LaTeX 已清除；diagnostics 已加入 C5 / T0-T1-T2 行为观察。

---

# 4. Lesson 2

### Diagnostic

设备四舍五入显示2.4，要求判断不唯一、构造反例、找完整边界并比较截断规则。

### Builder

训练：

- 一数多表示；
- 写法 vs 数学对象；
- 反例；
- 显示规则变化；
- 从具体边界推广到一般保留位数。

### Mastery / T2

0.38显示综合题作为 Mastery；T2 用正温度传感器显示3 ℃，避免引入与本讲无关的负数舍入端点干扰。

### 配套一致性

homework、answers、diagnostics 已重写，旧简单行内 LaTeX 写法已清理。

---

# 5. Lesson 3

### Diagnostic

A～F 等距，B = −1、E = 5，冷启动恢复尺度、坐标和隐藏原点；删除等距后构造反例。

### Builder

训练：

- 两锚点恢复尺度；
- 删除条件；
- 逆向设计非单位刻度数轴；
- “起点 + 间隔数 × 每格变化”的一般结构。

### Mastery / T2

Mastery 已具体化为“脱落标签”问题，避免抽象任务不可作答；T2 用机器人等距检测点迁移。

### 配套一致性

课堂答案已与具体 Mastery 对齐；homework、homework answers、diagnostics 均迁移 v2.0。

---

# 6. Lesson 4

### Diagnostic

P～T 等距，Q/T 互为相反数、P = −8，冷启动发现对称中心、隐藏原点、尺度及条件不足。

### Builder

训练：

- “−a 一定为负”的正/0/负三类检查；
- 对称结构与尺度条件分离；
- 逆向构造；
- 相反变换 R 的奇偶次复合。

### Mastery / T2

Mastery 使用“相反变换机器”，与 T0 数轴恢复保持结构差异；T2 使用 `flip` 校准系统。

### 配套一致性

课堂答案、homework、homework answers、diagnostics 均已同步 v2.0；简单变量/符号表达继续执行普通文本规则。

---

# 7. 题源体系

四讲均保留原权威 provenance，并增加 v2.0 addendum，明确区分：

- `Diagnostic`：测上限；
- `Builder`：提上限；
- `Mastery`：验迁移。

AMC、IMO、CMO、CEMC、UKMT、国内正式考试等均继续进入候选权威题源池审查；不因赛事等级机械超纲。

---

# 8. 做题习惯与长期能力

四讲 diagnostics 已同步 v2.0，重点追踪：

- 是否主动确认基准、对象、尺度；
- 是否质疑条件是否足够；
- 是否会构造反例；
- 是否能从具体推广到一般；
- H3/H7/H9/H10 等真实长期习惯是否下降；
- C5-A～F 与 T0/T1/T2 是否改善。

---

# 9. Markdown / LaTeX

本次全课程包迁移重点清理：

- 温度的 `^\circ\mathrm C` 不必要 LaTeX；
- `$-4$`、`$-a$` 等简单数值/变量行内 LaTeX；
- 标题中的数学标记；
- 旧 homework 中遗留的简单表达。

所有新提交必须继续经过 `Markdown Render Lint`。历史旧失败运行不代表当前文件状态；发布判断以当前版本提交的检查结果为准。

---

# 10. 最终状态

> **Lesson 1～4：v2.0 全课程包迁移完成，当前可正式标记 COMPLETE / PASS。**

Lesson 5 起必须从首次建设就原生执行最新 `CURRENT.md` 标准，包括：

```text
Core
→ Ceiling Diagnostic (T0)
→ Ceiling Builder
→ Advanced / Olympiad / Informatics
→ Mastery (T1)
→ 延迟陌生迁移 (T2)
```

以及完整的主课、答案、homework、provenance、diagnostics 和 Release Review 一致性检查。