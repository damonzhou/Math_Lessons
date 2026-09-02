# Math Lessons

面向初中数学（七至九年级）的系统自学、进阶、奥数与信息学数学课程仓库。

> **课程标准入口**：开始任何 Lesson 编写、修改或扩展前，先读取 [COURSE_STANDARD.md](./COURSE_STANDARD.md) 和 [docs/standards/CURRENT.md](./docs/standards/CURRENT.md)。不得仅依赖聊天记录或会话记忆决定课程标准。

当前规范：**v1.3～v1.9 + v2.0**。

- v1.3：权威一手来源 + 每讲 Release Review；
- v1.4：AMC / IMO / CMO 等权威奥赛题源池；
- v1.5：Mainline / Extension 分层；
- v1.6：Markdown / LaTeX 稳健性；
- v1.7：36讲 ↔ 当前人教版教材映射；
- v1.8：候选题源池审查可见性；
- v1.9：最高深度覆盖 + Ceiling Diagnostic 测能力上限；
- **v2.0：Ceiling Builder 提升能力上限 + T0/T1/T2 迁移验证。**

---

## 课程总目标

$$
\boxed{\text{会认}\rightarrow\text{会用}\rightarrow\text{会解释}\rightarrow\text{会迁移}\rightarrow\text{能独立发现}\rightarrow\text{持续提高独立发现上限}}
$$

课程不是以“达到课标最低要求”为目标。

> **课标和人教版决定知识边界、主线和不可遗漏内容；课程在当前知识可解的前提下，把概念理解、高阶迁移、独立发现和问题解决能力持续向上推进。**

---

## 快速导航

- [当前课程标准](./docs/standards/CURRENT.md)
- [课程标准版本库](./docs/standards/README.md)
- [v2.0 能力上限提升标准](./docs/standards/course-standard-v2.0.md)
- [七上36讲 ↔ 当前人教版教材映射](./docs/textbook-mapping-grade-07-semester-1.md)
- [Lesson 1～4 v1.9 上限诊断审计](./docs/audits/lessons-01-04-depth-ceiling-audit-v1.9.md)
- [Lesson 1～4 v2.0 能力上限提升审计](./docs/audits/lessons-01-04-ceiling-building-audit-v2.0.md)
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

## 六层深度体系｜v2.0

每个 Mainline Lesson 必须同时覆盖：

1. **L1 教材完整层**：定义、性质、表示、正反例、边界、规范表达、典型应用；
2. **L2 概念深度层**：为什么、相近概念、反例、多表示、条件变化、特殊值；
3. **L3 校内高阶层**：逆向、参数、隐藏条件、分类、综合、压轴结构；
4. **L4 竞赛/信息学迁移层**：权威竞赛陌生结构、一般化、算法化；
5. **L5 Ceiling Diagnostic**：高阶方法尚未直接教学时冷启动，测当前独立发现上限；
6. **L6 Ceiling Builder**：针对真实卡点训练表示转换、条件变化、反例、构造、多方法、一般化和陌生迁移，主动提高上限。

---

## 测上限、提上限、验迁移必须分开

### Ceiling Diagnostic｜测

Core 学完后、Advanced/Olympiad 方法完整讲解前先独立尝试；第一次不开放 Hint，按 C5-A～F 记录。

### Ceiling Builder｜练

根据 Diagnostic 或 H1～H10 暴露的卡点，有针对性训练：

- 换表示；
- 判断条件是否足够；
- 构造反例；
- 逆向构造；
- 比较方法；
- 从具体推广到一般；
- 在陌生表面下识别同一结构。

目的不是增加题量，而是改变学生面对陌生题时的启动方式。

### Mastery / Final Challenge｜验

经过教学和训练后，用新的问题检查是否稳定迁移、解释和一般化。

同一高度同构模板不能同时冒充三种功能。

---

## T0 / T1 / T2 能力变化

能力上限不能只测一次。

```text
T0：冷启动 Ceiling Diagnostic
↓
T1：Ceiling Builder / 高阶教学后的新题迁移
↓
T2：约7天后不同表面结构的延迟迁移
```

主要观察：

- Hint 是否减少；
- 是否更早识别关键结构；
- 是否能主动换表示；
- 是否能构造反例；
- 是否能一般化；
- 同类 H 错误是否减少。

这比单纯比较最终正确率更能说明能力是否真正提高。

---

## 四轨体系与权威题源

### Core

教育部课标和人教版决定知识顺序、概念边界和不可遗漏内容；不把最低掌握要求当作深度上限。

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

赛事不按名气排序，综合考虑：

```text
教学匹配度
+ 权威性
+ 当前可解性
+ 结构新颖度
+ 诊断区分度
+ 训练增益价值
+ 一般化价值
```

每讲 provenance 必须记录实际采用来源、候选权威题源池审查，以及 Diagnostic / Builder / Mastery 三类任务的来源和功能。

### Informatics

把数学概念连接到 signed/unsigned、offset、进制、模运算、gcd/lcm、递推、组合、图论和算法证明等。

---

## Release Review

当前必须检查：

- R0 Mainline / Extension；
- R0.5 教材映射；
- R1 课程逻辑；
- R2 课标/教材完整覆盖；
- R3 概念深度；
- **R3.5 最高深度与能力上限诊断**；
- **R3.6 能力上限提升设计**；
- R4 知识边界；
- R5 应用场景；
- R6 例题与训练梯度；
- R7 题源质量与候选池；
- R8 错误与做题习惯；
- R9 Mastery / Final Challenge；
- R10 前后衔接；
- R11 Markdown / LaTeX。

只有 R3.5 与 R3.6 都通过，才能标记：

> **最高深度 + 能力上限提升体系完成。**

---

## 当前进度

正式 Mainline Lesson 1～4 的原教学 Review 仍然有效。

v2.0 重新审计结果：

> **Lesson 1～4 教学内容 PASS；需要补独立 Ceiling Diagnostic、系统 Ceiling Builder 和 T0/T1/T2 观察，暂不标记“能力上限提升体系完成”。**

下一正式主线：Lesson 5《绝对值（一）》；从首次建设开始直接执行 v2.0。
