# 当前课程标准

> **当前版本：v1.6**  
> **生效日期：2026-09-01**  
> **状态：ACTIVE**

所有 Lesson、专题、训练、答案、题源审计、学习诊断和 Release Review，默认遵循：

1. [课程标准 v1.3](./course-standard-v1.3.md) — 完整课程框架、权威一手来源与 Release Review 门禁；
2. [课程标准 v1.4](./course-standard-v1.4.md) — AMC / IMO / CMO 等国内外权威奥赛题源池；
3. [课程标准 v1.5](./course-standard-v1.5.md) — 正式主线与 Extension 分层、需要时提示学习机制、R0 主线定位审查；
4. [课程标准 v1.6](./course-standard-v1.6.md) — Markdown / LaTeX 渲染稳健性、简单数值/单位文本化、R11 自动渲染检查。

v1.6 首次归档提交：

`208668577cd2f6dcfddd967a2c00a97b5b2aa807`

## 当前必须执行的核心规则

- 课程主线由教育部课标、人教版官方教材/教师用书及真实知识依赖决定；
- 每个 Lesson 首次发布或重大更新前必须整体 Review；
- Review 从 **R0 主线定位**开始，并增加 **R11 Markdown / LaTeX 渲染稳健性**；
- Advanced / Olympiad / Informatics 可以加深课程，但不能无必要地打断正式主线；
- 主要属于方法论、竞赛或信息学的主题优先放入 `extensions/`；
- Extension 在后续真正需要时必须显式提示学习，并标注 OPTIONAL / RECOMMENDED / REQUIRED-FOR-EXTENSION；
- 不得把未提示的 Extension 当成主课或 Final Challenge 的隐藏前置；
- 课程设计和真题认证必须回到权威一手来源；
- 奥赛题源池包括 AMC、CEMC、UKMT、IMO、CMO / 中国数学会正式赛事等；
- 新闻、自媒体、商业题库转载、论坛和搜索摘要不得作为课程依据或真题认证依据；
- 搜索工具只用于定位官方资料；
- Markdown 标题禁止使用 `$...$`；
- 正文中的简单数值和单位优先普通文本，例如 `−5`、`0 ℃`、`3 cm`、`20%`；
- LaTeX 只用于真正需要数学结构的表达；
- Lesson 发布前必须通过 `tools/lint_markdown_rendering.py` 的渲染检查。

## 当前七上数系主线

```text
Lesson 1  正数和负数
Lesson 2  有理数的意义与分类
Lesson 3  数轴
Lesson 4  相反数
Lesson 5  绝对值……
```

原“分类/集合/余数”Lesson 3 已调整为 Extension，后续按需要提示学习；旧 Mainline 文件已删除。

## 使用规则

1. 新 Lesson 或重大修改前先读取本文件；
2. 再读取 v1.3、v1.4、v1.5、v1.6；
3. 不以会话记忆替代仓库标准；
4. 全局规则变化创建新版本，不覆盖旧版本；
5. Mainline Lesson 标记完成前必须通过 R0～R11 完整 Release Review。
