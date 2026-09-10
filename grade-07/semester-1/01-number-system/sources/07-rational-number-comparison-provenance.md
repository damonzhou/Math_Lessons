# Lesson 7 题源与命题依据｜有理数大小比较｜v2.3

> **主题**：有理数大小比较、绝对值次序、未知符号、部分信息排序、反推、完整性与最少信息  
> **标准**：v2.3 + v2.1 题目级官方链接规则

---

# 1｜教材与课程依据

## S0｜教育部《义务教育数学课程标准（2022年版）》

官方文件：

https://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582346895190.pdf

第四学段要求理解有理数，能用数轴上的点表示有理数并比较大小，并借助数轴理解相反数和绝对值。

本讲 Core / Gap Check 据此确保：

```text
数轴左右顺序
+ 正负与0
+ 两个负数借绝对值比较
+ 多种表示排序
```

完整覆盖。

## S1｜人民教育出版社当前初中数学新教材介绍

官方页面：

https://www.pep.com.cn/xw/zt/hd/12/xjcjs/cz/202408/t20240826_1994351.html

用途：确认当前教材依据2022版课标重构，课程不猜未公开完整的小节编号。

## S2｜人教社教材结构解读

官方页面：

https://www.pep.com.cn/xw/zt/hd/12/zbtjc/202410/t20241022_1996035.html

用途：支持把知识联系、数学本质和思维过程放在机械规则之前。

---

# 2｜实际采用的权威竞赛来源

## S3｜CEMC 2018 Gauss Grade 7 Question 6

**标签**：`ADAPTED · Competition Bridge`  
**角色**：区间与双边顺序条件，不承担 Elite 难度。

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2018Gauss7Contest.html

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018GaussSolution.pdf

原题要求判断一个数是否位于3与4之间。本讲改为负区间，并要求把语言条件转换为完整双边不等关系。

## S4｜CEMC 2026 Gauss Grade 7 Question 3

**标签**：`ADAPTED · Competition Bridge`  
**角色**：区分“原数大小”和“离0距离”，不承担 Elite 难度。

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026Gauss7Contest.html

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026GaussSolution.html

本讲改编同时询问最大、最小、最近、最远，迫使学生区分两种排序对象。

---

# 3｜为什么 v2.2 最高层不够

旧 T0：

```text
0 < a < b
→ 排序 a,b,−a,−b
```

旧 Final：

```text
重复绝对值
→ 恢复相反数对
→ 用负数个数确定剩余符号
```

这些内容具有概念深度，但对已经掌握基础的优秀学生而言，结构暴露较明显，更接近：

```text
★★★ 概念深化 / 校内中高阶
```

不足以稳定承担 v2.3：

```text
★★★★～★★★★★ Elite / Final Challenge
```

因此 Lesson 7 v2.3 不增加长计算，而是更换高阶结构。

---

# 4｜v2.3 Ceiling Diagnostic 来源

## D0｜三个标签只有绝对值顺序

**标签**：`DESIGNED · Ceiling Diagnostic · ★★★★`  
**无单一原题。**

条件：

```text
0 < |a| < |b| < |c|
```

要求学生：

- 找出 a、b、c 全部可能标签排序；
- 证明6种排列中两种不可能；
- 发现 |c| 最大意味着 c 必在一个极端；
- 从排序反推 b、c 符号；
- 发现 a 的符号无法从排序恢复；
- 不靠8格符号表证明不重不漏。

### 为什么使用 DESIGNED

本题需要精确诊断一种当前课程能力：

```text
绝对值严格次序
→ 极端元素
→ 标签排序
→ 反推符号
→ 信息不可恢复
```

当前审查到的适龄官方原题没有一题同时覆盖该结构且不依赖后续知识。

透明原创比“为了真题标签降低结构匹配度”更符合 v2.3。

---

# 5｜v2.3 School Advanced 核心结构

## A0｜绝对值更大的那个数控制两数顺序

在：

```text
0 < |a| < |b|
```

下：

```text
b > 0 → a < b
b < 0 → a > b
```

反向也成立。

这不是额外公式，而是数轴结构的压缩表达。

它把学生从：

```text
每题分四种符号猜
```

提升到：

```text
找绝对值更大的对象
→ 看它在哪一侧
→ 直接决定相对顺序
```

这是 T0 与 Final 的核心局部定理。

---

# 6｜v2.3 Elite / Final Challenge 来源

## M0｜四个标签的顺序密码

**标签**：`SYNTHESIS · Elite / Final Challenge · ★★★★～★★★★★`  
**无单一原题。**

条件：

```text
0 < |a| < |b| < |c| < |d|
```

最高层要求：

1. 证明最大绝对值标签 d 只能在最左或最右；
2. 删除 d 后对 c 重复；
3. 不枚举16种符号组合生成全部8种标签顺序；
4. 从最终排名反推 b、c、d 的符号；
5. 证明 a 的符号不可由排名恢复；
6. 用一次额外方向询问恢复全部符号；
7. 同时证明“0次不够、1次足够”；
8. 推广到5变量和递归结构。

### 结构来源

- 人教版当前知识：数轴、相反数、绝对值、大小比较；
- S3：顺序/区间条件意识；
- S4：原数次序与距离次序必须区分；
- v2.3：部分信息、完整性、最少信息、递归一般化。

结构 Bridge 官方链接：

- https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2018Gauss7Contest.html
- https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026Gauss7Contest.html

本题不是这两道 Gauss 题的改写，不标 `ADAPTED`；它是透明 `SYNTHESIS`。

---

# 7｜候选权威题源池审查｜v2.3

| 题源池 | 审查 | 采用 | v2.3 结论 |
|---|---|---|---|
| 教育部课标 | 是 | 是 | 决定知识边界 |
| 人民教育出版社 | 是 | 是 | 决定 Mainline / Core |
| CEMC Gauss | 是 | 是 | 2018 G7 Q6、2026 G7 Q3 继续作为 Bridge；明确不把前段题冒充 Elite |
| CEMC Gauss 中后段 / Part C | 是 | 否 | 审查了更高题位，但当前可核验题主要转向其他主题；没有找到同时聚焦“未知符号 + 绝对值排名反推”且只需当前知识的直接原题 |
| UKMT JMC | 是 | 否 | 审查 2017 JMC Q7 等排序问题；官方 Extended Solutions：https://ukmt.org.uk/wp-content/uploads/2023/08/jmc-2017-extended.pdf 。其主要压力来自分数表达求值与统一分母，不如本讲目标结构匹配，因此不作为 Elite |
| UKMT JMO | 是 | 否 | 证明型价值高，但当前节点直接匹配题不足；不因难度高而硬塞 |
| MAA AMC 8 | 是 | 否 | 继续作为正式候选池；当前未找到比 D0/M0 更直接且无需额外知识的官方可追溯问题 |
| AMC 10/12、AIME | 是 | 否 | 多数题需要更高代数工具；当前不以超前知识制造难度 |
| USAJMO/USAMO | 是 | 否 | 证明层级与当前知识节点不匹配 |
| IMO / Shortlist | 是 | 否 | 可作未来结构灵感，不直接用于本讲 |
| CMO / 全国高中数学联赛 / 女奥 | 是 | 否 | 年龄/知识边界不匹配 |
| 国内正式考试压轴 | 是 | 否 | 当前未选到来源一手、结构增益高于本次 D0/M0 的直接题；不使用商业题库转载 |
| CSP-J / NOI | 是 | 否 | 本讲信息学迁移采用透明“排名后信息恢复”设计，不伪装竞赛原题 |

### 选择结论

v2.3 不再采用：

> “只要是真题就比原创深”

而采用：

```text
官方真题 → 负责真实迁移与校准
高匹配 DESIGNED / SYNTHESIS → 负责能力上限诊断与提升
```

前提是所有标签和来源关系透明。

---

# 8｜题目级链接审查

- 主课 C1：`ADAPTED · CEMC 2018 G7 Q6`，题旁有官方原题 + 官方解答；
- 主课 C2：`ADAPTED · CEMC 2026 G7 Q3`，题旁有官方原题 + 官方解答；
- Homework Q14/Q15：同样题旁直接列官方链接；
- Final：`SYNTHESIS · 无单一原题`，主课直接列结构 Bridge 官方来源；
- Ceiling Diagnostic：`DESIGNED`，不伪造真题来源。

---

# 9｜知识边界审查

v2.3 高阶层不依赖：

- 有理数加减运算法则；
- 解不等式；
- 绝对值不等式；
- 函数单调性；
- 高中代数。

最高难度来自：

```text
极端结构
+ 部分信息
+ 递归剥离
+ 反推
+ 不可能性证明
+ 完整性证明
+ 最少信息证明
```

符合“Deep Reasoning > Harder Arithmetic”。
