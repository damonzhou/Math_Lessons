# 七年级上册 · 自学进阶课程

目标：以当前人教版七年级上册与《义务教育数学课程标准（2022年版）》为主线，完成：

$$
\text{课内掌握}\rightarrow\text{概念理解}\rightarrow\text{校内拔高}\rightarrow\text{奥赛思维}\rightarrow\text{信息学迁移}
$$

所有课程编写先读取：

- [当前课程标准](../../docs/standards/CURRENT.md)
- [课程标准总入口](../../COURSE_STANDARD.md)

当前规范：**v1.3 + v1.4 + v1.5**。

v1.5 特别要求：正式编号 Lesson 优先保持课标、人教版知识顺序和真实知识依赖；Advanced/Olympiad/Informatics 方法专题若不是当前主线强前置，则放入 `extensions/`，以后真正需要时再提示学习。

建议节奏：每周2讲新课 + 1次复盘/测试，自学进度领先学校约1～2周即可，不机械追求超前速度。

---

# 七上 36 讲正式主线

## 模块一：从小学算术进入初中数系

1. **正数和负数：为什么数学需要扩展数系**
2. **有理数的意义与分类：写法、对象与身份**
3. **数轴：怎样把“数”变成直线上的位置**
4. **相反数：数轴上的对称位置**
5. **绝对值（一）：距离的定义与几何意义**
6. **绝对值（二）：含字母、分类讨论与绝对值方程直觉**
7. **有理数大小比较：数轴、绝对值与多种表示的统一**
8. **数轴综合：两点距离、中点、动点与距离和**

主依赖链：

$$
\boxed{
\text{有理数}
\rightarrow
\text{数轴}
\rightarrow
\text{相反数}
\rightarrow
\text{绝对值}
\rightarrow
\text{大小比较}
\rightarrow
\text{数轴综合}
}
$$

---

## 模块二：有理数的运算

9. 加法：方向、大小与运算结构
10. 减法：为什么可以转化成加法
11. 乘法与除法：符号规律的来源
12. 乘方：底数、指数与符号陷阱
13. 运算律与巧算：重组、凑整、分配律
14. 有理数综合：混合运算、规律与新定义

---

## 模块三：从算术到代数

15. 为什么要用字母表示数
16. 数量关系翻译：把文字变成代数式
17. 代数式的值：代入与整体代入
18. 规律表达（一）：从具体到一般
19. 规律表达（二）：图形与数列中的代数模型

---

## 模块四：整式

20. 单项式、多项式与整式结构
21. 同类项：为什么有些项可以合并
22. 去括号：符号变化的本质
23. 整式加减：标准化简流程
24. 整式综合：整体思想、条件求值与结构识别

---

## 模块五：一元一次方程

25. 什么是方程：从算术答案到未知数
26. 等式性质：每一步变形为什么合法
27. 一元一次方程基本解法
28. 复杂方程：去括号、去分母与规范步骤
29. 应用题：怎样寻找等量关系
30. 方程综合：行程、利润、配套、分段与方案问题

---

## 模块六：几何图形初步

31. 几何语言：点、线、面与位置关系
32. 直线、射线、线段：长度、和差、中点与分类讨论
33. 动点线段题：几何与数轴的统一
34. 角：度分秒、角平分线、余角与补角
35. 几何推理入门：从“算对”到“说清理由”

---

## 模块七：全册综合

36. 七上数学思想总复盘：数形结合、分类讨论、转化、整体、方程、从特殊到一般

---

# Extensions｜按需要学习，不占正式编号

## E1｜[分类是一种数学方法——集合直觉、余数与抽屉原理](./extensions/classification-as-a-method.md)

内容包括：

- 分类“不重不漏”；
- 元素与集合直觉；
- 属于 / 包含；
- 互斥 / 包含 / 相交；
- 奇偶与余数分类；
- 周期与多条件筛选；
- 抽屉原理；
- 程序条件分支。

学习机制：

- 当前数轴 Core **不需要** E1；
- 后续第一次明显使用余数分类、抽屉原理、复杂集合重叠或程序多标签时，Mainline 会明确提示 `OPTIONAL / RECOMMENDED / REQUIRED-FOR-EXTENSION`；
- 未提示的 Extension 不得成为 Core 或 Final Challenge 的隐藏前置。

[查看所有 Extensions](./extensions/README.md)

---

# 已完成并通过当前标准 Review

## Lesson 1

- [第1讲：从“3−5”到负数——数系为什么必须继续扩展](./01-number-system/01-positive-negative-numbers.md)

## Lesson 2

- [第2讲：有理数的分类——一个数的“写法”和“身份”为什么不是一回事？](./01-number-system/02-rational-number-classification.md)
  - [当堂训练答案](./01-number-system/solutions/02-rational-number-classification-classroom.md)
  - [课后练习](./01-number-system/exercises/02-rational-number-classification-homework.md)
  - [课后练习答案](./01-number-system/solutions/02-rational-number-classification-homework.md)
  - [题源审计](./01-number-system/sources/02-rational-number-classification-provenance.md)
  - [做题习惯诊断](./01-number-system/diagnostics/02-rational-number-classification-habits.md)
  - [v1.5 Release Review](./01-number-system/reviews/02-rational-number-classification-release-review-v1.5.md)

## Lesson 3

- [第3讲：数轴——怎样把“数”变成直线上的位置](./01-number-system/03-number-line.md)
  - [当堂训练答案](./01-number-system/solutions/03-number-line-classroom.md)
  - [课后练习](./01-number-system/exercises/03-number-line-homework.md)
  - [课后练习答案](./01-number-system/solutions/03-number-line-homework.md)
  - [题源审计](./01-number-system/sources/03-number-line-provenance.md)
  - [做题习惯诊断](./01-number-system/diagnostics/03-number-line-habits.md)
  - [v1.5 Release Review](./01-number-system/reviews/03-number-line-release-review-v1.5.md)

## Extension E1

- [分类是一种数学方法](./extensions/classification-as-a-method.md)
- [专项练习](./extensions/classification-as-a-method-exercises.md)
- [练习答案](./extensions/classification-as-a-method-solutions.md)

原旧路径 `01-number-system/03-classification-sets-partitions.md` 仅保留兼容跳转说明，不再是正式 Lesson。

---

# 后续建设原则

每讲遵循 `docs/standards/CURRENT.md` 指向的当前课程标准。

任何新 Mainline Lesson 发布前都必须先完成：

> **R0 主线定位 → R1～R10 整体 Review → PASS**

如果未来改变全局课程原则，创建新的标准版本；单讲内容微调不自动升级课程标准。
