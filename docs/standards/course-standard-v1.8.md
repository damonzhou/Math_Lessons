# 课程标准 v1.8｜题源候选池可见性与简单表达渲染

> **状态**：LOCKED / 增量标准  
> **生效日期**：2026-09-01  
> **基于**：v1.3 + v1.4 + v1.5 + v1.6 + v1.7

---

# 1. 为什么增加本标准

两个问题需要成为全局规则：

1. 某个 Lesson 的 provenance 过去只列“实际采用的来源”，如果该讲没有使用 AMC / IMO / CMO，会让读者误以为这些权威题源已被排除；
2. Markdown 渲染规则虽然已经禁止简单纯数字使用行内 LaTeX，但 `a`、`-a`、`a>0` 等简单表达仍可能在部分 GitHub 客户端暴露 `$`。

因此 v1.8 同时增强：

- 题源候选池审查的可见性；
- 简单数学表达的稳定文本化规则。

---

# 2. Provenance 必须区分“采用来源”和“候选池审查”

每讲 `sources/XX-lesson-provenance.md` 至少包含两层：

## A. 实际采用来源

列出真正进入本讲课程、例题、训练或 Final Challenge 的来源，并标明：

- 来源机构；
- 年份/赛事/题号（如适用）；
- `SOURCE / ADAPTED / SYNTHESIS / TEXTBOOK-MODEL / DESIGNED`；
- 在本讲承担什么教学功能。

## B. 候选权威题源池审查

至少显式检查与本讲主题相关的权威题源池：

- MAA：AMC 8 / AMC 10 / AMC 12、AIME、USAJMO / USAMO；
- IMO 官方历年题 / 公开 Shortlist；
- University of Waterloo CEMC：Gauss 等；
- UKMT：JMC / JMO 等；
- 中国数学会：CMO、全国高中数学联赛、中国女子数学奥林匹克等；
- 与本讲相关的国内正式考试原卷；
- Informatics 相关主题可审查 CSP-J / NOI 等官方题源。

对没有选用的高权威来源也要写明理由，例如：

- 超出当前知识；
- 年龄/难度不匹配；
- 与本讲核心概念匹配度不如另一官方来源；
- 需要后续知识；
- 没有找到可核验且教学价值足够高的适龄原题。

**不要求每讲机械使用 AMC / IMO / CMO。要求的是“进入候选审查视野，并把取舍理由公开”。**

---

# 3. 题源选择顺序不按赛事名气

仍执行 v1.4 原则：

$$
\boxed{\text{教学匹配度}+\text{来源权威性}+\text{当前知识可解性}+\text{思维价值}}
$$

例如：

- 七年级数轴/相反数问题，Gauss 或 AMC 8 的适龄结构可能优于 IMO / CMO；
- 若 IMO / CMO 某题恰好仅用当前知识且结构优秀，可以直接 SOURCE/ADAPTED；
- 不得为了 provenance 中“出现 IMO/CMO”而强行使用超纲题。

---

# 4. R7 题源质量新增检查项

Release Review 的 R7 从 v1.8 起增加：

- [ ] provenance 已列实际采用来源；
- [ ] provenance 已列候选权威题源池审查；
- [ ] AMC / IMO / CMO 等未选用时有明确原因，而不是静默缺失；
- [ ] 未因赛事级别高而牺牲适龄性；
- [ ] 未把“审查过”误写成“实际题源”。

---

# 5. 简单数学表达文本化

在 GitHub Web / Mobile 课程正文中，以下简单表达优先普通文本 / Unicode：

```text
a
−a
a > 0
a = 0
a < 0
−5
0 ℃
3 cm
20%
```

避免仅为了排版写成：

```text
$a$
$-a$
$a>0$
```

仍然应该使用 LaTeX 的典型情况：

- 分数：`\frac{3}{7}`；
- 根式；
- 多层括号或复杂式子；
- 多项式、方程组、较长等式/不等式；
- 需要数学结构清晰展示的公式。

原则：

> **简单符号用稳定文本，复杂结构才使用数学渲染。**

---

# 6. Markdown lint 要求

`tools/lint_markdown_rendering.py` 应将以下简单行内 LaTeX 视为发布错误：

- 纯数字；
- 单个变量；
- 带单个正负号的变量；
- 简单变量与0的比较。

例如：

```text
$-4$   → ERROR
$a$    → ERROR
$-a$   → ERROR
$a>0$  → ERROR
```

而以下继续允许：

```text
$\frac{3}{7}$
$-(-a)=a$
$|a-b|$
```

---

# 7. 与此前标准的关系

v1.8 不改变：

- 人教版 Mainline 顺序；
- 36讲教材映射；
- Mainline / Extension 分层；
- AMC / IMO / CMO 等权威题源池本身；
- Final Challenge 规则；
- H1～H10 诊断体系。

它只新增两项治理要求：

$$
\boxed{\text{题源取舍可见}+\text{简单表达稳定渲染}}
$$
