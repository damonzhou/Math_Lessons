# 第X讲 课程标题

> **年级**：X年级  
> **学期**：上/下  
> **模块**：XXX  
> **定位**：Mainline / Extension  
> **课程标准**：读取 `docs/standards/CURRENT.md`  
> **教材映射**：当前人教版 · <章/知识群> · <知识节点>  
> **映射类型**：DIRECT / SPLIT / INTEGRATED / BRIDGE  
> **建议用时**：Core XX分钟；Ceiling Diagnostic 10～20分钟；Advanced XX分钟；Olympiad + Informatics XX分钟  
> **前置知识**：XXX  
> **关键词**：XXX

> **Release Review**：`./reviews/XX-lesson-release-review-vX.Y.md`

---

# R0. 主线定位｜写课前先完成

先回答：

1. 本主题是 Mainline 还是 Extension？
2. 如果是 Mainline，它为什么必须在当前位置学习？
3. 后续哪些主线知识直接依赖它？
4. 如果教材没有独立章节，是否仍有足够强的知识依赖理由？
5. 是否存在更重要、更直接的教材主线应该先学？
6. Advanced/Olympiad 是否正在反客为主改变 Core 顺序？

Mainline 优先满足：

$$
\boxed{\text{课标要求}+\text{人教版顺序}+\text{知识依赖}+\text{认知连续性}}
$$

若主要属于方法论、竞赛或信息学，应优先放入 `extensions/`。

---

# R0.5. 教材映射｜v1.7+

Mainline 发布前读取对应教材映射表。

七上：

`docs/textbook-mapping-grade-07-semester-1.md`

检查：

1. 当前章/知识群是什么？
2. 对应哪个教材知识节点？
3. DIRECT / SPLIT / INTEGRATED / BRIDGE 哪一种？
4. Core 是否严格服务教材节点？
5. 哪些 Advanced/Olympiad 内容必须明确标为深化？
6. 是否错误猜测了官方未公开的新版细小节编号？

无法权威核实新版小节编号时，只写章名/知识节点。

---

# 0. 课程依据与知识边界

发布前必须确认：

1. 教育部课标要求；
2. 人教版教材/教师用书安排；
3. 学生此前已正式学过哪些工具；
4. 依据是否来自权威一手资料。

> **课标是底线和边界，不是课程深度上限。**

新闻、自媒体、商业题库转载、论坛和搜索摘要不能作为课程事实依据或真题认证依据。

## 前置扩展提示｜如适用

如果本讲某个 Advanced/Olympiad 部分第一次明显依赖 `extensions/` 中的专题，必须显式写：

> **前置扩展提示（OPTIONAL / RECOMMENDED / REQUIRED-FOR-EXTENSION）**：本节会使用 ______ 思想。建议先学习：[专题链接]。

未提示的 Extension 不得成为 Core、Ceiling Diagnostic 或 Final Challenge 的隐藏前置。

---

# 1. 学习层级

## MUST

完整覆盖当前教材节点，不以最低会做作为完成标准。

## SHOULD

重要方法、校内拔高和高频迁移。

## EXTENSION

奥数、信息学或后续数学连接；不得伪装成当前必会。

---

# 2. 五层深度目标｜v1.9

| 层级 | 目标 |
|---|---|
| L1 教材完整 | 定义、性质、表示、正反例、边界、规范表达、典型应用完整覆盖 |
| L2 概念深度 | 为什么、相近概念、反例、边界、表示转换、条件变化 |
| L3 校内高阶 | 逆向、参数、隐藏条件、分类、综合、校内压轴结构 |
| L4 竞赛/信息学迁移 | 权威竞赛陌生结构、一般化、算法化、真实迁移 |
| L5 上限诊断 | 方法未完整教学前冷启动，测学生独立发现能力 |

---

# 3. 本讲习惯检查点

选择 H1～H10 中本讲重点，并写出具体执行动作。

统一流程：

$$
\boxed{\text{提取条件}\rightarrow\text{明确所求}\rightarrow\text{建立关系}\rightarrow\text{执行检查}\rightarrow\text{回代核对}}
$$

---

# 4. 权威题源与标签｜v1.8+

标签：

- `TEXTBOOK-MODEL`
- `SOURCE`
- `ADAPTED`
- `SYNTHESIS`
- `DESIGNED`

正式权威题源池包括：

- 教育部/人教社官方教材与资源；
- 可追溯校内/区市统考/中考原卷；
- MAA AMC 8/10/12、AIME、USAJMO/USAMO；
- IMO 官方题目/公开 Shortlist；
- CEMC Gauss 等官方竞赛；
- UKMT JMC/JMO；
- 中国数学会 CMO、全国高中数学联赛、中国女子数学奥林匹克等正式赛事；
- CSP-J/NOI 等信息学官方题目结构。

使用规则：

$$
\text{教学匹配度}+\text{权威性}+\text{当前可解性}+\text{思维价值}
$$

赛事越高级不代表越适合当前 Lesson。IMO/CMO 等高阶题必须通过适龄筛选。

每讲维护：

```text
sources/XX-lesson-provenance.md
```

provenance 必须分成：

## 4.1 实际采用来源

记录真正进入本讲的教材依据、真题、改编题和结构来源。

## 4.2 候选权威题源池审查

至少显式记录 AMC / IMO / CMO / CEMC / UKMT / 国内正式考试等与本讲相关来源的审查结果。

## 4.3 Ceiling Diagnostic 来源与区分度

明确：

- 哪一道题承担上限诊断；
- 为什么当前知识可解；
- 为什么它不是前文已教模板的简单换皮；
- 为什么能区分独立发现、提示后完成和教学后掌握。

---

# 5. Markdown / LaTeX 渲染预检｜v1.6 + v1.8

写课过程中遵守：

- 标题中不写 `$...$`；
- 简单数值/单位用普通文本：`−5`、`0 ℃`、`3 cm`、`20%`；
- 单个变量、带正负号的变量、简单与0比较也用普通文本：`a`、`−a`、`a > 0`、`a = 0`、`a < 0`；
- 纯数字或上述简单变量表达的行内 LaTeX 属于发布错误；
- 分数、根式、多层括号、复合公式、方程等真正需要数学结构的内容继续使用 LaTeX；
- 完整数学答案不放 `<details>`。

发布前运行：

```bash
python3 tools/lint_markdown_rendering.py <本次修改的 Markdown 文件>
```

---

# 第一部分：情境导入

用真正服务于概念的场景暴露旧知识不足、产生问题或建立共同结构。

---

# 第二部分：概念为什么出现

回答：为什么需要？旧知识哪里不够？新概念解决什么？

---

# 第三部分：核心定义、正反例与边界

核心概念尽量包含：正式定义、通俗解释、数学表达、正例、反例、边界、相近概念区别、表示形式与数学对象区别（如适用）。

---

# 第四部分：Core 训练

确保 L1 教材完整层已经稳定，然后进入上限诊断。

---

# 第五部分：Ceiling Diagnostic｜v1.9

> **首次尝试时不要打开 Hint 或答案。**

要求：

1. Core 已学完，但 Advanced/Olympiad 方法尚未完整讲解；
2. 当前及此前知识足够；
3. 前文没有出现高度同构完整模板；
4. 至少一个真实突破口；
5. 建议独立 10～20 分钟；
6. 记录首次卡点与 H1～H10；
7. 独立尝试后才开放 Hint 1 → Hint 2 → Hint 3 → Full Solution。

记录等级：

- C5-A：独立完成并能一般化；
- C5-B：独立找到核心结构，有次要错误；
- C5-C：Hint 1 后完成；
- C5-D：Hint 2 后完成；
- C5-E：Hint 3 后完成；
- C5-F：看完整解答后才能理解。

---

# 第六部分：应用场景

不要只换故事。检查不同数学语义和真实迁移。

---

# 第七部分：Advanced / Olympiad / Informatics

在 Ceiling Diagnostic 完成后再系统教学相关高阶方法。

Advanced 不机械超前；Olympiad 强调陌生结构、分层 hints 和一般化；Informatics 说明数学模型与程序/算法对应。

---

# 第八部分：错误实验室

展示真实/高频错误路径，说明为什么会错、怎样发现、下次在哪一步检查。

---

# 第九部分：当堂训练

按需要覆盖 Core、Advanced、Olympiad、Informatics、DIAGNOSTIC。

---

# 第十部分：Mastery Challenge / Final Challenge

教完高阶方法后用于验证真正掌握与迁移。

必须：当前知识可解、题面不泄露方法、有真实突破口、优先权威题源/结构、有 Hint 1～3、解后一般化、不依赖未提示 Extension。

> 如果该题的核心方法已在前文完整教学，它是 Mastery Challenge，不能同时冒充唯一的 Ceiling Diagnostic。

---

# 第十一部分：掌握度、复习与知识地图

至少区分：

- 会认；
- 会用；
- 会解释；
- 会迁移；
- 能独立发现结构。

设置24小时和7天复习；Ceiling Diagnostic 至少安排一个不同表面结构的延迟迁移检查。

---

# 第十二部分：Release Review｜发布前强制

必须审查：

- R0 主线定位
- R0.5 教材映射
- R1 课程逻辑
- R2 课标/教材覆盖
- R3 概念深度
- **R3.5 最高深度与能力上限诊断**
- R4 知识边界
- R5 应用场景
- R6 例题/训练梯度
- R7 题源质量：实际采用 + 候选池 + Ceiling Diagnostic 来源
- R8 错误/习惯
- R9 Mastery/Final Challenge
- R10 前后衔接
- R11 Markdown / LaTeX 渲染稳健性

只有 R3.5 也通过，才能标记“最高深度覆盖完成”。
