# 第1讲题源与命题依据

> 对应主课：[第1讲《从“3−5”到负数——数系为什么必须继续扩展》](../01-positive-negative-numbers.md)
>
> 本文件记录例题、当堂训练、课后练习与 Final Challenge 的题源和改编依据。目标不是追求“全部真题”，而是保证：**能用高质量真题/教材模型覆盖的地方优先使用；真题覆盖不到的概念诊断、迁移和错误辨析允许少量教学原创，但必须明确标注。**

---

## 1. 标记规则

- **SOURCE**：基本保留原题数学结构，仅做语言翻译、单位或数字微调。
- **ADAPTED**：由明确真题的核心数学结构改编，情境、数字或问法发生变化。
- **SYNTHESIS**：融合两个或以上可追溯题源的结构，再结合本讲知识重新设计。
- **DESIGNED**：教学原创。只有当现有题源不能精确覆盖某个重要概念、易错点或迁移目标时才使用。

### 原则

1. 不把 `DESIGNED` 冒充真题。
2. 不因为追求“真题比例”而塞入与本讲概念弱相关的题。
3. Final Challenge 优先采用 `SOURCE / ADAPTED / SYNTHESIS`；若必须原创，要写明为什么现有题源不足。
4. 题目正文不大量复制原题文字，尽量使用等价改编，并保留官方出处。

---

## 2. 官方题源索引

### S1｜CEMC 2023 Gauss Grade 7, Question 4

主题：负温度与跨越 0 的温差。

官方页面：
https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023Gauss7Contest.html

本讲用途：Core 中“负温度不是异常值”“跨越 0 比较差值”的真实竞赛依据。

### S2｜CEMC 2017 Gauss Grade 7, Question 17

主题：已知平均数，在一个未知数据与平均数关系之间建立约束。

官方页面：
https://cemc.uwaterloo.ca/sites/default/files/documents/2017/2017Gauss7Contest.html

本讲用途：平均数—偏差—未知量模型。

### S3｜CEMC 2016 Gauss Grade 7, Question 18

主题：一组数据平均数已知，移除一个数据后研究新平均数。

官方 PDF：
https://cemc.uwaterloo.ca/sites/default/files/documents/2016/2016Gauss7Contest.pdf

本讲用途：整体总量、平均数和单个数据之间的联系；为 Final Challenge 的整体变化思想提供依据。

### S4｜CEMC 2019 Gauss Grade 7, Question 10

主题：比较两组数据的平均数是否相等。

官方页面：
https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019Gauss7Contest.html

本讲用途：把“平均数”理解为基准，而不是机械计算公式。

### S5｜CEMC 2026 Gauss Grade 7, Question 11

主题：实际测量数据的平均数。

官方页面：
https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026Gauss7Contest.html

本讲用途：真实测量数据、平均数和偏差语言之间的连接。

### CEMC 历年官方题库

https://cemc.uwaterloo.ca/resources/past-contests

---

## 3. 主课例题题源审计

| 内容 | 标记 | 依据 / 说明 |
|---|---|---|
| 场景 A：天气 | ADAPTED · S1 | 使用负温度和跨越 0 的变化这一竞赛结构；数字和问法为教学改写 |
| 场景 B：账户 | DESIGNED | 为解释“负数表示状态而非错误”设计，现有真题不必强行替代 |
| 场景 C：电梯 | DESIGNED | 为建立“基准 + 两侧方向”模型设计 |
| 例题 1：相反意义的量 | DESIGNED | 概念辨析题，需要专门覆盖“同一种量”这一易错点 |
| 例题 2：零件质量 | DESIGNED | 为建立 `实际值—标准值—偏差` 三量模型设计 |
| 例题 3：水位记录 | DESIGNED | 用连续数据强化偏差到实际值的迁移 |
| 例题 4：方向表示 | DESIGNED | Core 基础诊断 |
| 例题 5：逆向读取 | DESIGNED | 训练从数学符号还原现实语义 |
| 例题 6：基准改变 | DESIGNED | 本讲核心“相对性”模型，无合适单一真题可直接覆盖 |
| 例题 7：平均数与缺失偏差 | ADAPTED · S2/S4 | 将平均数未知量真题结构改写成“围绕平均数看偏差” |
| Advanced 基准法巧算 | DESIGNED | 这是本课程希望建立的方法线，题目用于揭示方法，不是伪装真题 |
| Olympiad 平均数与偏差 | ADAPTED · S2/S3 | 从平均数约束与整体总量变化结构改编 |
| 比赛积分 | DESIGNED | 为后续有理数加法做语义铺垫 |
| “负负得正”方向直觉 | DESIGNED | 概念预告，不属于检测题 |
| Informatics `delta/offset` | DESIGNED | 数学到程序变量的最小教学示例 |

---

## 4. 当堂训练题源审计

### Core 1–6

- Q1：DESIGNED｜分类诊断。
- Q2：DESIGNED｜正方向读取。
- Q3：DESIGNED｜人为约定正负方向，避免“正=好、负=坏”误解。
- **Q4：ADAPTED · S1｜CEMC 2023 Gauss Grade 7 Q4 的负温度差模型。**
- Q5：DESIGNED｜0 的边界性质。
- Q6：DESIGNED｜“相反意义的量”反例辨析。

### Advanced 7–11

- Q7：DESIGNED｜标准值到实际值。
- Q8：DESIGNED｜同一实际值换基准。
- Q9：DESIGNED｜海拔基准迁移。
- **Q10：ADAPTED · S2｜平均数约束下求未知数据，改写为偏差语言。**
- Q11：DESIGNED｜基准法方法检测。

### Olympiad 12–15

- **Q12：ADAPTED · S4｜从“不同数据组具有相同平均数”的结构改写为“偏差和为 0”。**
- **Q13：ADAPTED · S2/S3｜平均数与整体偏差约束的组合改编。**
- Q14：DESIGNED｜基准平移，是本讲特有核心迁移点。
- Q15：DESIGNED｜基准法竞赛化训练。

### Informatics 16–18

均为 **DESIGNED**。理由：这三题不是为了模拟编程竞赛题，而是把数学中的 `基准—差值—坐标` 映射到程序语义；使用真实竞赛代码题反而会引入尚未学习的算法负担。

### Final Challenge 19

**SYNTHESIS · S2 + S3 + 本讲“基准改变”模型。**

- S2 提供“平均数约束与未知量”的真题结构；
- S3 提供“整体总量随单个/部分数据变化”的真题结构；
- 本讲加入“统一改变基准时，每个偏差同步平移”的核心概念；
- 综合后形成一道新的奥赛级迁移题。

因此它不是某一届竞赛的原题，也不会标成“真题”；它是**有明确真题结构依据的综合改编题**。

---

## 5. 课后练习题源审计

### A 组 1–4

均为 **DESIGNED**：用于基础概念与偏差模型的延迟回忆，这类题需要精确匹配课堂目标。

### B 组 5–8

- **Q5：ADAPTED · S1｜负温度跨越 0 的多步版本。**
- Q6：DESIGNED｜人为定义正负方向的应用。
- Q7：DESIGNED｜同一实际值在多个基准下的表示。
- Q8：DESIGNED｜解释型反例题。

### C 组 9–12

- Q9：DESIGNED｜基准法。
- **Q10：ADAPTED · S3/S5｜平均数和整体偏差模型。**
- **Q11：ADAPTED · S2｜未知数据相对平均数的关系。**
- Q12：DESIGNED｜基准平移，直接检验本讲特有迁移能力。

### D 组 13–15

均为 **DESIGNED**：用于数学到程序/坐标的迁移，不冒充信息学竞赛真题。

---

## 6. 为什么仍保留一部分 DESIGNED

现有真题往往考一个已经成熟的知识点，而完整课程还必须覆盖：

- 概念形成过程；
- 反例与边界；
- 常见错误；
- 从“会算”到“会解释”；
- 同一概念在现实、奥数和程序中的迁移；
- 尚未形成标准竞赛题型、但对后续学习非常重要的方法。

因此本课程不追求“100% 真题”。更重要的标准是：

> **来源真实可追溯 + 改编理由明确 + 原创比例受控 + 每一道原创题都有不可替代的教学目的。**

---

## 7. 后续维护要求

Lesson 2 以后，每讲在发布前都应完成类似的题源审计：

1. 先检索教材、校内考试、CEMC、AMC、UKMT、CSP-J/NOI 等真实题源；
2. 选择与本讲知识真正相关的题，不为凑真题而凑真题；
3. 对改编题保留原始赛事、年份、年级/组别、题号；
4. 对原创题写出它补了哪个“真题覆盖空白”；
5. Final Challenge 必须标明 `SOURCE / ADAPTED / SYNTHESIS / DESIGNED` 中的一类。
