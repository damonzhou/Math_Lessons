# Math Lessons

面向初中数学（七至九年级）的系统自学、进阶、奥数与信息学数学课程仓库。

课程以**义务教育数学课程标准 + 人教版教材**为主线，但不把教材目录当作能力上限。每一讲都形成完整学习闭环：从真实问题和概念来源开始，经过定义、反例、例题链、数学思想、分层训练，再延伸到奥数、信息学和真实应用。

课程同时关注两件事：

1. **知识是否真正理解**；
2. **做题流程和思维习惯是否健康**。

---

## 快速导航

- [课程统一编写与质量审核标准](./docs/course-authoring-standard.md)
- [课程设计原则](./docs/course-design.md)
- [题源与原创命题规范](./docs/problem-source-policy.md)
- [学习诊断与做题习惯纠偏体系](./docs/student-learning-diagnostics.md)
- [统一课程模板](./templates/lesson-template.md)
- [七年级课程](./grade-07/README.md)
  - [七年级上册 · 36讲路线图](./grade-07/semester-1/README.md)
  - [第1讲：从“3−5”到负数——数系为什么必须继续扩展](./grade-07/semester-1/01-number-system/01-positive-negative-numbers.md)
  - [第1讲题源审计](./grade-07/semester-1/01-number-system/sources/01-positive-negative-numbers-provenance.md)
  - [第1讲做题习惯诊断](./grade-07/semester-1/01-number-system/diagnostics/01-positive-negative-numbers-habits.md)
  - [七年级下册](./grade-07/semester-2/README.md)
- [八年级课程](./grade-08/README.md)
- [九年级课程](./grade-09/README.md)

---

## 课程总目标

课程希望建立：

$$
\text{课标/教材主线}
\longrightarrow
\text{概念完全理解}
\longrightarrow
\text{校内拔高}
\longrightarrow
\text{奥数/竞赛思维}
\longrightarrow
\text{真实应用与信息学迁移}
$$

最终目标不是“见过多少题型”，而是：

$$
\boxed{\text{会认}\rightarrow\text{会用}\rightarrow\text{会解释}\rightarrow\text{会迁移}}
$$

---

## 四轨课程体系

### Core｜课内主线

课标与人教版决定知识顺序和 Core 边界。要求定义、性质、基本技能、教材典型题和规范表达无漏洞。

### Advanced｜校内拔高

训练易错辨析、逆向、条件变化、分类讨论、整体、数形结合、参数意识和校内综合题。

### Olympiad｜奥数 / 竞赛思维

重点参考 **AMC 8、CEMC Gauss、UKMT JMC/JMO** 等真实竞赛题源。AMC 10 只选择不依赖明显超前知识的高质量题。

问题设计参考 Po-Shen Loh（罗博深）的思路：少量高价值陌生问题、独立探索、逐级提示、多方法和解后推广。

### Informatics｜信息学数学

把当前数学概念连接到程序和算法，例如 signed / unsigned、坐标与 offset、进制、模运算、gcd/lcm、递推、组合计数、图论和算法证明。

---

## 题源原则

所有重要题目尽量标记为：

- `TEXTBOOK-MODEL`
- `SOURCE`
- `ADAPTED`
- `SYNTHESIS`
- `DESIGNED`

教材和真题能覆盖时优先使用；原创只补现有题库无法精确覆盖的重要概念、方法、错误诊断和迁移目标。

每讲都维护独立 `sources/*-provenance.md`，记录教材/赛事、年份、题号、官方链接和改编理由。

---

## 每讲必须有 Final Challenge

每讲最后至少一道奥赛/高水平竞赛思维挑战，要求：

1. 主要依靠本讲及此前知识可解；
2. 题面不直接泄露方法；
3. 存在真正的观察、转化、整体、分类或构造突破口；
4. 优先有真实竞赛题源或明确结构依据；
5. 有 Hint 1 → Hint 2 → Hint 3；
6. 解后继续一般化、改变条件或比较方法。

目标是：

$$
\text{一道题}\rightarrow\text{一种方法}\rightarrow\text{一类结构}
$$

---

## 做题习惯也是课程内容

课程采用统一五步流程：

$$
\boxed{\text{提取条件}\rightarrow\text{明确所求}\rightarrow\text{建立关系}\rightarrow\text{执行检查}\rightarrow\text{回代核对}}
$$

长期跟踪 H1～H10 做题习惯标签，例如：条件误读、未确认所求、擅自补图形条件、先套公式后分析、分类不完整、符号检查不足、局部整体混淆、估算不验证、陌生题过早套模板、结果不回代。

每4～6讲复盘错误模式，而不是只看正确率。

---

## 单课文档结构

```text
module/
├── XX-lesson.md                  # 主课 + 当堂训练 + Final Challenge
├── exercises/
│   └── XX-lesson-homework.md
├── solutions/
│   ├── XX-lesson-classroom.md
│   └── XX-lesson-homework.md
├── sources/
│   └── XX-lesson-provenance.md
└── diagnostics/                  # 需要时增加专项习惯诊断
```

当堂训练题保留在主课；当堂答案、课后练习、课后答案分开，避免频繁切文档和提前看到答案。

---

## 数学公式

仓库保留 LaTeX，并以 GitHub Web 渲染为准：

- 行内：`$...$`
- 块级：`$$...$$`

不为了 GitHub Mobile 的公式渲染限制而降低后续奥数、代数、几何和信息学数学的表达能力。

---

## 当前进度

正在建设：**七年级上册（人教版）完整自学进阶课程**。

当前已完成：

- 七上36讲路线图；
- Lesson 1 完整重构；
- AMC / Gauss 等真实题源与题源审计机制；
- Po-Shen Loh 式问题设计原则；
- 每讲 Final Challenge 规范；
- Core / Advanced / Olympiad / Informatics 四轨体系；
- C/H 双重错因与做题习惯诊断机制；
- 七至九年级可扩展目录结构。

下一阶段：

> 有理数分类 → 数轴 → 相反数 → 绝对值 → 有理数运算

并持续训练：

> 分类讨论 → 数形结合 → 条件意识 → 整体思想 → 整数性质 → 奇偶与整除 → 模运算与信息学连接。
