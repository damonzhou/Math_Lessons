# 当前课程标准

> **当前版本：v2.0**  
> **生效日期：2026-09-02**  
> **状态：ACTIVE**

所有 Lesson、专题、训练、答案、题源审计、学习诊断和 Release Review，默认遵循：

1. [课程标准 v1.3](./course-standard-v1.3.md) — 完整课程框架、权威一手来源与 Release Review 门禁；
2. [课程标准 v1.4](./course-standard-v1.4.md) — AMC / IMO / CMO 等国内外权威奥赛题源池；
3. [课程标准 v1.5](./course-standard-v1.5.md) — 正式主线与 Extension 分层、需要时提示学习机制、R0 主线定位审查；
4. [课程标准 v1.6](./course-standard-v1.6.md) — Markdown / LaTeX 渲染稳健性、简单数值/单位文本化、R11 自动渲染检查；
5. [课程标准 v1.7](./course-standard-v1.7.md) — 36讲教材映射、R0.5 教材映射门禁；
6. [课程标准 v1.8](./course-standard-v1.8.md) — provenance 候选权威题源池审查可见性、简单变量/符号表达文本化；
7. [课程标准 v1.9](./course-standard-v1.9.md) — 最高深度覆盖、Ceiling Diagnostic 能力上限诊断、R3.5 门禁；
8. [课程标准 v2.0](./course-standard-v2.0.md) — Ceiling Builder 能力上限提升体系、T0/T1/T2 迁移验证、R3.6 门禁。

七上教材映射工作表：

- [七年级上册 36讲 ↔ 当前人教版教材映射](../textbook-mapping-grade-07-semester-1.md)

## 当前必须执行的核心规则

- 课程主线由教育部课标、人教版官方教材/教师用书及真实知识依赖决定；
- **课标是底线和知识边界，不是课程深度上限**；
- 每个 Mainline Lesson 必须能映射到当前人教版的正式章/知识节点，或明确标记为综合课；
- 人教社未公开完整新版细小节编号时，只写可权威核实的章名/知识节点，不猜编号；
- 每个 Lesson 首次发布或重大更新前必须整体 Review；
- Review 顺序从 **R0 主线定位 → R0.5 教材映射** 开始，并包含 **R3.5 最高深度与能力上限诊断、R3.6 能力上限提升设计、R11 Markdown / LaTeX 渲染稳健性**；
- 每讲必须覆盖六层：教材完整、概念深度、校内高阶、竞赛/信息学迁移、Ceiling Diagnostic、Ceiling Builder；
- Ceiling Diagnostic 必须在 Advanced/Olympiad 方法完整讲解前冷启动，不能用刚教过的同构模板假装能力上限；
- 上限诊断第一次尝试不开放 Hint，之后按 Hint 1 / 2 / 3 分级，并记录 C5-A～F；
- Ceiling Builder 必须针对上限诊断或长期做题习惯暴露的真实卡点，训练表示转换、条件变化、逆向构造、多方法比较、一般化或陌生迁移中的至少一种；
- 课程必须区分 **Ceiling Diagnostic（测上限）/ Ceiling Builder（提上限）/ Mastery Challenge（测教学后迁移）**；
- 每讲高阶能力尽量记录 T0 冷启动 → T1 教学后迁移 → T2 约7天后陌生迁移，不能只看最终正确率；
- 能力提升不能依靠提前灌输后续公式、定理或大量同模板训练；
- Advanced / Olympiad / Informatics 可以加深课程，但不能无必要地打断正式主线；
- 主要属于方法论、竞赛或信息学的主题优先放入 `extensions/`；
- Extension 在后续真正需要时必须显式提示学习，并标注 OPTIONAL / RECOMMENDED / REQUIRED-FOR-EXTENSION；
- 不得把未提示的 Extension 当成主课、Ceiling Diagnostic、Ceiling Builder 或 Final Challenge 的隐藏前置；
- 课程设计和真题认证必须回到权威一手来源；
- 奥赛题源池包括 AMC、CEMC、UKMT、IMO、CMO / 中国数学会正式赛事等；
- 每讲 provenance 必须区分“实际采用来源”和“候选权威题源池审查”，并说明哪些题承担 Ceiling Diagnostic、Ceiling Builder 和 Mastery/Final Challenge；
- AMC / IMO / CMO 等没有被本讲选用时，必须说明已审查及未选理由，不能静默缺失；
- 新闻、自媒体、商业题库转载、论坛和搜索摘要不得作为课程依据或真题认证依据；
- 搜索工具只用于定位官方资料；
- Markdown 标题禁止使用 `$...$`；
- 正文中的简单数值、单位、百分数、单个变量、带正负号变量及简单与0比较优先普通文本，例如 `−5`、`0 ℃`、`50%`、`a`、`−a`、`a > 0`；
- 百分数不使用 LaTeX `\%` 转义；GitHub/MathJax 中简单百分数一律直接写普通文本；
- LaTeX 只用于真正需要数学结构的表达；
- Lesson 发布前必须通过 `tools/lint_markdown_rendering.py` 的渲染检查。

## 当前七上章节主线

```text
有理数
→ 有理数的运算
→ 代数式
→ 整式及整式加减
→ 一元一次方程
→ 几何图形初步
→ 全册综合
```

当前已完成前六讲：

```text
Lesson 1  正数和负数
Lesson 2  有理数的意义与分类
Lesson 3  数轴
Lesson 4  相反数
Lesson 5  绝对值（一）
Lesson 6  绝对值（二）
```

原“分类/集合/余数”Lesson 3 已调整为 Extension，后续按需要提示学习；旧 Mainline 文件已删除。

## 使用规则

1. 新 Lesson 或重大修改前先读取本文件；
2. 再读取 v1.3～v1.9 + v2.0；
3. 七上 Mainline 同时读取教材映射表；
4. 不以会话记忆替代仓库标准；
5. 全局规则变化创建新版本，不覆盖旧版本；
6. Mainline Lesson 标记“最高深度 + 能力上限提升体系完成”前必须通过 R0、R0.5、R1～R3、R3.5、R3.6、R4～R11 完整 Release Review；
7. Lesson 1～4 已完成 v1.9 Ceiling Diagnostic、v2.0 Ceiling Builder 与 T0/T1/T2 兼容迁移，当前按 v2.0 标记完成；
8. Lesson 5～6 均从首次建设即原生包含 Ceiling Diagnostic、Ceiling Builder、T0/T1/T2、完整 provenance 与 R0～R11 Review，当前状态 PASS；
9. Lesson 7 及后续新 Lesson 均必须从首次建设开始执行同一最新标准；若 `CURRENT.md` 后续升级，则以升级后的 CURRENT 为准。
