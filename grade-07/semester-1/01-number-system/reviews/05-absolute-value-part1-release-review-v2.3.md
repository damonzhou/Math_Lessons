# Lesson 5 Release Review｜绝对值（一）｜v2.3

> **课程标准**：v2.3  
> **结论**：PASS（以两项 CI 成功为最终发布条件）

---

## R0｜Mainline 定位

PASS。

绝对值紧接数轴与相反数；Lesson 5 负责距离意义和逆向信息恢复，Lesson 6 再进入含字母分类与多层结构。

## R0.5｜教材映射

PASS。

当前人教版七上 · 有理数 · 绝对值；`SPLIT`。

## R1｜课程逻辑

PASS。

```text
Gap Check
→ 绝对值信息本质
→ 多对象恢复
→ T0测上限
→ Builder短板分流
→ Competition Bridge
→ Elite Final
→ T2陌生迁移
```

## R2｜教材完整覆盖

PASS。

定义、具体数求绝对值、0、正负数、相反数绝对值、坐标/距离辨析均在 Gap Check 与 Concept Deepening 中覆盖。

## R2.7｜Audience / Advancement Fit

PASS。

本讲已从“从零讲授型”调整为“已学基础后的查漏补缺 + 拔高”：

- 基础用10～15分钟 Gap Check；
- 基础稳定时快速通过；
- 主要增量放在逆向恢复、条件筛选、完整枚举、最少信息和一般化；
- CEMC 前段题降级为 Competition Bridge；
- Elite 由高区分度、当前知识可解的 DESIGNED 题承担。

## R3｜概念深度

PASS。

绝对值不再只解释为“距离”，进一步理解为：

```text
坐标信息
→ 保留距离
→ 丢失方向
```

Homework 继续扩展到“标签与距离对应关系也可能丢失”。

## R3.5｜Ceiling Diagnostic

PASS。

新 T0 从旧4对象恢复升级为7标签问题，能区分：

```text
A 逆向建模
B 条件筛选
C 枚举完整
D 完整性证明
E 最少信息证明
F 一般化
```

不是只测最终是否算对。

## R3.6｜Ceiling Builder

PASS。

Builder 按 T0 首个卡点分流，而不是所有学生做同样5题：

- A：逆向模型；
- B：条件作用；
- C：独立选择/完整枚举；
- D：最少性证明；
- E：高水平参数一般化。

符合“提升短板而不是堆题量”。

## R3.7｜思维深度

PASS。

覆盖 D1～D6：

- D1：重复绝对值 → 相反位置组；
- D2：条件消除自由选择、冗余条件；
- D3：删条件后状态数变化；
- D4：不重不漏、最少询问下界；
- D5：推广到 k 个不同正距离组；
- D6：数轴 ↔ 记录器 ↔ 标签信息丢失。

高阶难度来自结构组织，不是长计算。

## R4｜知识边界

PASS。

没有提前正式教授：

- Lesson 6 的字母绝对值完整分类；
- 多层绝对值方程；
- 两点距离公式；
- 绝对值不等式；
- 正式组合数学/信息论。

“2 × 2”“最少询问”仅使用小学阶段可理解的二选一逻辑。

## R5｜应用与迁移

PASS。

本讲应用不再只换故事，而是改变信息模型：

- 主课：只丢方向；
- Homework Elite：方向 + 标签对应关系同时丢失；
- T2：传感器偏差幅度。

## R6｜难度梯度

PASS。

```text
Gap Check ★
→ Concept ★★～★★★
→ School Advanced ★★★
→ T0 ★★★★
→ Bridge ★★★
→ Final ★★★★～★★★★★
```

Competition Bridge 的真题难度不再被虚高标注。

## R7｜题源质量

PASS。

实际采用 CEMC 2021/2022/2026 一手来源作为 Bridge；AMC/UKMT/IMO/CMO/CEMC高阶等候选池有明确审查和未选理由。

特别记录 CEMC 2026 G8 Q25：结构价值高，但涉及任意两点距离重建，更适合 Lesson 8，不为了提高名义难度提前使用。

## R7.5｜题目级官方链接

PASS。

所有 `ADAPTED` CEMC 题在题旁直接给官方原题和解答链接；T0/Final/Homework Elite 标记为 `DESIGNED`，不伪造真题链接。

## R8｜错误与习惯诊断

PASS。

重点：H3/H5/H7/H9/H10，并把 T0 首个卡点映射到具体 Builder。

这次新增的重要诊断：

> 学生是“不会”，还是“会做但不会证明完整/最少”。

## R9｜Elite / Final Challenge

PASS。

Final 包含：

- 8标签；
- 3组重复绝对值；
- 条件强迫方向；
- 冗余条件识别；
- 8种状态完整证明；
- 最少3次询问的上界/下界；
- k 组不同正距离的一般化。

目标为优秀七年级学生完整独立思考20～30分钟。

如果实际学生15分钟内完全独立并一般化，diagnostics 明确规定进一步上调 Lesson 6 Ceiling 难度。

## R10｜前后衔接

PASS。

Lesson 5 已建立：

```text
绝对值逆向
+ 条件
+ 独立选择
+ 完整性
```

Lesson 6 可以自然升级为：

```text
字母
+ 分类
+ 多层绝对值
+ 参数/边界
```

## R11｜Markdown / LaTeX

待 CI 最终确认。

必须同时通过：

```text
Markdown Render Lint
Problem Source Link Lint
```

---

# 最终结论

**PASS（CI 条件式）**。

Lesson 5 v2.3 已从“概念讲深但题目偏基础”升级为：

> **基础快速查漏 + 高区分度上限测试 + 首个卡点诊断 + 短板分流 Builder + 不同表面 Elite 迁移。**
