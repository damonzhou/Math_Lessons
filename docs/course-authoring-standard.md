# 课程统一编写与质量审核标准｜v1.7 工作版

> 当前规范以 `docs/standards/CURRENT.md` 为最高版本入口。

课程目标：

$$
\boxed{\text{概念完全理解}\rightarrow\text{规范解决问题}\rightarrow\text{真实应用}\rightarrow\text{陌生问题迁移}}
$$

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

> **理解更深，不等于更早引入更抽象的术语。**

---

# 二、Mainline 必须完成教材映射｜v1.7

七上 Mainline 写课前必须读取：

`docs/textbook-mapping-grade-07-semester-1.md`

每讲必须明确：

- 当前人教版章/知识群；
- 对应教材知识节点；
- 映射类型：`DIRECT / SPLIT / INTEGRATED / BRIDGE`；
- 为什么需要独立成讲；
- 哪些内容只是 Advanced/Olympiad/Informatics，不属于教材 Core。

若人教社官方公开资料没有完整展示新版细小节编号：

> **只写能够权威核实的章名/知识节点，不猜小节编号。**

Lesson 头部必须增加：

```text
教材映射：当前人教版七上 · <章/知识群> · <知识节点>
映射类型：DIRECT / SPLIT / INTEGRATED / BRIDGE
```

综合课必须明确“不对应教材独立小节”。

---

# 三、Extension 触发机制

后续 Lesson 第一次明显依赖某个扩展专题时，必须显式提示：

> **前置扩展提示**：本节会使用 ______ 思想。建议先学习：[专题链接]。

并标记：

- `OPTIONAL`
- `RECOMMENDED`
- `REQUIRED-FOR-EXTENSION`

未提示的 Extension 不得成为 Core 或 Final Challenge 的隐藏前置。

当前已建立：

- `extensions/classification-as-a-method.md`：集合直觉、分类不重不漏、互斥/包含/相交、余数分类、抽屉原理、程序分支。

---

# 四、主线与边界

1. 教育部课标决定学段目标；
2. 人教版教材/教师用书决定 Core 顺序和概念边界；
3. Advanced/Olympiad/Final Challenge 主要依赖本讲及此前已学知识；
4. 超前内容只能延后、适龄改编或标为 EXTENSION；
5. Advanced/Olympiad 不能反客为主改变正式主线。

---

# 五、四轨体系

- **Core**：定义、性质、规范表达、教材典型模型、概念边界；
- **Advanced**：逆向、条件变化、综合、分类、整体、数形结合、校内高档题；
- **Olympiad**：数论、代数结构、组合、几何、构造、不变量、极端思想；
- **Informatics**：整数表示、offset、模运算、递推、组合、图论和算法证明。

---

# 六、概念深度

核心概念必须尽量回答：

- 为什么需要；
- 正式定义；
- 正例/反例/边界；
- 与相近概念区别；
- 表示形式与数学对象是否需要区分；
- 不同应用场景中的语义；
- 能否用自己的话解释；
- 能否迁移到陌生场景。

Core 最终稳定达到“会解释”，重要概念逐步达到“会迁移”。

---

# 七、应用场景

应用不能只换故事背景。应尽量覆盖不同数学语义：

- 状态；
- 位置/方向；
- 变化量；
- 偏差/误差；
- 比例/测量；
- 数据；
- 科学/工程；
- 金融/生活；
- 程序/算法。

---

# 八、例题体系

例题应形成：

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

重要例题说明突破口、关键条件、错误路径、检查点和可推广结构。

---

# 九、权威题源

课程依据和真题认证必须回到一手来源：

- 教育部、人教社；
- 正式考试原卷/教育主管部门/考试机构；
- MAA AMC、IMO 官方站、CEMC、UKMT；
- 中国数学会 CMO、全国高中数学联赛等正式赛事；
- 可靠正式出版物。

新闻、自媒体、商业题库转载、论坛和搜索摘要不得作为课程依据。

题源标签：

- `TEXTBOOK-MODEL`
- `SOURCE`
- `ADAPTED`
- `SYNTHESIS`
- `DESIGNED`

赛事选择按：

$$
\text{教学匹配度}+\text{权威性}+\text{当前可解性}+\text{思维价值}
$$

而不是赛事名气。

---

# 十、Po-Shen Loh 方法

参考：陌生题先独立探索、少机械重复、分级 hints、多方法、解后推广。

仅作为教学方法论，不作为题源认证。

---

# 十一、做题习惯

统一流程：

$$
\boxed{\text{提取条件}\rightarrow\text{明确所求}\rightarrow\text{建立关系}\rightarrow\text{执行检查}\rightarrow\text{回代核对}}
$$

每讲明确 H1～H10 中的重点纠偏，并按需要设计 `DIAGNOSTIC-Hx`。

---

# 十二、Final Challenge

必须：

1. 当前知识可解；
2. 题面不泄露方法；
3. 有真正突破口；
4. 优先有权威题源/结构；
5. Hint 1 → Hint 2 → Hint 3；
6. 解后一般化/第二方法/条件变化；
7. 真正服务本讲核心；
8. 不依赖未提示的 Extension。

好题若主要训练下一讲或某 Extension，应移动到对应位置。

---

# 十三、Markdown / LaTeX 渲染规则｜v1.6

课程主要在 GitHub Web / Mobile 阅读，排版必须优先保证稳定显示。

## 强制规则

1. Markdown 标题中禁止 `$...$`；
2. 简单数值和单位在正文中优先普通文本：`−5`、`0 ℃`、`3 cm`、`20%`；
3. 不使用 `$0^\circ\mathrm C$` 一类可直接文本化的单位表达；
4. 纯数字行内 LaTeX（如 `$-4$`）属于发布错误；
5. LaTeX 留给分数、根式、变量、方程、不等式、乘方等真正需要数学结构的内容；
6. 数学答案不放进 `<details>` 等原生 HTML 折叠块。

## 自动检查

发布前运行：

```bash
python3 tools/lint_markdown_rendering.py <本次修改的 Markdown 文件>
```

GitHub Actions 也会自动检查提交中发生变化的 Markdown 文件。

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

Extension：

```text
semester/
└── extensions/
    ├── README.md
    ├── topic.md
    ├── topic-exercises.md
    └── topic-solutions.md
```

当堂训练留主课；答案和课后题分离。

---

# 十五、强制 Release Review

新 Lesson 首次发布、重大修改或迁移新标准时，必须 Review：

- **R0 主线定位**：Mainline 还是 Extension；当前位置是否必要；
- **R0.5 教材映射**：章/知识节点、映射类型、Core 边界是否正确；
- R1 课程逻辑；
- R2 课标/教材覆盖；
- R3 概念深度；
- R4 知识边界；
- R5 应用场景；
- R6 例题/训练梯度；
- R7 题源质量；
- R8 错误/习惯；
- R9 Final Challenge；
- R10 前后衔接；
- **R11 Markdown / LaTeX 渲染稳健性**。

结论：`PASS / PASS WITH MINOR FIXES / REVISE / BLOCK`。

R0 或 R0.5 错误时最高只能 `REVISE`；R11 存在高风险渲染错误时不得 `PASS`。

---

# 十六、发布前硬检查

- [ ] 当前标准已读取；
- [ ] 当前教材映射表已读取；
- [ ] R0 已确认 Mainline / Extension 定位；
- [ ] R0.5 已确认章/知识节点和映射类型；
- [ ] Mainline 顺序符合课标/人教版与知识依赖；
- [ ] 未猜测无法权威确认的新版小节编号；
- [ ] Core 覆盖无遗漏；
- [ ] 概念无内部逻辑冲突；
- [ ] 应用真正服务概念；
- [ ] 例题有梯度；
- [ ] 题源来自权威一手资料；
- [ ] AMC/IMO/CMO 等赛事题未因名气而超纲；
- [ ] 原创题有必要性；
- [ ] H 标签明确；
- [ ] Final Challenge 贴本讲核心且无隐藏 Extension 前置；
- [ ] 前后课程不重复/断层；
- [ ] 标题无 `$...$`，简单数值/单位未滥用 LaTeX；
- [ ] Markdown 渲染自动检查通过；
- [ ] Release Review 已 PASS。
