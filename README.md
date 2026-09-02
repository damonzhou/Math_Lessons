# Math Lessons

面向初中数学（七至九年级）的系统自学、进阶、奥数与信息学数学课程仓库。

> **唯一标准入口**：任何 Lesson 新建、修改、复审或扩展前，先读取 [COURSE_STANDARD.md](./COURSE_STANDARD.md) 与 [docs/standards/CURRENT.md](./docs/standards/CURRENT.md)。后续课程工作一律采用 `CURRENT.md` 指定的最新标准，不以聊天记录或旧 Lesson 版本代替。

当前规范：**v1.3～v1.9 + v2.0**。

- v1.3：权威一手来源 + Release Review；
- v1.4：AMC / IMO / CMO 等权威竞赛题源池；
- v1.5：Mainline / Extension 分层；
- v1.6：Markdown / LaTeX 稳健性；
- v1.7：36讲 ↔ 当前人教版教材映射；
- v1.8：候选权威题源池审查可见性；
- v1.9：Ceiling Diagnostic 测能力上限；
- **v2.0：Ceiling Builder 提升能力上限 + T0/T1/T2 迁移验证。**

---

## 课程总目标

$$
\boxed{\text{会认}\rightarrow\text{会用}\rightarrow\text{会解释}\rightarrow\text{会迁移}\rightarrow\text{能独立发现}\rightarrow\text{持续提高独立发现上限}}
$$

课程不以“达到课标最低要求”为完成标准。

> **课标和人教版决定知识边界、主线和不可遗漏内容；课程在当前知识可解的前提下，把概念理解、高阶迁移、独立发现和问题解决能力持续向上推进。**

---

## 快速导航

- [当前课程标准](./docs/standards/CURRENT.md)
- [v2.0 能力上限提升标准](./docs/standards/course-standard-v2.0.md)
- [课程标准版本库](./docs/standards/README.md)
- [七上36讲 ↔ 当前人教版教材映射](./docs/textbook-mapping-grade-07-semester-1.md)
- [Lesson 1～4 v2.0 完成审计](./docs/audits/lessons-01-04-ceiling-building-audit-v2.0.md)
- [课程统一编写与质量审核标准](./docs/course-authoring-standard.md)
- [题源与原创命题规范](./docs/problem-source-policy.md)
- [学习诊断与做题习惯纠偏](./docs/student-learning-diagnostics.md)
- [统一 Lesson 模板](./templates/lesson-template.md)
- [七年级上册 · 36讲路线图](./grade-07/semester-1/README.md)
- [Lesson 1：正数和负数](./grade-07/semester-1/01-number-system/01-positive-negative-numbers.md)
- [Lesson 2：有理数的意义与分类](./grade-07/semester-1/01-number-system/02-rational-number-classification.md)
- [Lesson 3：数轴](./grade-07/semester-1/01-number-system/03-number-line.md)
- [Lesson 4：相反数](./grade-07/semester-1/01-number-system/04-opposite-numbers.md)
- [Extensions](./grade-07/semester-1/extensions/README.md)

---

## Mainline 与教材映射

正式编号 Lesson 优先满足：

$$
\boxed{\text{课标要求}+\text{人教版顺序}+\text{知识依赖}+\text{认知连续性}}
$$

主要属于竞赛方法、抽象语言或信息学的专题优先进入 `extensions/`；后续真正需要时由 Mainline 显式提示 `OPTIONAL / RECOMMENDED / REQUIRED-FOR-EXTENSION`。

---

## 六层深度体系｜v2.0

每个 Mainline Lesson 必须同时覆盖：

1. **L1 教材完整层**：定义、性质、表示、正反例、边界、规范表达、典型应用；
2. **L2 概念深度层**：为什么、相近概念、多表示、条件变化、特殊值和反例；
3. **L3 校内高阶层**：逆向、参数、隐藏条件、分类、综合、压轴结构；
4. **L4 竞赛/信息学迁移层**：权威竞赛陌生结构、一般化、算法化；
5. **L5 Ceiling Diagnostic**：方法尚未完整教学时冷启动，测当前独立发现上限；
6. **L6 Ceiling Builder**：针对真实卡点训练表示转换、条件变化、反例、构造、多方法、一般化和陌生迁移。

---

## 测上限、提上限、验迁移

### Ceiling Diagnostic｜测

Core 学完后、Advanced/Olympiad 方法完整教学前独立尝试；第一次不开放 Hint，按 C5-A～F 记录。

### Ceiling Builder｜提

针对 Diagnostic 和 H1～H10 暴露的真实卡点训练，不以增加题量为目的。

### Mastery / Final Challenge｜验

教学后用不同问题检查是否稳定迁移、解释和一般化。

同一高度同构模板不能同时冒充三种功能。

---

## T0 / T1 / T2

```text
T0：冷启动 Ceiling Diagnostic
↓
T1：Builder / 高阶教学后的新题迁移
↓
T2：约7天后不同表面结构的延迟迁移
```

主要观察：

- Hint 是否减少；
- 是否更早识别关键结构；
- 是否主动换表示；
- 是否会构造反例；
- 是否能一般化；
- 同类 H 错误是否减少。

---

## 权威题源

正式题源池包括：

- 教育部、人教社；
- MAA AMC 8 / 10 / 12、AIME、USAJMO、USAMO；
- IMO 官方历年题 / Shortlist；
- CEMC Gauss 等；
- UKMT JMC / JMO；
- 中国数学会 CMO、全国高中数学联赛、中国女子数学奥林匹克等；
- 国内正式考试原卷；
- CSP-J / NOI 等官方信息学题目结构。

选择标准：

```text
教学匹配度
+ 权威性
+ 当前可解性
+ 结构新颖度
+ 诊断区分度
+ 训练增益价值
+ 一般化价值
```

每讲 provenance 必须记录：实际采用来源、候选题源池审查，以及 Diagnostic / Builder / Mastery 的来源与功能。

---

## Release Review

当前完整门禁：

```text
R0 主线定位
→ R0.5 教材映射
→ R1～R3
→ R3.5 Ceiling Diagnostic
→ R3.6 Ceiling Builder
→ R4～R11
→ PASS
```

只有 R3.5 和 R3.6 都通过，才能标记：

> **最高深度 + 能力上限提升体系完成。**

---

## Markdown / LaTeX

课程主要在 GitHub Web / Mobile 阅读：

- 标题不使用 `$...$`；
- 简单数值、单位、单变量、−a 等使用普通文本；
- 复杂数学结构再使用 LaTeX；
- 所有变更通过 `tools/lint_markdown_rendering.py` 与 GitHub Actions。

---

## 当前进度

**Lesson 1～4 已全部完成 v2.0 迁移。**

每讲现在都有：

- Core / Advanced / Olympiad / Informatics；
- Ceiling Diagnostic；
- Ceiling Builder；
- C5-A～F 与 T0/T1/T2 记录；
- v2.0 provenance 补充；
- v2.0 Release Review。

四个主课更新提交的 Markdown Render Lint 均已实际 `success`。

下一正式主线：

> **Lesson 5《绝对值（一）——距离的定义与几何意义》**，从首次建设开始原生采用 v2.0。