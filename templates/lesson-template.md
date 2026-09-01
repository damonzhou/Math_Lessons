# 第X讲 课程标题

> **年级**：X年级  
> **学期**：上/下  
> **模块**：XXX  
> **定位**：Mainline / Extension  
> **课程标准**：读取 `docs/standards/CURRENT.md`  
> **教材映射**：当前人教版 · <章/知识群> · <知识节点>  
> **映射类型**：DIRECT / SPLIT / INTEGRATED / BRIDGE  
> **建议用时**：Core XX分钟；Advanced XX分钟；Olympiad + Informatics XX分钟  
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

# R0.5. 教材映射｜v1.7

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

新闻、自媒体、商业题库转载、论坛和搜索摘要不能作为课程事实依据或真题认证依据。

## 前置扩展提示｜如适用

如果本讲某个 Advanced/Olympiad 部分第一次明显依赖 `extensions/` 中的专题，必须显式写：

> **前置扩展提示（OPTIONAL / RECOMMENDED / REQUIRED-FOR-EXTENSION）**：本节会使用 ______ 思想。建议先学习：[专题链接]。

未提示的 Extension 不得成为 Core 或 Final Challenge 的隐藏前置。

---

# 1. 学习层级

## MUST

本讲 Core，最终至少达到“会解释”。

## SHOULD

重要方法、校内拔高和高频迁移。

## EXTENSION

奥数、信息学或后续数学连接；不得伪装成当前必会。

---

# 2. 四轨目标

| 层级 | 目标 |
|---|---|
| Core | 教材概念、性质、表达无漏洞 |
| Advanced | 逆向、条件变化、综合、方法选择 |
| Olympiad | 陌生问题中发现结构 |
| Informatics | 数学进入程序和算法 |

---

# 3. 本讲习惯检查点

选择 H1～H10 中本讲重点，并写出具体执行动作。

统一流程：

$$
\boxed{\text{提取条件}\rightarrow\text{明确所求}\rightarrow\text{建立关系}\rightarrow\text{执行检查}\rightarrow\text{回代核对}}
$$

---

# 4. 权威题源与标签

标签：

- `TEXTBOOK-MODEL`
- `SOURCE`
- `ADAPTED`
- `SYNTHESIS`
- `DESIGNED`

优先题源：

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

---

# 5. Markdown / LaTeX 渲染预检｜v1.6

写课过程中遵守：

- 标题中不写 `$...$`；
- 简单数值/单位用普通文本：`−5`、`0 ℃`、`3 cm`、`20%`；
- 纯数字行内 LaTeX 属于发布错误；
- 不写 `$0^\circ\mathrm C$` 一类不必要的单位 LaTeX；
- 分数、根式、变量、方程、不等式等继续使用 LaTeX；
- 完整数学答案不放 `<details>`。

发布前运行：

```bash
python3 tools/lint_markdown_rendering.py <本次修改的 Markdown 文件>
```

---

# 第一部分：情境导入

用真正服务于概念的场景暴露旧知识不足、产生问题或建立共同结构。

至少一次“停下来想一想”。

---

# 第二部分：概念为什么出现

回答：为什么需要？旧知识哪里不够？新概念解决什么？

---

# 第三部分：核心定义、正反例与边界

核心概念尽量包含：

- 正式定义；
- 通俗解释；
- 数学表达；
- 正例；
- 反例；
- 边界；
- 相近概念区别；
- 表示形式与数学对象的区别（如适用）。

---

# 第四部分：应用场景

不要只换故事。检查是否覆盖不同数学语义：状态、位置、变化、偏差、比例、测量、数据、科学/工程、金融/生活、程序/算法。

---

# 第五部分：例题链

按需要组织：

1. 直接应用；
2. 逆向；
3. 概念辨析；
4. 条件变化；
5. 综合；
6. 方法发现；
7. 真实应用；
8. 陌生迁移。

重要解析说明突破口、关键条件、错误路径和检查点。

---

# 第六部分：错误实验室

展示真实/高频错误路径，说明为什么会错、怎样发现、下次在哪一步检查。

---

# 第七部分：Advanced / Olympiad / Informatics

Advanced 不机械超前。

Olympiad 参考 Po-Shen Loh 式问题设计：先探索、分层 hints、少机械重复、解后推广；这是方法论，不是题源标签。

Informatics 说明数学模型与程序变量/算法的对应。

---

# 第八部分：当堂训练

按需要覆盖：

- A Core
- B Advanced
- C Olympiad
- D Informatics
- E DIAGNOSTIC

题目留正文，答案独立。

---

# 第九部分：Final Challenge

必须：

1. 当前知识可解；
2. 题面不泄露方法；
3. 有真正突破口；
4. 优先有权威题源/结构；
5. Hint 1 → Hint 2 → Hint 3；
6. 解后一般化/第二解法/条件变化；
7. 真正服务本讲核心；
8. 不依赖未提示 Extension。

---

# 第十部分：掌握度、复习与知识地图

- Level 1 会认
- Level 2 会用
- Level 3 会解释
- Level 4 会迁移

设置24小时和7天复习，并给出下一讲连接。

---

# 第十一部分：Release Review｜发布前强制

必须审查：

- **R0 主线定位**
- **R0.5 教材映射**
- R1 课程逻辑
- R2 课标/教材覆盖
- R3 概念深度
- R4 知识边界
- R5 应用场景
- R6 例题/训练梯度
- R7 题源质量
- R8 错误/习惯
- R9 Final Challenge
- R10 前后衔接
- **R11 Markdown / LaTeX 渲染稳健性**

Review 文件：

```text
reviews/XX-lesson-release-review-vX.Y.md
```

只有 R0、R0.5 正确，R11 通过，且最终结论达到 `PASS`（或完成 minor fixes 后 PASS），才把课程标记为完成。
