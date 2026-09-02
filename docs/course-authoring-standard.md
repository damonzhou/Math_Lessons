# 课程统一编写与质量审核标准｜v1.9 工作版

> 当前规范以 `docs/standards/CURRENT.md` 为最高版本入口。

课程目标：

$$
\boxed{\text{概念完全理解}\rightarrow\text{规范解决问题}\rightarrow\text{真实应用}\rightarrow\text{陌生问题迁移}\rightarrow\text{独立发现结构}}
$$

> **课标是底线和边界，不是课程深度上限。**

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

未提示 Extension 不得成为 Core、Ceiling Diagnostic 或 Final Challenge 的隐藏前置。

---

# 四、五层深度体系｜v1.9

每个 Mainline Lesson 必须覆盖：

## L1 教材完整层

定义、性质、表示、正例、反例、边界、规范表达、典型应用完整覆盖。

## L2 概念深度层

回答为什么需要、与相近概念区别、多表示关系、条件变化、特殊值/边界值、反例和解释。

## L3 校内高阶层

逆向、条件隐藏、参数、分类讨论、数形结合、综合应用、校内高档/压轴结构。

## L4 竞赛/信息学迁移层

在当前知识可解前提下，从 AMC、CEMC、UKMT、国内正式赛事以及选择性 AIME/IMO/CMO 等权威结构中训练陌生迁移；信息学连接到程序和算法模型。

## L5 Ceiling Diagnostic

Core 完成后、Advanced/Olympiad 方法完整教学前安排至少一道冷启动上限诊断题。

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

# 六、Mastery Challenge 与 Ceiling Diagnostic 分开

- **Ceiling Diagnostic**：方法尚未直接教学时，测学生能否独立发现结构；
- **Mastery / Final Challenge**：方法教学后，测是否真正掌握并能迁移。

如果 Final Challenge 的核心方法前文已经完整教过，它不能同时作为唯一上限诊断。

---

# 七、应用与概念深度

应用不能只换故事背景。应尽量覆盖状态、位置/方向、变化量、偏差/误差、比例/测量、数据、科学/工程、金融/生活、程序/算法等不同语义。

核心概念至少要求：为什么、定义、正反例、边界、相近概念、多表示、解释、陌生迁移。

---

# 八、例题体系

建议形成：

```text
直接应用
→ 逆向读取
→ 概念辨析
→ 条件变化
→ 综合应用
→ 方法发现
→ 真实应用
→ 陌生迁移
```

但 Ceiling Diagnostic 必须在相关高阶方法被完整教学前完成，避免“教完模板再测上限”。

---

# 九、权威题源

课程依据和真题认证必须回到一手来源：

- 教育部、人教社；
- 正式考试原卷/教育主管部门/考试机构；
- MAA AMC、IMO 官方站、CEMC、UKMT；
- 中国数学会 CMO、全国高中数学联赛等正式赛事；
- CSP-J/NOI 等官方信息学来源；
- 可靠正式出版物。

新闻、自媒体、商业题库转载、论坛和搜索摘要不得作为课程依据。

题源标签：`TEXTBOOK-MODEL / SOURCE / ADAPTED / SYNTHESIS / DESIGNED`。

赛事选择按：

$$
\text{当前可解性}+\text{结构新颖度}+\text{诊断区分度}+\text{权威性}+\text{一般化价值}
$$

不是赛事名气。

每讲 provenance 必须记录：

1. 实际采用来源；
2. AMC / IMO / CMO / CEMC / UKMT / 国内正式考试等候选池审查；
3. Ceiling Diagnostic 的来源和诊断区分度。

---

# 十、做题习惯

统一流程：

$$
\boxed{\text{提取条件}\rightarrow\text{明确所求}\rightarrow\text{建立关系}\rightarrow\text{执行检查}\rightarrow\text{回代核对}}
$$

每讲明确 H1～H10 重点纠偏；Ceiling Diagnostic 同样记录习惯错误，不能只记录答案对错。

---

# 十一、Markdown / LaTeX

- 标题中禁止 `$...$`；
- 简单数值/单位用普通文本：`−5`、`0 ℃`、`3 cm`、`20%`；
- 简单变量/符号表达用普通文本：`a`、`−a`、`a > 0`；
- LaTeX 留给真正需要数学结构的分数、根式、复合公式、方程等；
- 完整数学答案不放 `<details>`；
- 发布前运行 `tools/lint_markdown_rendering.py`，并要求 GitHub Actions 通过。

---

# 十二、文档结构

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

# 十三、强制 Release Review

新 Lesson 首次发布、重大修改或迁移新标准时，必须 Review：

- R0 主线定位；
- R0.5 教材映射；
- R1 课程逻辑；
- R2 课标/教材完整覆盖；
- R3 概念深度；
- **R3.5 最高深度与能力上限诊断**；
- R4 知识边界；
- R5 应用场景；
- R6 例题/训练梯度；
- R7 题源质量与候选池审查；
- R8 错误/习惯；
- R9 Mastery/Final Challenge；
- R10 前后衔接；
- R11 Markdown / LaTeX。

结论：`PASS / PASS WITH MINOR FIXES / REVISE / BLOCK`。

R3.5 不通过时，课程可以作为教学稿使用，但不得标记为“最高深度覆盖完成”。

---

# 十四、发布前硬检查

- [ ] 当前标准和教材映射已读取；
- [ ] Core 不是只满足最低要求，而是完整覆盖当前知识节点；
- [ ] L1～L5 五层均有证据；
- [ ] Ceiling Diagnostic 在高阶方法讲解前完成；
- [ ] 上限题当前知识可解且不是同模板换皮；
- [ ] C5-A～F 记录规则存在；
- [ ] 有7天后的延迟迁移检查；
- [ ] 权威题源和候选池审查透明；
- [ ] Final Challenge 与 Ceiling Diagnostic 定位不混淆；
- [ ] H 标签明确；
- [ ] 无隐藏 Extension 前置；
- [ ] Markdown 自动检查通过；
- [ ] R0、R0.5、R1～R3、R3.5、R4～R11 全部完成。
