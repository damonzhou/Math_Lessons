# 第1讲题源与命题依据

> 对应主课：[第1讲《从“3−5”到负数——数系为什么必须继续扩展》](../01-positive-negative-numbers.md)
>
> 本文件记录 Lesson 1 的课程边界、例题、训练题、Final Challenge 和教学方法依据。目标不是追求“全部真题”，而是做到：**课标/教材约束明确、真题来源透明、改编程度可追溯、原创有必要性说明。**

---

# 1. 课程边界依据

## P0｜《义务教育数学课程标准（2022年版）》

官方 PDF：
https://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582346895190.pdf

本讲遵循的核心方向：

- 不只学习符号和运算，还要理解数学概念产生的实际背景；
- 训练数学抽象、推理和模型意识；
- 逐步形成发现、分析和解决问题的能力。

## P1｜人民教育出版社七年级数学教材

官方页面：
https://www.pep.com.cn/products/jc/czjks/201510/t20151026_1250813.shtml

本讲主要对应“正数和负数”课内主线：

- 负数产生的必要性；
- 正数、负数和 0；
- 相反意义的量；
- 实际问题中的正负表示；
- 加工允许误差等“标准—偏差”模型。

## P2｜人民教育出版社七年级数学教师教学用书

官方页面：
https://www.pep.com.cn/products/jc/jks/201510/t20151026_1250885.shtml

用于判断：教材重点、教学设计、典型错误、练习与评价边界。

---

# 2. 题目类型标记

- **TEXTBOOK-MODEL**：有教材/教师用书模型依据，但不是教材原题；
- **SOURCE**：基本保留真实考试或竞赛题的数学结构；
- **ADAPTED**：由明确真题核心结构改编；
- **SYNTHESIS**：融合多个可追溯题源，再结合本讲知识重新设计；
- **DESIGNED**：少量教学原创，用于补足题库覆盖不到的重要目标。

额外教学标签：

- **DIAGNOSTIC-Hx**：专门检查某种做题习惯，不改变题源类型。

---

# 3. 真实竞赛题源

## C1｜CEMC 2023 Gauss Grade 7, Question 4

主题：负温度、跨越 0 比较温差。

官方页面：
https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023Gauss7Contest.html

用途：负数是真实量、跨越 0 的变化。

## C2｜CEMC 2017 Gauss Grade 7, Question 17

主题：平均数约束与未知数据。

官方页面：
https://cemc.uwaterloo.ca/sites/default/files/documents/2017/2017Gauss7Contest.html

用途：平均数—偏差—未知量结构。

## C3｜CEMC 2016 Gauss Grade 7, Question 18

主题：平均数与整体总量变化。

官方 PDF：
https://cemc.uwaterloo.ca/sites/default/files/documents/2016/2016Gauss7Contest.pdf

用途：Final Challenge 中“整体变化”结构依据。

## C4｜CEMC 2019 Gauss Grade 7, Question 10

主题：数据组与平均数关系。

官方页面：
https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019Gauss7Contest.html

用途：把平均数理解为平衡基准。

## A1｜2023 MAA AMC 8, Problem 3

主题：真实环境中的风寒模型：

$$
W=T-0.7v
$$

官方样题：
https://maa.org/resource/sample-competition-2023-amc-8/

官方题目 PDF：
https://maa.org/wp-content/uploads/2024/08/2023-Problems-AMC8-PDF.pdf

本讲不是全文复制原题，而是保留公式模型并改用：

$$
T=5,\qquad v=20
$$

得到负值 $W=-9$，用于训练：

> **真实模型的计算结果为负数时，如何解释其数学和现实意义。**

标记：`ADAPTED · 2023 AMC 8 Q3`。

---

# 4. Po-Shen Loh（罗博深）参考说明

官方 Daily Challenge：
https://daily.poshenloh.com/courses/0-introduction

课程借鉴的是教学方法：

- 陌生问题先独立思考；
- 通过 hints 逐步推进；
- 少量高价值问题优于大量重复；
- 即使已解出也比较不同方法；
- 鼓励自己创造解法；
- 解后继续推广到更一般的结构。

**这不是题源标签。**除非某题确实来自其公开材料，否则不得标记成“罗博深题”。

---

# 5. 主课内容审计

| 内容 | 类型 | 依据 / 目的 |
|---|---|---|
| 温度导入 | ADAPTED · C1 + TEXTBOOK-MODEL | 教材现实入口 + Gauss 负温度结构 |
| 账户、电梯、海拔 | TEXTBOOK-MODEL · P1/P2 | 相反意义与基准两侧 |
| 数系扩张 | TEXTBOOK-MODEL · P1 | 解释负数为什么出现 |
| 封闭性直觉 | DESIGNED · EXTENSION | 为后续数集/运算建立世界观，不要求记忆 |
| 0 的意义 | TEXTBOOK-MODEL | 概念边界与反例 |
| 相反意义的量 | TEXTBOOK-MODEL | Core 概念辨析 |
| 标准值—实际值—偏差 | TEXTBOOK-MODEL · P1 | 与加工允许误差同类 |
| 基准改变 | DESIGNED | 教材常给固定基准，本课程进一步研究“主动换基准” |
| 平均数与缺失偏差 | ADAPTED · C2/C4 | 平均数约束真题结构 |
| AMC 风寒模型 | ADAPTED · A1 | 真实应用、负值解释 |
| 基准法 | DESIGNED | 建立长期“基准+偏差”方法线 |
| 平均数与偏差 Olympiad | ADAPTED · C2/C3 | 平衡与整体思维 |
| delta / offset / signed | DESIGNED | 数学到程序语义的最小桥接 |

---

# 6. 当堂训练审计

## Core 1–6

- Q1、Q2、Q3、Q5、Q6：`TEXTBOOK-MODEL · P1/P2`；
- Q4：`ADAPTED · C1`，负温度跨越 0。

## Advanced 7–11

- Q7：`TEXTBOOK-MODEL · P1`，标准/偏差；
- Q8、Q9：`TEXTBOOK-MODEL + 拓展`，同一实际值换基准；
- Q10：`ADAPTED · C2`，平均数约束；
- Q11：`DESIGNED`，基准法方法检测。

## Olympiad 12–15

- Q12：`ADAPTED · C4`；
- Q13：`ADAPTED · C2/C3`；
- Q14、Q15：`DESIGNED`，用于本课程特有的基准平移和基准法迁移。

## Informatics 16–18

均为 `DESIGNED`。这些不是模拟编程竞赛题，而是建立“基准—差值—坐标”与程序变量的语义映射。

---

# 7. Final Challenge 审计

Final Challenge 标记：

> **SYNTHESIS · C2/C3 + 本讲基准改变模型**

它不是某届竞赛原题。

结构来源：

- C2：平均数与未知量约束；
- C3：整体总量变化；
- 本讲：统一改变基准时，每一个偏差同步平移。

## 知识边界检查

可主要使用本讲已建立的：

- 偏差；
- 平均数；
- 整体求和；
- 一元一次关系的直观建模。

不依赖后续高阶公式。

## 六项质量检查

- [x] 当前知识可解
- [x] 题面不直接给方法
- [x] 真正突破口是“每个偏差同步变化”
- [x] 有明确真实竞赛结构依据
- [x] 答案采用 Hint 1 → Hint 2 → Hint 3
- [x] 主课包含“解后再思考”和字母一般化

因此适合作为本讲最终思维挑战。

---

# 8. 做题习惯诊断依据

Lesson 1 另设：

[第1讲做题习惯诊断与纠偏](../diagnostics/01-positive-negative-numbers-habits.md)

重点检查：

- H1：没有先读正负约定；
- H2：没有确认求实际值还是偏差；
- H6：符号逻辑不一致；
- H7：把偏差/记录与实际对象混淆；
- H9：看到平均数后过早套模板；
- H10：结果没有回到现实语义核对。

这些检查点来自此前真实解题中暴露的长期习惯问题，而不是只针对本讲临时设置。

---

# 9. 原创题为什么仍然保留

真正保留的 `DESIGNED` 主要用于：

- 主动改变基准；
- 基准整体平移；
- 基准法；
- 信息学中的 `delta / offset / signed integer`；
- 错误路径和习惯诊断。

这些内容对课程长期能力线很重要，但教材和单一竞赛真题未必能精确覆盖。

原则仍然是：

> **教材能覆盖先用教材模型；真题能覆盖优先真题；需要组合时做 SYNTHESIS；只有存在教学空白时才原创。**
