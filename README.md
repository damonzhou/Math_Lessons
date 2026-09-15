# Math Lessons

面向七至九年级的数学课程仓库，兼顾教材知识节点、概念深化、灵活应用、奥数证明与信息学数学思维。

> **唯一当前标准入口**：[CURRENT.md](./docs/standards/CURRENT.md)。当前标准v2.4，最新课程内容修订2026-09-15。  
> [COURSE_STANDARD.md](./COURSE_STANDARD.md)及历史标准用于追溯；不能用旧课程或聊天中的旧PASS覆盖最新状态。

## 课程入口

[七年级上册36讲路线与发布进度](./grade-07/semester-1/README.md) · [教材知识节点映射](./docs/textbook-mapping-grade-07-semester-1.md) · [标准v2.4](./docs/standards/course-standard-v2.4.md)

| 已建立主课 | 入口 |
|---|---|
| Lesson 1～2 | [正数和负数](./grade-07/semester-1/01-number-system/01-positive-negative-numbers.md) · [有理数](./grade-07/semester-1/01-number-system/02-rational-number-classification.md) |
| Lesson 3～4 | [数轴](./grade-07/semester-1/01-number-system/03-number-line.md) · [相反数](./grade-07/semester-1/01-number-system/04-opposite-numbers.md) |
| Lesson 5～6 | [绝对值（一）](./grade-07/semester-1/01-number-system/05-absolute-value-part1.md) · [绝对值（二）](./grade-07/semester-1/01-number-system/06-absolute-value-part2.md) |
| Lesson 7～8 | [大小比较](./grade-07/semester-1/01-number-system/07-rational-number-comparison.md) · [数轴综合](./grade-07/semester-1/01-number-system/08-number-line-integration.md) |

集合方法保持为[可选专题](./grade-07/semester-1/extensions/classification-as-a-method.md)，不改教材主线。年级与学期目录保留，可继续扩充初二初三。

## 2026-09-15发布修订

本次按[复审原记录](./docs/audits/lessons-05-08-v2.4-independent-review-2026-09-15.md)修订Lesson 5～8，详见[整改回执](./docs/audits/lessons-05-08-v2.4-remediation-2026-09-15.md)。修正L6执行顺序记号，补齐L7题干；增加UKMT JMO、AMC8的具体官方题，补传统绝对值最值和离散动点；Gauss真题成为L8正式Final，研究反例改可选并补出处。

每讲主课、当堂答案、ceiling分级提示、课后题、课后答案、题源、诊断、release review同步。下一正式新课仍是Lesson 9《有理数加法》；本次没有提前创建。

## 长期课程目标

知道概念、理解原因、正确应用、识别陌生结构、完整证明、构造与一般化。基础已会时不重复占主要课时；难度来自数学关系与知识组合，不靠长计算或隐藏未来工具。

人教版及课标决定Core节点，竞赛拓展明确分层。课堂题嵌入正文；答案与分级提示独立。官方题在题旁给原卷/解答，改编说明变化，原创不冒充真题。允许AMC、IMO、CMO、UKMT、CEMC及国内正式来源，是否实际采用和核验逐题记录。

T0先独立尝试；Builder针对首个卡点；T1验证训练后的应用；T2约一周后检验保持与变化条件后的迁移。相同题换名字只算近迁移，不夸大为陌生迁移。

## 质量检查的范围

- Markdown Render Lint：检查改动Markdown的渲染风险。
- Problem Source Link Lint：检查题旁来源字段，不认证外部网页当前可读。
- Lessons 5-8 Math Regression：12组有限数学与活跃文件链接回归，不替代一般证明或学生试教。

所有自动结果以具体提交的GitHub Actions为准。静态review不是独立第三方认证；知识节点覆盖不是未实际进行的2026印次逐页审核。

```text
python3 tools/lint_markdown_rendering.py
python3 tools/lint_problem_source_links.py
python3 tools/check_lessons_05_08.py
```

复杂数学仍保留LaTeX；简单数字、单位、变量及比较用普通文本；标题不放行内数学命令，完整数学答案不放HTML折叠。
