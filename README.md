# Math Lessons

面向初中数学（七至九年级）的系统自学、进阶、奥数与信息学数学课程仓库。

> **课程标准入口**：开始任何 Lesson 编写、修改或扩展前，先读取 [COURSE_STANDARD.md](./COURSE_STANDARD.md) 和 [docs/standards/CURRENT.md](./docs/standards/CURRENT.md)。不得仅依赖聊天记录或会话记忆决定课程标准。

当前规范：**v1.3 + v1.4 + v1.5 + v1.6 + v1.7**。

- v1.3：权威一手来源 + 每讲发布前整体 Release Review；
- v1.4：AMC / IMO / CMO 等国内外权威奥赛题源池及适龄筛选；
- v1.5：Mainline / Extension 分层、需要时提示学习、R0 主线定位审查；
- v1.6：Markdown / LaTeX 渲染稳健性、简单数值/单位文本化、R11 自动检查；
- v1.7：36讲 ↔ 当前人教版教材映射、R0.5 教材映射门禁。

---

## 课程总目标

$$
\boxed{\text{会认}\rightarrow\text{会用}\rightarrow\text{会解释}\rightarrow\text{会迁移}}
$$

主线：

$$
\text{课标/人教版}
\rightarrow
\text{概念完全理解}
\rightarrow
\text{校内拔高}
\rightarrow
\text{奥赛/竞赛思维}
\rightarrow
\text{真实应用与信息学迁移}
$$

---

## 快速导航

- [当前课程标准](./docs/standards/CURRENT.md)
- [课程标准版本库](./docs/standards/README.md)
- [七上36讲 ↔ 当前人教版教材映射](./docs/textbook-mapping-grade-07-semester-1.md)
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
  - [E1：分类是一种数学方法——集合直觉、余数与抽屉原理](./grade-07/semester-1/extensions/classification-as-a-method.md)

---

## Mainline、Extension 与教材映射

正式编号 Lesson 优先保持：

$$
\boxed{\text{课标要求}+\text{人教版顺序}+\text{知识依赖}+\text{认知连续性}}
$$

课程仍然会深入讲 Advanced / Olympiad / Informatics，但：

> **理解更深，不等于更早引入更抽象的术语。**

主要属于竞赛方法、抽象语言或信息学的专题优先保存在 `extensions/`。后续真正需要时，Mainline 会显式提示：

- `OPTIONAL`
- `RECOMMENDED`
- `REQUIRED-FOR-EXTENSION`

未提示的 Extension 不得成为 Core 或 Final Challenge 的隐藏前置。

从 v1.7 起，每个 Mainline Lesson 还必须通过 **R0.5 教材映射**：

- 对应当前人教版章/知识节点；
- 标明 `DIRECT / SPLIT / INTEGRATED / BRIDGE`；
- Core 与 Advanced/Olympiad 边界清楚；
- 人教社未公开新版细小节编号时不猜编号。

当前七上数系正式主线：

$$
\boxed{
\text{正负数}
\rightarrow
\text{有理数}
\rightarrow
\text{数轴}
\rightarrow
\text{相反数}
\rightarrow
\text{绝对值}
\rightarrow
\text{大小比较}
}
$$

---

## Markdown / LaTeX 渲染规则｜v1.6

课程主要在 GitHub Web / Mobile 阅读，优先保证稳定显示：

- 标题中禁止 `$...$`；
- 简单数值和单位使用普通文本，例如 `−5`、`0 ℃`、`3 cm`、`20%`；
- 纯数字行内 LaTeX 直接作为 lint error；
- LaTeX 只用于真正需要数学结构的分数、根式、变量、方程、不等式等；
- GitHub Actions 自动检查发生变化的 Markdown 文件；
- Release Review 包含 R11 渲染稳健性。

---

## 四轨体系

### Core

教育部课标和人教版官方教材/教师用书决定知识顺序、概念边界和最低掌握深度。

### Advanced

训练条件变化、逆向、综合、分类讨论、整体、数形结合和真实校内高档题。

### Olympiad

权威题源池包括但不限于：

- MAA：AMC 8 / AMC 10 / AMC 12、AIME、USAJMO、USAMO；
- IMO 官方历年题/公开 Shortlist；
- University of Waterloo CEMC：Gauss 等；
- UKMT：JMC / JMO 等；
- 中国数学会：CMO（中国数学奥林匹克）、全国高中数学联赛、中国女子数学奥林匹克等正式赛事；
- 其他具有明确主办方和可核验原题的国内外权威赛事。

题源不按赛事名气机械排序，而按：

$$
\boxed{\text{教学匹配度}+\text{权威性}+\text{当前可解性}+\text{思维价值}}
$$

七年级最常直接采用 AMC 8、Gauss 等适龄题；IMO/CMO 等高阶来源只选择当前知识可解的题或进行透明适龄改编。

### Informatics

把数学概念连接到程序和算法：signed/unsigned、offset、进制、模运算、gcd/lcm、递推、组合、图论和算法证明。

---

## 权威来源硬规则

课程设计与题源认证必须尽量回到一手来源：

- 教育部、人教社官方资料；
- 赛事主办方官方题目和官方解答；
- 教育主管部门/考试机构/学校正式试卷；
- 可核验正式出版物。

**新闻报道、自媒体、商业题库转载、论坛、搜索摘要不能作为课程设计事实依据或真题认证依据。**

搜索工具只用于找到一手来源。

题源标记：

- `TEXTBOOK-MODEL`
- `SOURCE`
- `ADAPTED`
- `SYNTHESIS`
- `DESIGNED`

每讲维护独立 provenance。

---

## 每讲发布前必须整体 Review

当前 Release Review 顺序：

- R0：Mainline / Extension 定位；
- R0.5：教材映射；
- R1：课程逻辑；
- R2：课标/教材覆盖；
- R3：概念理解深度；
- R4：知识边界/是否超前；
- R5：应用场景；
- R6：例题与训练梯度；
- R7：题源质量；
- R8：错误与做题习惯；
- R9：Final Challenge；
- R10：前后 Lesson 纵向衔接；
- R11：Markdown / LaTeX 渲染稳健性。

Review 结论存入 `reviews/`，达到 PASS 后才标记完成。

---

## Final Challenge

每讲至少一道高水平综合挑战：

- 当前知识可解；
- 不直接泄露方法；
- 有真正突破口；
- 优先有权威题源/明确结构依据；
- Hint 1 → Hint 2 → Hint 3；
- 解后一般化/第二解法/条件变化；
- 不依赖未提示的 Extension。

$$
\text{一道题}\rightarrow\text{一种方法}\rightarrow\text{一类结构}
$$

---

## 做题习惯

统一流程：

$$
\boxed{\text{提取条件}\rightarrow\text{明确所求}\rightarrow\text{建立关系}\rightarrow\text{执行检查}\rightarrow\text{回代核对}}
$$

长期跟踪 H1～H10，结合真实做题错误持续纠偏。

---

## 当前进度

正式 Mainline：

- **Lesson 1**：正数和负数、基准与偏差；
- **Lesson 2**：有理数的意义、分类、表示与精确/近似；
- **Lesson 3**：数轴三要素、数↔点、刻度与距离直觉；
- **Lesson 4**：相反数、原点对称、$a$ 与 $-a$、双重负号、隐藏原点结构。

扩展专题：

- **E1 分类是一种数学方法**：集合直觉、互斥/包含/相交、余数分类、周期筛选、抽屉原理、程序分支。以后按需要提示学习。

下一正式主线：

> **Lesson 5：绝对值（一）——距离的定义与几何意义。**
