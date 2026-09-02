# 课程统一编写与质量审核标准｜v2.0 工作版

> 当前规范以 `docs/standards/CURRENT.md` 为最高版本入口。

课程目标：

$$
\boxed{\text{概念完全理解}\rightarrow\text{规范解决问题}\rightarrow\text{真实应用}\rightarrow\text{陌生迁移}\rightarrow\text{独立发现}\rightarrow\text{持续提高独立发现上限}}
$$

> **课标是底线和知识边界，不是课程深度上限。**

---

# 一、先判断 Mainline 还是 Extension

任何新主题在写成正式编号 Lesson 前，先做定位：

1. 是否属于当前课标/人教版正式知识节点；
2. 后续主线是否直接依赖；
3. 现在单独学习是否优于以后需要时调用；
4. 是否会打断更强的教材/认知依赖链。

正式 Mainline 优先服从：

$$
\boxed{\text{课标要求}+\text{人教版顺序}+\text{知识依赖}+\text{认知连续性}}
$$

主要属于竞赛方法、抽象语言或信息学桥接的专题优先进入 `extensions/`。

---

# 二、Mainline 必须完成教材映射

七上 Mainline 写课前读取：

`docs/textbook-mapping-grade-07-semester-1.md`

每讲必须明确当前人教版章/知识群、知识节点、映射类型、Core 边界以及前后依赖。不能猜测官方未公开的新版细小节编号。

---

# 三、Extension 触发机制

后续 Lesson 第一次明显依赖某个扩展专题时，必须显式提示并标记：

- `OPTIONAL`
- `RECOMMENDED`
- `REQUIRED-FOR-EXTENSION`

未提示 Extension 不得成为 Core、Ceiling Diagnostic、Ceiling Builder 或 Final Challenge 的隐藏前置。

---

# 四、六层深度体系｜v2.0

每个 Mainline Lesson 必须覆盖：

## L1 教材完整层

定义、性质、表示、正例、反例、边界、规范表达、典型应用完整覆盖。

## L2 概念深度层

回答为什么需要、与相近概念区别、多表示关系、条件变化、特殊值/边界值、反例和解释。

## L3 校内高阶层

逆向、条件隐藏、参数、分类讨论、数形结合、综合应用、校内高档/压轴结构。

## L4 竞赛/信息学迁移层

在当前知识可解前提下，从 AMC、CEMC、UKMT、国内正式赛事以及选择性 AIME/IMO/CMO 等权威结构中训练陌生迁移；信息学连接到程序和算法模型。

## L5 Ceiling Diagnostic｜测当前上限

Core 完成后、Advanced/Olympiad 方法完整教学前安排至少一道冷启动上限诊断题。

## L6 Ceiling Builder｜提高上限

针对 L5 暴露的真实卡点，设计至少一组能够改变解题行为的训练，不靠后续知识和模板堆量。

可选择：

- 表示转换；
- 条件变化；
- 反例构造；
- 逆向/构造；
- 多方法比较；
- 特殊到一般；
- 陌生表面迁移。

---

# 五、Ceiling Diagnostic｜能力上限诊断

第一次尝试必须：

- 独立 10～20 分钟；
- 不看 Hint；
- 不先做高度同构例题；
- 当前及此前知识足够；
- 至少有一个真实突破口。

之后按顺序开放：Hint 1 → Hint 2 → Hint 3 → Full Solution。

结果记录：

| 等级 | 含义 |
|---|---|
| C5-A | 独立完成，并能解释/一般化 |
| C5-B | 独立找到核心结构，有次要错误 |
| C5-C | Hint 1 后完成 |
| C5-D | Hint 2 后完成 |
| C5-E | Hint 3 后完成 |
| C5-F | 看完整解答后才能理解 |

同时记录首个卡点、H1～H10、变式表现和7天后迁移。

---

# 六、Ceiling Builder｜能力上限提升

Ceiling Builder 必须明确回答：

> **本讲希望提高学生哪一种“面对陌生问题时的独立能力”？**

不能只写“多做几道难题”。

推荐模块：

## 6.1 表示转换

同一问题在数字、数轴/图形、表格、语言关系、程序变量之间切换，训练主动选择表示。

## 6.2 条件变化与反例

问：

- 去掉一个条件还成立吗？
- 哪个条件必要？
- 能否构造最小反例？

训练不擅自补条件和验证结论。

## 6.3 逆向与构造

从结果倒推条件，或要求自己构造满足条件/不满足条件的例子。

## 6.4 多方法与方法选择

有自然多解时，不以展示技巧为目的，而比较方法背后的共同结构及适用条件。

## 6.5 特殊到一般

从具体数字逐步推广到变量和一般条件，形成：

```text
题目 → 方法 → 一般结构
```

## 6.6 陌生表面迁移

把同一数学结构迁移到不同真实情境、竞赛题或 Informatics 模型中，训练“识别结构而不是识别题型外观”。

---

# 七、三种 Challenge 必须分开

## Ceiling Diagnostic

测：方法没教时，学生能独立走多远。

## Ceiling Builder

练：怎样让学生以后独立走得更远。

## Mastery / Final Challenge

测：经过教学和训练以后，能否在新问题中稳定迁移和一般化。

高度同构的同一道结构不能同时冒充三种功能。

---

# 八、能力提升必须有 T0 / T1 / T2

建议每讲记录：

- **T0**：Ceiling Diagnostic 冷启动；
- **T1**：Ceiling Builder 和高阶教学后的新题迁移；
- **T2**：约7天后不同表面结构的延迟迁移。

至少观察：

- 是否独立识别关键结构；
- Hint 等级是否下降；
- 首个卡点是否改变；
- 是否能解释；
- 是否能一般化；
- 是否能主动构造反例；
- H1～H10 同类错误是否减少。

“上限提高”不能只用一次最终正确率判断。

---

# 九、应用与概念深度

应用不能只换故事背景。应尽量覆盖状态、位置/方向、变化量、偏差/误差、比例/测量、数据、科学/工程、金融/生活、程序/算法等不同语义。

核心概念至少要求：为什么、定义、正反例、边界、相近概念、多表示、解释、陌生迁移。

---

# 十、例题体系

建议形成：

```text
直接应用
→ 逆向读取
→ 概念辨析
→ Ceiling Diagnostic
→ Ceiling Builder
→ 条件变化
→ 方法比较/一般化
→ Advanced/Olympiad/Informatics
→ Mastery Challenge
→ 延迟迁移
```

Ceiling Diagnostic 必须在相关高阶方法完整教学前完成；Ceiling Builder 则在诊断后针对卡点训练。

---

# 十一、权威题源

课程依据和真题认证必须回到一手来源：

- 教育部、人教社；
- 正式考试原卷/教育主管部门/考试机构；
- MAA AMC、IMO 官方站、CEMC、UKMT；
- 中国数学会 CMO、全国高中数学联赛等正式赛事；
- CSP-J/NOI 等官方信息学来源；
- 可靠正式出版物。

新闻、自媒体、商业题库转载、论坛和搜索摘要不得作为课程依据。

题源标签：`TEXTBOOK-MODEL / SOURCE / ADAPTED / SYNTHESIS / DESIGNED`。

赛事选择不按名气，而按：

```text
教学匹配度
+ 权威性
+ 当前可解性
+ 结构新颖度
+ 诊断区分度
+ 训练增益价值
+ 一般化价值
```

每讲 provenance 必须记录：

1. 实际采用来源；
2. AMC / IMO / CMO / CEMC / UKMT / 国内正式考试等候选池审查；
3. Ceiling Diagnostic 的来源和诊断区分度；
4. Ceiling Builder 的来源/设计依据和训练目标；
5. Mastery/Final Challenge 与前述任务的结构差异。

---

# 十二、做题习惯

统一流程：

$$
\boxed{\text{提取条件}\rightarrow\text{明确所求}\rightarrow\text{建立关系}\rightarrow\text{执行检查}\rightarrow\text{回代核对}}
$$

每讲明确 H1～H10 重点纠偏；Ceiling Diagnostic 和 Ceiling Builder 都记录习惯错误，不能只记录答案对错。

Ceiling Builder 应优先针对真实 H 错误：

- H1/H3 → 条件变化、反例；
- H5 → 分类筛选；
- H7 → 多表示、整体关系；
- H8/H10 → 界限、回代、唯一性；
- H9 → 陌生表面和方法选择。

---

# 十三、Markdown / LaTeX

- 标题中禁止 `$...$`；
- 简单数值/单位用普通文本：`−5`、`0 ℃`、`3 cm`、`20%`；
- 简单变量/符号表达用普通文本：`a`、`−a`、`a > 0`；
- LaTeX 留给真正需要数学结构的分数、根式、复合公式、方程等；
- 完整数学答案不放 `<details>`；
- 发布前运行 `tools/lint_markdown_rendering.py`，并要求 GitHub Actions 通过。

---

# 十四、文档结构

Mainline：

```text
module/
├── XX-lesson.md
├── exercises/XX-lesson-homework.md
├── solutions/XX-lesson-classroom.md
├── solutions/XX-lesson-homework.md
├── sources/XX-lesson-provenance.md
├── reviews/XX-lesson-release-review-vX.Y.md
└── diagnostics/
```

当堂训练留主课；答案和课后题分离。

---

# 十五、强制 Release Review

新 Lesson 首次发布、重大修改或迁移新标准时，必须 Review：

- R0 主线定位；
- R0.5 教材映射；
- R1 课程逻辑；
- R2 课标/教材完整覆盖；
- R3 概念深度；
- **R3.5 最高深度与能力上限诊断**；
- **R3.6 能力上限提升设计**；
- R4 知识边界；
- R5 应用场景；
- R6 例题/训练梯度；
- R7 题源质量与候选池审查；
- R8 错误/习惯；
- R9 Mastery/Final Challenge；
- R10 前后衔接；
- R11 Markdown / LaTeX。

结论：`PASS / PASS WITH MINOR FIXES / REVISE / BLOCK`。

R3.5 不通过时不能标记“最高深度覆盖完成”；R3.6 不通过时不能标记“能力上限提升体系完成”。

---

# 十六、发布前硬检查

- [ ] 当前标准和教材映射已读取；
- [ ] Core 不是只满足最低要求，而是完整覆盖当前知识节点；
- [ ] L1～L6 六层均有证据；
- [ ] Ceiling Diagnostic 在高阶方法讲解前完成；
- [ ] 上限题当前知识可解且不是同模板换皮；
- [ ] Ceiling Builder 针对真实卡点而不是增加机械题量；
- [ ] Builder 至少使用一种：表示转换 / 条件变化 / 逆向构造 / 多方法 / 一般化 / 陌生迁移；
- [ ] Diagnostic / Builder / Mastery 三者功能区分清楚；
- [ ] 有 T0 / T1 / T2 观察设计；
- [ ] 权威题源和候选池审查透明；
- [ ] H 标签明确；
- [ ] 无隐藏 Extension 前置；
- [ ] Markdown 自动检查通过；
- [ ] R0、R0.5、R1～R3、R3.5、R3.6、R4～R11 全部完成。
