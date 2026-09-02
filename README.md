# Math Lessons

面向初中数学（七至九年级）的系统自学、进阶、奥数与信息学数学课程仓库。

> **课程标准入口**：开始任何 Lesson 编写、修改或扩展前，先读取 [COURSE_STANDARD.md](./COURSE_STANDARD.md) 和 [docs/standards/CURRENT.md](./docs/standards/CURRENT.md)。不得仅依赖聊天记录或会话记忆决定课程标准。

当前规范：**v1.3 + v1.4 + v1.5 + v1.6 + v1.7 + v1.8 + v1.9**。

- v1.3：权威一手来源 + 每讲发布前整体 Release Review；
- v1.4：AMC / IMO / CMO 等国内外权威奥赛题源池及适龄筛选；
- v1.5：Mainline / Extension 分层、需要时提示学习、R0 主线定位审查；
- v1.6：Markdown / LaTeX 渲染稳健性、R11 自动检查；
- v1.7：36讲 ↔ 当前人教版教材映射、R0.5 教材映射门禁；
- v1.8：provenance 候选权威题源池审查可见性、简单变量/符号表达文本化；
- v1.9：**课标不再作为深度上限；五层深度覆盖 + Ceiling Diagnostic 能力上限诊断 + R3.5 门禁。**

---

## 课程总目标

$$
\boxed{\text{会认}\rightarrow\text{会用}\rightarrow\text{会解释}\rightarrow\text{会迁移}\rightarrow\text{能独立发现结构}}
$$

课程不是以“达到最低要求”为目标，而是：

> **完整覆盖当前教材节点，并在不依赖后续知识的前提下，把概念理解、校内高阶、竞赛迁移和独立发现能力推到当前知识边界内的上限。**

---

## 快速导航

- [当前课程标准](./docs/standards/CURRENT.md)
- [课程标准版本库](./docs/standards/README.md)
- [七上36讲 ↔ 当前人教版教材映射](./docs/textbook-mapping-grade-07-semester-1.md)
- [Lesson 1～4 最高深度/上限诊断审计](./docs/audits/lessons-01-04-depth-ceiling-audit-v1.9.md)
- [课程统一编写与质量审核标准](./docs/course-authoring-standard.md)
- [题源与原创命题规范](./docs/problem-source-policy.md)
- [学习诊断与做题习惯纠偏](./docs/student-learning-diagnostics.md)
- [统一课程模板](./templates/lesson-template.md)
- [Markdown 渲染检查工具](./tools/lint_markdown_rendering.py)
- [七年级上册 · 36讲路线图](./grade-07/semester-1/README.md)
- [Lesson 1：正数、负数、基准与偏差](./grade-07/semester-1/01-number-system/01-positive-negative-numbers.md)
- [Lesson 2：有理数的分类——写法与身份](./grade-07/semester-1/01-number-system/02-rational-number-classification.md)
- [Lesson 3：数轴——怎样把“数”变成直线上的位置](./grade-07/semester-1/01-number-system/03-number-line.md)
- [Lesson 4：相反数——数轴上的对称位置](./grade-07/semester-1/01-number-system/04-opposite-numbers.md)
- [Extensions](./grade-07/semester-1/extensions/README.md)

---

## Mainline、Extension 与教材映射

正式编号 Lesson 优先保持：

$$
\boxed{\text{课标要求}+\text{人教版顺序}+\text{知识依赖}+\text{认知连续性}}
$$

课标/教材决定“学什么”和顺序，但不限制课程深度。

主要属于竞赛方法、抽象语言或信息学的专题优先保存在 `extensions/`；后续真正需要时 Mainline 显式提示 `OPTIONAL / RECOMMENDED / REQUIRED-FOR-EXTENSION`。

---

## 五层深度体系｜v1.9

每个 Mainline Lesson 必须同时检查：

1. **L1 教材完整层**：定义、性质、表示、正反例、边界、规范表达、典型应用；
2. **L2 概念深度层**：为什么、相近概念、反例、多表示、条件变化、特殊值；
3. **L3 校内高阶层**：逆向、参数、隐藏条件、分类、综合、压轴结构；
4. **L4 竞赛/信息学迁移层**：权威竞赛陌生结构、一般化、算法化；
5. **L5 Ceiling Diagnostic**：高阶方法尚未直接教学时，冷启动测学生独立发现能力。

### Ceiling Diagnostic 与 Final Challenge 不再混淆

- **Ceiling Diagnostic**：Core 学完后、Advanced/Olympiad 方法完整讲解前先独立尝试；
- **Mastery / Final Challenge**：教学后检查真正掌握和迁移。

如果 Final Challenge 的方法前文已经完整教过，它不能同时冒充唯一的能力上限诊断。

上限诊断采用 C5-A～F 分级，而不是只看对错。

---

## 四轨体系

### Core

教育部课标和人教版决定知识顺序、概念边界和不可遗漏内容；**不再把最低掌握要求当成课程完成上限。**

### Advanced

训练条件变化、逆向、综合、分类讨论、整体、数形结合和真实校内高档题。

### Olympiad

权威题源池包括：

- MAA AMC 8 / 10 / 12、AIME、USAJMO、USAMO；
- IMO 官方历年题 / Shortlist；
- CEMC Gauss 等；
- UKMT JMC / JMO；
- 中国数学会 CMO、全国高中数学联赛、中国女子数学奥林匹克等；
- 其他可核验官方赛事。

题源选择按：

$$
\boxed{\text{当前可解性}+\text{结构新颖度}+\text{诊断区分度}+\text{权威性}+\text{一般化价值}}
$$

不是赛事名气。

每讲 provenance 必须同时记录：实际采用来源、候选权威题源池审查、Ceiling Diagnostic 来源与区分度。

### Informatics

把数学概念连接到 signed/unsigned、offset、进制、模运算、gcd/lcm、递推、组合、图论和算法证明等。

---

## 权威来源硬规则

课程设计与题源认证必须回到一手来源：教育部、人教社、赛事主办方官方题目/解答、正式考试原卷、可核验正式出版物。

新闻、自媒体、商业题库转载、论坛、搜索摘要不能作为课程设计事实依据或真题认证依据。

---

## Release Review

当前必须检查：

- R0 Mainline / Extension；
- R0.5 教材映射；
- R1 课程逻辑；
- R2 课标/教材完整覆盖；
- R3 概念深度；
- **R3.5 最高深度与能力上限诊断**；
- R4 知识边界；
- R5 应用场景；
- R6 例题与训练梯度；
- R7 题源质量与候选池；
- R8 错误与做题习惯；
- R9 Mastery / Final Challenge；
- R10 前后衔接；
- R11 Markdown / LaTeX。

只有 R3.5 也通过，才能标记“最高深度覆盖完成”。

---

## Markdown / LaTeX

课程主要在 GitHub Web / Mobile 阅读：标题不写 `$...$`；简单数值、单位和简单变量表达用普通文本；复杂数学结构再用 LaTeX；所有变更通过自动 lint。

---

## 当前进度

正式 Mainline：Lesson 1～4 已完成原有教学 Review。

v1.9 重新审计结果：

> **Lesson 1～4 教学内容仍 PASS；独立 Ceiling Diagnostic 层需要补齐，因此暂不标记“最高深度覆盖完成”。**

下一正式主线：Lesson 5《绝对值（一）》；从首次建设开始直接执行 v1.9。
