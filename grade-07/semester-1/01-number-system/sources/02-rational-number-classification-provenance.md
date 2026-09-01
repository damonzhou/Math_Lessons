# 第2讲题源与命题依据｜v1.5

> 对应主课：[第2讲《有理数的分类——一个数的“写法”和“身份”为什么不是一回事？》](../02-rational-number-classification.md)
>
> 发布 Review：[Lesson 2 v1.5 Review](../reviews/02-rational-number-classification-release-review-v1.5.md)

---

# 1. 课程依据｜权威一手来源

## P0｜教育部《义务教育数学课程标准（2022年版）》

https://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582346895190.pdf

用于确定“理解有理数的意义”等第四学段数与式要求。

## P1｜人民教育出版社官方资源

https://www.pep.com.cn/

用于确定有理数概念、整数/分数分类和当前知识边界。

## C1｜CEMC 2019 Gauss Grade 7 Q3

官方历年题入口：

https://cemc.uwaterloo.ca/resources/past-contests

核心结构：

$$
\frac14=25\%
$$

用于等价表示、分数/百分数同一数学对象。

主课改变图形份数和问法，因此标记：

> `ADAPTED · CEMC 2019 Gauss Grade 7 Q3 structure`

## C2｜CEMC 2025 Gauss Grade 7 Q8

官方历年题入口同上。

核心结构：使用 $\frac12$ 杯量具测量 $2\frac12$ 杯，体现“改变表示后操作关系更清楚”。

---

# 2. 本讲关键概念修订依据

旧版曾存在逻辑风险：

> “能写成两个整数之比”不能作为教材分类中“分数类”的判定条件，因为整数也能写成 $p/q$。

现行课程明确：

$$
\boxed{\text{能写成 }\frac pq\text{ 是有理数的统一特征}}
$$

而：

$$
\frac62=3
$$

按数的实际值应归入整数。

这也是本讲最重要的概念辨析之一。

---

# 3. 主课内容审计

| 内容 | 类型 | 教学目的 |
|---|---|---|
| 整数/分数/有理数 | TEXTBOOK-MODEL | Core 分类主线 |
| $p/q$ 统一表示 | SHOULD | 解释所有有理数共同结构 |
| $6/2=3$、3.0=3 | DESIGNED · DIAGNOSTIC | 写法 vs 数学对象 |
| 有限小数 | TEXTBOOK-MODEL | 有理数表示 |
| 分数/小数/百分数 | ADAPTED · C1 | 等价表示 |
| 配方量杯 | ADAPTED · C2 | 表示选择的真实作用 |
| 精确/近似 | DESIGNED | 连接测量、显示、后续近似数 |
| 循环小数 | EXTENSION | 只预告，不作为当前技能 |
| `int` / 整数除法 | DESIGNED · Informatics | 数学对象 vs 程序表示 |

---

# 4. v1.5 主线定位调整

旧规划曾把以下内容安排为正式 Lesson 3：

- 集合/包含系统化；
- 奇偶分类；
- 余数分类；
- 模6；
- 多条件筛选；
- 抽屉原理。

v1.5 Review 后确认：这些内容数学上正确且对竞赛/信息学有价值，但**不应打断**更强的教材知识链：

$$
\text{有理数}\rightarrow\text{数轴}\rightarrow\text{相反数}\rightarrow\text{绝对值}
$$

因此这些内容改为：

[Extension E1｜分类是一种数学方法](../../extensions/classification-as-a-method.md)

并采用“后续需要时提示学习”的机制。

正式下一讲为：

[Lesson 3｜数轴](../03-number-line.md)

Lesson 2 Core、Homework、Final Challenge 都**不依赖** E1。

---

# 5. Final Challenge

类型：

> `SYNTHESIS · 等价表示 + 四舍五入显示模型`

问题：设备显示0.38，反推原有理数的可能范围。

训练：

- 精确对象 vs 近似表示；
- 同一显示值可对应多个不同有理数；
- 从近似结果反推范围；
- 表示精度变化。

知识边界：只需小数、四舍五入、分数互化和不等关系直觉。

质量检查：

- [x] 当前知识可解
- [x] 贴合本讲核心
- [x] 有真正概念突破口
- [x] 有三级提示
- [x] 可推广到不同显示精度
- [x] 不依赖集合/余数 Extension

---

# 6. 权威奥赛题源池

后续 Olympiad 可从 AMC、CEMC、UKMT、IMO、CMO 等权威官方来源筛选。

本讲没有机械加入 IMO/CMO 高难题，因为：

$$
\text{适龄}+\text{概念匹配}+\text{当前可解}
$$

优先于赛事等级。

---

# 7. 来源限制

不使用新闻、自媒体、商业题库转载、论坛、搜索摘要认证课程知识或真题。

任何 `SOURCE / ADAPTED / SYNTHESIS` 都应能回到赛事官方资料或正式可核验出版物。
