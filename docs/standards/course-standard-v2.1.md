# 课程标准 v2.1｜题目原题链接与可追溯性门禁

> **状态**：ACTIVE / 增量标准  
> **生效日期**：2026-09-05  
> **基于**：v1.3～v1.9 + v2.0

---

# 1. 为什么增加本标准

此前的 provenance 已能记录题源，但部分主课和课后题只写：

```text
ADAPTED · CEMC 2026 Gauss Grade 7 Q3
```

读者仍需要跳到 provenance 才能找到官方原题。

这不满足“题目本身可追溯”的要求。

从 v2.1 起：

> **凡题目使用真实考试/竞赛原题或其改编结构，题目附近必须直接给出官方原题链接。**

provenance 继续负责完整审计；题目旁链接负责即时核验。

---

# 2. SOURCE / ADAPTED 的强制格式

凡题目标题或标签为 `SOURCE` / `ADAPTED`，必须在题目正文开始前直接写：

```markdown
> 原题：[官方原题｜赛事 年份 组别 Qx](官方链接)  
> 官方解答：[官方解答](官方链接)
```

要求：

1. 优先赛事主办方/考试机构官方页面；
2. 明确年份、组别、题号；
3. 有官方解答时必须一起链接；
4. 若官方只提供整卷 PDF/HTML，则链接整卷并在文字中标清题号；
5. 不用商业题库、博客、转载页替代官方链接；
6. `ADAPTED` 必须继续说明本题已改编，不得伪装成原题。

---

# 3. SYNTHESIS 的强制格式

若题目由一个或多个具体权威题目结构综合而来，应写：

```markdown
> **SYNTHESIS · 无单一原题**  
> 结构来源：
> - [官方原题 A｜...](...)
> - [官方原题 B｜...](...)
```

若综合只依赖教材概念、课程诊断模型，没有具体竞赛原题，则明确写：

```text
SYNTHESIS · 无单一原题；结构依据见 provenance
```

禁止让 `SYNTHESIS` 看起来像某一道真实竞赛原题。

---

# 4. DESIGNED / TEXTBOOK-MODEL

- `DESIGNED`：没有原题链接是正常的，但 provenance 必须解释原创必要性；
- `TEXTBOOK-MODEL`：不是教材原题，不得伪造“原题链接”；可链接教材/课标依据，但必须继续标明是模型题。

---

# 5. 题目页面与 provenance 的职责分工

## 题目页面

负责让学生/家长/教师在当前页面直接看到：

- 题源标签；
- 官方原题链接；
- 官方解答链接；
- 是否为改编/综合。

## provenance

继续负责完整记录：

- 原题数学结构；
- 改编内容；
- 当前知识可解性；
- 教学目的；
- 候选 AMC / IMO / CMO / CEMC / UKMT / 国内正式考试题源池审查；
- Diagnostic / Builder / Mastery 的功能映射。

二者不能互相替代。

---

# 6. Release Review 新门禁｜R7.5

在 R7“题源质量”之后增加：

## R7.5｜题目级原题链接可追溯性

检查：

- [ ] 每个 `SOURCE` 题目旁有官方原题链接；
- [ ] 每个 `ADAPTED` 题目旁有官方原题链接；
- [ ] 有官方解答时已同时链接；
- [ ] 年份/组别/题号写清楚；
- [ ] `SYNTHESIS` 已说明“无单一原题”并列出结构来源；
- [ ] `DESIGNED` 没有被伪装成真实原题；
- [ ] 题目页与 provenance 的来源描述一致。

R7.5 不通过时，Lesson 不得标记 PASS。

---

# 7. 自动检查

新增：

```text
tools/lint_problem_source_links.py
```

自动检查发生变化的 Markdown 文件中，带 `SOURCE / ADAPTED / SYNTHESIS` 的题目标题是否在附近提供可追溯标记。

自动检查只负责发现明显遗漏，不能代替人工核验链接是否真的是官方一手来源。

---

# 8. 与既有标准的关系

v2.1 不改变：

- Mainline / Extension；
- AMC / IMO / CMO 等题源池；
- Ceiling Diagnostic / Builder / Mastery；
- T0/T1/T2；
- Markdown / LaTeX R11。

它新增的是：

\[
\boxed{\text{provenance 可追溯}\;\rightarrow\;\text{每一道有真实题源的题目本身也可直接追溯}}
\]

从 Lesson 7 起原生执行；Lesson 3～6 的现有来源题同步回填。