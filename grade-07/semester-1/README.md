# 七年级上册 · 自学进阶课程

目标：以当前人教版七年级上册与《义务教育数学课程标准（2022年版）》为主线，完成：

$$
\text{课内掌握}\rightarrow\text{概念理解}\rightarrow\text{校内拔高}\rightarrow\text{奥赛思维}\rightarrow\text{信息学迁移}\rightarrow\text{独立发现}\rightarrow\text{持续提高能力上限}
$$

所有课程编写先读取：

- [当前课程标准](../../docs/standards/CURRENT.md)
- [课程标准总入口](../../COURSE_STANDARD.md)
- [36讲 ↔ 当前人教版教材映射](../../docs/textbook-mapping-grade-07-semester-1.md)
- [课程统一编写与质量审核标准](../../docs/course-authoring-standard.md)

当前规范：**v1.3～v1.9 + v2.0**。

核心要求：

- R0：Mainline / Extension 定位；
- R0.5：教材映射；
- R3.5：Ceiling Diagnostic 测当前独立上限；
- R3.6：Ceiling Builder 针对真实卡点提升上限；
- T0 → T1 → T2：检查提升是否能迁移并保持；
- R11：Markdown / LaTeX 自动检查。

建议节奏：每周2讲新课 + 1次复盘/测试，自学进度领先学校约1～2周即可，不机械追求超前速度。

---

# 七上 36 讲正式主线

## 模块一｜有理数

1. **正数和负数：为什么数学需要扩展数系**
2. **有理数的意义与分类：写法、对象与身份**
3. **数轴：怎样把“数”变成直线上的位置**
4. **相反数：数轴上的对称位置**
5. **绝对值（一）：距离的定义与几何意义**
6. **绝对值（二）：含字母、分类讨论与边界理解**
7. **有理数大小比较：数轴、绝对值与多种表示的统一**
8. **数轴综合：两点位置、距离、中点、动点与距离和**

教材映射：当前人教版 **“有理数”** 章/知识群。

其中 Lesson 8 为 `INTEGRATED` 综合课，不对应教材独立小节。

---

## 模块二｜有理数的运算

9. **加法：方向、大小与运算结构**
10. **减法：为什么可以转化成加法**
11. **乘法与除法：符号规律的来源**
12. **乘方：底数、指数与符号陷阱**
13. **运算律与巧算：重组、凑整、分配律**
14. **有理数运算综合：混合运算、应用与结构识别**

教材映射：新版独立 **“有理数的运算”** 章。

---

## 模块三｜代数式

15. **为什么要用字母表示数：从具体到一般**
16. **代数式与数量关系：把文字变成数学表达**
17. **代数式的值：代入、公式与整体代入**
18. **整数指数幂与科学记数法：怎样压缩表示大数**
19. **代数式综合：规律、图形、公式与建模**

教材映射：新版新增 **“代数式”** 章/知识群。

> 当前人教社公开资料可确认新版新增“代数式”章，但没有完整公开七上所有细小节编号；Lesson 18 的最终细目位置在正式发布前仍需按最新官方教材细目再次核对，不凭非官方目录猜编号。

---

## 模块四｜整式及整式加减

20. **单项式、多项式与整式结构**
21. **同类项与合并：为什么有些项可以合并**
22. **去括号：符号变化的本质**
23. **整式加减：标准化简流程**
24. **整式综合：整体思想、条件求值与结构识别**

教材映射：当前人教版整式及整式加减知识群。

---

## 模块五｜一元一次方程

25. **什么是方程：从算术答案到未知数**
26. **等式性质：每一步变形为什么合法**
27. **一元一次方程基本解法**
28. **复杂方程：去括号、去分母与规范步骤**
29. **应用题：怎样寻找等量关系**
30. **方程综合：行程、利润、配套、分段与方案问题**

教材映射：当前人教版 **“一元一次方程”** 知识群。

---

## 模块六｜几何图形初步

31. **几何图形与几何语言：从物体到点、线、面、体**
32. **直线、射线、线段：表示、长度和基本事实**
33. **线段综合：比较、和差、中点、动点与分类讨论**
34. **角：表示、度量、比较、运算与角平分线**
35. **余角、补角与初步几何说理**

教材映射：当前人教版 **“几何图形初步”** 知识群。

---

## 模块七｜全册综合

36. **七上数学思想总复盘：数形结合、分类讨论、转化、整体、方程、从特殊到一般**

类型：`INTEGRATED`，不引入新的 Core 概念。

---

# 每讲统一的能力上限提升结构｜v2.0

从 Lesson 5 起，新 Lesson 原生按：

```text
Core 完整学习
→ Ceiling Diagnostic（T0）
→ 记录首个卡点 / H 标签
→ Ceiling Builder
→ Advanced / Olympiad / Informatics
→ Mastery / Final Challenge（T1）
→ 约7天后陌生迁移（T2）
```

Ceiling Builder 不以增加题量为目标，而是训练：

- 换表示；
- 判断条件是否足够；
- 构造反例；
- 逆向构造；
- 比较方法；
- 从具体推广到一般；
- 在陌生表面下识别同一数学结构。

---

# Extensions｜按需要学习，不占正式编号

## E1｜[分类是一种数学方法——集合直觉、余数与抽屉原理](./extensions/classification-as-a-method.md)

内容包括分类“不重不漏”、集合直觉、属于/包含、互斥/相交、奇偶与余数分类、周期筛选、抽屉原理、程序条件分支。

学习机制：

- 当前 Lesson 1～4 Core 不需要 E1；
- 后续第一次明显使用时，Mainline 明确提示 `OPTIONAL / RECOMMENDED / REQUIRED-FOR-EXTENSION`；
- 未提示 Extension 不得成为 Core、Ceiling Diagnostic、Ceiling Builder 或 Final Challenge 的隐藏前置。

[查看所有 Extensions](./extensions/README.md)

---

# 已完成 / 已准备

## Lesson 1

- [第1讲：从“3−5”到负数——数系为什么必须继续扩展](./01-number-system/01-positive-negative-numbers.md)

## Lesson 2

- [第2讲：有理数的分类——一个数的“写法”和“身份”为什么不是一回事？](./01-number-system/02-rational-number-classification.md)

## Lesson 3

- [第3讲：数轴——怎样把“数”变成直线上的位置](./01-number-system/03-number-line.md)
  - [当堂训练答案](./01-number-system/solutions/03-number-line-classroom.md)
  - [课后练习](./01-number-system/exercises/03-number-line-homework.md)
  - [课后练习答案](./01-number-system/solutions/03-number-line-homework.md)
  - [题源审计](./01-number-system/sources/03-number-line-provenance.md)
  - [做题习惯诊断](./01-number-system/diagnostics/03-number-line-habits.md)
  - [v1.6 Release Review](./01-number-system/reviews/03-number-line-release-review-v1.6.md)

## Lesson 4

- [第4讲：相反数——为什么数轴上的对称位置代表一对特殊的数](./01-number-system/04-opposite-numbers.md)
  - [当堂训练答案](./01-number-system/solutions/04-opposite-numbers-classroom.md)
  - [课后练习](./01-number-system/exercises/04-opposite-numbers-homework.md)
  - [课后练习答案](./01-number-system/solutions/04-opposite-numbers-homework.md)
  - [题源审计](./01-number-system/sources/04-opposite-numbers-provenance.md)
  - [做题习惯诊断](./01-number-system/diagnostics/04-opposite-numbers-habits.md)
  - [v1.8 Release Review](./01-number-system/reviews/04-opposite-numbers-release-review-v1.8.md)

## v2.0 前4课审计

- [Lesson 1～4 能力上限提升审计](../../docs/audits/lessons-01-04-ceiling-building-audit-v2.0.md)

当前状态：

> **Lesson 1～4 原教学内容 PASS；需要补独立 Ceiling Diagnostic、系统 Ceiling Builder 和 T0/T1/T2 观察后，才能按 v2.0 标记“能力上限提升体系完成”。**

---

# 后续建设原则

任何新 Mainline Lesson 发布前必须完成：

```text
R0   主线定位
→ R0.5 教材映射
→ R1～R3
→ R3.5 Ceiling Diagnostic
→ R3.6 Ceiling Builder
→ R4～R11
→ PASS
```

Lesson 5 起直接按 v2.0 建设，不再把上限诊断和上限提升作为事后补丁。
