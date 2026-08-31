# Math Lessons

面向初中数学（七至九年级）的系统自学、进阶、奥数与信息学数学课程仓库。

> **课程标准入口**：开始任何 Lesson 编写、修改或扩展前，先读取 [COURSE_STANDARD.md](./COURSE_STANDARD.md)。  
> 当前生效版本由 [docs/standards/CURRENT.md](./docs/standards/CURRENT.md) 唯一指定。不得仅依赖聊天记录或会话记忆决定课程标准。

课程以**义务教育数学课程标准 + 人教版教材**为主线，但不把教材目录当作能力上限。每一讲都形成完整学习闭环：从真实问题和概念来源开始，经过定义、反例、例题链、数学思想、分层训练，再延伸到奥数、信息学和真实应用。

课程同时关注两件事：

1. **知识是否真正理解**；
2. **做题流程和思维习惯是否健康**。

---

## 快速导航

- [当前课程标准](./docs/standards/CURRENT.md)
- [课程标准版本库](./docs/standards/README.md)
- [课程统一编写与质量审核标准](./docs/course-authoring-standard.md)
- [课程设计原则](./docs/course-design.md)
- [题源与原创命题规范](./docs/problem-source-policy.md)
- [学习诊断与做题习惯纠偏体系](./docs/student-learning-diagnostics.md)
- [统一课程模板](./templates/lesson-template.md)
- [七年级课程](./grade-07/README.md)
  - [七年级上册 · 36讲路线图](./grade-07/semester-1/README.md)
  - [第1讲：从“3−5”到负数——数系为什么必须继续扩展](./grade-07/semester-1/01-number-system/01-positive-negative-numbers.md)
  - [第2讲：有理数的分类——同一个数为什么可以属于多个集合？](./grade-07/semester-1/01-number-system/02-rational-number-classification.md)
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

训练易错辨析、逆向、条件变化、分类讨论、整体、数形结合、参数意识和校内综合题，并优先吸收可追溯的校内、区市级和中考历年真题模型。

### Olympiad｜奥数 / 竞赛思维

题源采用**国内外并行**：国内权威数学竞赛 / 奥赛 / 数学邀请赛历年真题，以及 AMC 8、CEMC Gauss、UKMT JMC/JMO 等国际竞赛题源；AMC 10 只选择不依赖明显超前知识的高质量题。

不机械规定国内或国外优先。以**教学目标匹配度、题源可靠性、当前知识可解性**决定。

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

可追溯真题包括：

- 校内期中 / 期末历年真题；
- 区级 / 市级统一考试真题；
- 各地历年中考真题；
- 国内权威数学竞赛 / 奥赛真题；
- AMC、Gauss、UKMT 等国际竞赛真题。

每讲都维护独立 `sources/*-provenance.md`，记录教材 / 赛事 / 考试、年份、地区 / 组别、题号、可靠来源和改编理由。来源不明的“网传真题”不得直接标记为 `SOURCE`。

---

## 每讲必须有 Final Challenge

每讲最后至少一道奥赛/高水平竞赛思维挑战，要求：

1. 主要依靠本讲及此前知识可解；
2. 题面不直接泄露方法；
3. 存在真正的观察、转化、整体、分类或构造突破口；
4. 优先有国内权威竞赛、历年考试压轴题或国际竞赛等可追溯题源 / 明确结构依据；
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
├── XX-lesson.md
├── exercises/
│   └── XX-lesson-homework.md
├── solutions/
│   ├── XX-lesson-classroom.md
│   └── XX-lesson-homework.md
├── sources/
│   └── XX-lesson-provenance.md
└── diagnostics/
```

当堂训练题保留在主课；当堂答案、课后练习、课后答案分开。

---

## 数学公式

仓库保留 LaTeX，并以 GitHub Web 渲染为准：

- 行内：`$...$`
- 块级：`$$...$$`

复杂数学表达继续使用 LaTeX；标题中的简单整数等若遇到 GitHub 行内公式显示异常，可以使用普通文本符号，例如 `−5`。

---

## 当前进度

正在建设：**七年级上册（人教版）完整自学进阶课程**。

当前已完成：

- 七上36讲路线图；
- Lesson 1：正数、负数、参照标准与偏差；
- Lesson 2：有理数分类、等价表示、分类标准、奇偶/余数分类与程序分支迁移；
- 国内外真实题源与题源审计机制；
- Po-Shen Loh 式问题设计原则；
- 每讲 Final Challenge 规范；
- Core / Advanced / Olympiad / Informatics 四轨体系；
- C/H 双重错因与做题习惯诊断机制；
- **课程标准 v1.1 版本化归档与防漂移入口**；
- 七至九年级可扩展目录结构。

下一阶段：

> 集合/包含进一步整理 → 数轴 → 相反数 → 绝对值 → 有理数运算

并持续训练：

> 分类讨论 → 数形结合 → 条件意识 → 整体思想 → 整数性质 → 奇偶与整除 → 模运算与信息学连接。
