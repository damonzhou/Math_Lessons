# 第3讲题源与命题依据｜v1.4

> 对应主课：[第3讲《分类是一种数学方法——集合、包含与“不重不漏”》](../03-classification-sets-partitions.md)
>
> 课程标准：[CURRENT v1.4](../../../../docs/standards/CURRENT.md)
>
> 本文件只采用课程标准允许的权威一手来源。搜索引擎只用于定位官方资料，不作为题源认证依据。

---

# 1. 课程与知识边界依据

## P0｜教育部《义务教育数学课程标准（2022年版）》

官方 PDF：

https://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582346895190.pdf

本讲服务于第四学段“数与式”中有理数理解，并重点发展：

- 数学抽象；
- 推理意识；
- 分类讨论；
- 从具体对象发现共同结构；
- 解决问题时选择合适表示和方法。

## P1｜人民教育出版社官方资源

https://www.pep.com.cn/

用于确定七年级有理数主线及当前知识边界。

### 边界说明

“集合”不是当前人教版七年级独立正式章节。

因此本讲：

- `MUST` 是分类标准、不重不漏、包含/相交直觉、奇偶与余数分类；
- `\in`、`\subseteq` 等形式化集合符号只放 `SHOULD / EXTENSION`；
- 不提前讲高中集合运算体系。

---

# 2. 权威竞赛题源

## A1｜2023 MAA AMC 8, Problem 16

官方解答 PDF：

https://maa.org/wp-content/uploads/2024/08/2023_AMC8_Solutions_.pdf

原题核心：P、Q、R 按周期规律填入 $20\times20$ 表格，统计三类字母数量。

官方解答明确使用：

$$
400=3\times133+1
$$

并用周期3、商和余数解释三类数量关系。

### 本讲用途

支持：

- 周期问题 → 余数分类；
- 先识别周期长度，再研究商和余数；
- 当堂 Q11 和主课周期窗口。

本讲大幅简化表格结构为线性周期，因此标记：

> `ADAPTED · 2023 AMC 8 Problem 16`

不是 AMC 原题。

### 题号校验

2023 AMC 8 **Problem 16** 才是 P/Q/R 周期表格题。

Problem 18 是 Greta Grasshopper 的 $+5/-3$ 跳格题，不能把二者混淆。

---

## G1｜2026 CEMC Gauss Grade 7, Question 19

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026Gauss7Contest.html

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026GaussSolution.html

原题核心：从100到199的正整数中，同时要求：

- 在指定范围；
- 能被4整除；
- 数位和满足条件；

再统计符合条件的整数数量。

### 本讲用途

支持：

> **大集合 → 先用强条件筛选 → 再检查第二条件。**

主课例17、当堂 Q8、课后 Q6 都只保留“逐层筛选”结构并改动范围/数字，因此属于 `ADAPTED`。

---

## G2｜2026 CEMC Gauss Grade 7, Question 20

官方原题同：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026Gauss7Contest.html

原题核心：85个冰淇淋分为巧克力、香草和 twist（同时含巧克力、香草），已知“含巧克力”和“含香草”的比例，求 twist 数量。

### 本讲用途

支持：

- 两个性质集合可以相交；
- 相加时共同部分被计算两次；
- 从重复计数反求交集。

主课和练习改成饮料/社团情境及不同数字，因此标记 `ADAPTED`，不复制原题。

---

## I1｜IMO 2021 Shortlist A1｜方法参考

IMO 官方 Shortlist：

https://www.imo-official.org/problems/IMO2021SL.pdf

该题官方解法中使用了：

> **partition（分组） + Pigeonhole Principle（抽屉原理）**

的结构。

### 本讲用途

只用于说明“分组/分类 + 抽屉原理”是正式高水平竞赛数学中长期使用的方法。

本讲没有改编 IMO 2021 A1 原题本身，也没有把七年级训练题标为 IMO 真题。

因此 I1 属于：

> **方法论 / 高阶结构依据，不是具体题源标签。**

---

# 3. 为什么本讲没有强行加入 CMO / IMO 原题

课程标准 v1.4 要求主动检查 AMC / IMO / CMO 等权威来源，但同时规定：

$$
\text{当前知识可解}+\text{服务本讲核心}
$$

优先于赛事等级。

本讲当前最适配的直接真题结构来自：

- AMC 8；
- CEMC Gauss。

IMO / CMO 大量原题依赖更成熟的数论、代数、几何或证明能力。

因此本讲只引用 IMO 官方资料说明“分组 + 抽屉原理”的竞赛地位，不为了“题源看起来高级”而超纲。

---

# 4. 主课内容审计

| 内容 | 类型 | 依据 / 教学目的 |
|---|---|---|
| 分类标准、不重不漏 | TEXTBOOK-MODEL + DESIGNED explanation | 整理 Lesson 1/2 已出现的分类思想 |
| 元素/集合直觉 | DESIGNED · SHOULD | 为分类语言服务，不提前集合论 |
| 属于/包含 | DESIGNED · SHOULD | 区分对象—集合和集合—集合关系 |
| 互斥/包含/相交 | DESIGNED + G2 | 建立类别关系框架 |
| 奇偶分类 | TEXTBOOK-MODEL | 经典完整分类 |
| $n=mq+r$ | TEXTBOOK-MODEL + Advanced | 从小学余数推广为统一分类语言 |
| 负整数非负余数 | DESIGNED | 防止只会处理正整数 |
| 周期与余数 | ADAPTED · A1 | AMC 8 官方结构 |
| 多条件筛选 | ADAPTED · G1 | Gauss 官方结构 |
| 重复计数/交集 | ADAPTED · G2 | Gauss 官方结构 |
| 模6统一奇偶/3倍数 | SYNTHESIS | Lesson 2 移交的分类方法主线 |
| 抽屉原理 | DESIGNED + I1 method reference | 分类之后的竞赛方法 |
| if/else 与独立布尔 | DESIGNED · Informatics | 数学关系映射到控制流 |

---

# 5. 当堂训练题源审计

## Core Q1～Q6

以 `TEXTBOOK-MODEL / DESIGNED DIAGNOSTIC` 为主：

- 检查分类标准；
- 奇偶；
- 非负余数；
- 平级/包含/相交关系。

这些属于概念诊断，现成真题未必比定向原创更有效，因此保留少量 `DESIGNED`。

## Advanced Q7～Q10

- Q7：`ADAPTED · G2`，相交集合与重复计数；
- Q8：`ADAPTED · G1`，逐层筛选；
- Q9/Q10：`DESIGNED`，为模6和更细分类搭桥。

## Olympiad Q11～Q13

- Q11：`ADAPTED · A1`，周期3 → 商余数；
- Q12：`SYNTHESIS / DESIGNED`，余数分类 + 抽屉原理；I1只作为高阶方法参考；
- Q13：`DESIGNED`，最小公倍数作为统一周期直觉。

## Informatics Q14～Q16

均为 `DESIGNED`，因为目标是精确映射当前数学概念到控制流，而不是模拟正式编程竞赛题。

---

# 6. Final Challenge 审计

类型：

> `SYNTHESIS · A1 + G1/G2 + 本讲模6分类思想`

题目不是某一届竞赛原题。

## 结构来源

- A1：周期/余数分类；
- G1：多条件筛选；
- G2：两个性质集合相交；
- 本讲：模6同时编码奇偶和3的整除性；
- Lesson 2 Review：原模6挑战应移动到真正以“分类方法”为核心的 Lesson 3。

## 知识边界

只需要：

- 倍数；
- 奇偶；
- 除法与余数；
- 简单计数；
- 分类；
- 条件范围。

不需要：

- 正式同余理论；
- 容斥公式；
- 高中集合运算；
- 高阶数论。

## 六项审核

- [x] 当前知识可解；
- [x] 题面不直接告诉“用模6”；
- [x] 突破口来自选择合适分类标准；
- [x] 有权威竞赛结构依据；
- [x] 有 Hint 1 → Hint 2 → Hint 3；
- [x] 解后推广到抽屉原理与任意 $m$。

---

# 7. 版权与引用方式

本仓库不大段复制 AMC / Gauss / IMO 原题。

采用：

- 官方赛事名称、年份、题号；
- 数学结构摘要；
- 改写数字/情境后的 `ADAPTED`；
- 清楚说明哪些内容是 `SYNTHESIS / DESIGNED`。

---

# 8. 来源限制

以下来源不能认证本讲题源：

- 新闻；
- 自媒体；
- 商业题库转载；
- 论坛/博客；
- 搜索摘要；
- 无年份、赛事、题号的“奥赛真题合集”。

如未来加入国内考试或 CMO 真题，必须回到教育主管部门、赛事主办方、正式原卷或可靠正式出版物核验。
