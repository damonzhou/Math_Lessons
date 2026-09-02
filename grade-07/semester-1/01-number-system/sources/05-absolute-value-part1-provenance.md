# Lesson 5 题源与命题依据｜绝对值（一）

> **课程标准**：v2.0  
> **主题**：绝对值的距离意义、具体数求值、逆向位置、信息丢失  
> **发布要求**：实际采用来源 + 候选权威题源池审查 + Diagnostic / Builder / Mastery 功能映射

---

# 1. 课程与教材依据

## S0｜教育部《义务教育数学课程标准（2022年版）》

**机构**：中华人民共和国教育部  
**类型**：课程标准 / 一手来源  
**官方文件**：

https://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582346895190.pdf

第四学段“数与式”明确要求：

- 理解负数、有理数；
- 能用数轴上的点表示有理数；
- 能借助数轴体会相反数和绝对值的意义；
- 能求有理数的相反数和绝对值。

本讲据此把绝对值的 Core 建立在“数轴上的点到原点的距离”上，而不是只教符号操作。

---

## S1｜人民教育出版社当前初中数学新教材介绍

**机构**：人民教育出版社  
**类型**：当前教材结构依据 / 一手来源  
**官方页面**：

https://www.pep.com.cn/xw/zt/hd/12/xjcjs/cz/202408/t20240826_1994351.html

用途：确认当前教材依据2022版课标重构，课程 Mainline 继续以当前人教版正式知识逻辑为准。

本页面不完整公开2026七上所有细小节编号，因此本讲只写：

```text
当前人教版七上 · 有理数 · 绝对值
```

不猜新版小节编号。

---

## S2｜人教社官方历史教材/教师教学用书

**机构**：人民教育出版社  
**用途**：辅助确认长期稳定的知识依赖“数轴 → 相反数 → 绝对值”，不用于冒充2026新版细小节编号。

官方教材页面：

https://www.pep.com.cn/products/jc/czjks/201510/t20151026_1250813.shtml

官方教师教学用书页面：

https://www.pep.com.cn/products/jc/jks/201510/t20151026_1250885.shtml

历史人教版结构明确把数轴、相反数、绝对值作为有理数概念链连续展开。

---

# 2. 实际采用的竞赛结构来源

## S3｜CEMC 2019 Gauss Grade 8 Question 3

**机构**：University of Waterloo, CEMC  
**赛事**：2019 Gauss Contest, Grade 8  
**题号**：Q3  
**原结构**：从一组正负整数中判断哪个最接近0。  
**本讲标签**：`ADAPTED`

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019Gauss8Contest.html

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019GaussSolution.pdf

### 本讲使用

- 主课 Advanced 例1；
- Homework Q6。

### 改编内容

替换具体候选数，并要求显式写出“到0的距离”，强化：

```text
原数大小 ≠ 离0距离大小
```

不把改编题称为原题。

---

## S4｜CEMC 2021 Gauss Grade 7 Question 5

**机构**：University of Waterloo, CEMC  
**赛事**：2021 Gauss Contest, Grade 7  
**题号**：Q5  
**原结构**：比较若干正分数谁最接近0。  
**本讲标签**：`ADAPTED`

官方原题 PDF：

https://cemc.uwaterloo.ca/sites/default/files/documents/2021/2021Gauss7Contest.pdf

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2021GaussSolution.html

### 本讲使用

Homework Q14 将部分候选改为负分数，并增加“全部换成相反数后距离是否改变”的迁移问题。

### 教学目的

把“最接近0”从正分数比较迁移到：

- 正负号不改变到0距离；
- 相反数绝对值相同。

---

## S5｜CEMC 2022 Gauss Grade 8 Question 7

**机构**：University of Waterloo, CEMC  
**赛事**：2022 Gauss Contest, Grade 8  
**题号**：Q7  
**原结构**：在整数、分数、小数等不同表示中判断哪个值最接近0。  
**本讲标签**：`ADAPTED`

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022Gauss8Contest.html

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022GaussSolution.html

### 本讲使用

Homework Q7。

### 改编目的

保留“多种表示 + 到0距离”的核心结构，替换候选值，避免复制原题，并要求学生解释：

> “最小的原数”与“离0最近”为什么不是同一个判断。

---

## S6｜CEMC 2026 Gauss Grade 7 Question 3

**机构**：University of Waterloo, CEMC  
**赛事**：2026 Gauss Contest, Grade 7  
**题号**：Q3  
**原结构**：判断给定数中哪个在数轴上离0最远。  
**本讲标签**：`ADAPTED`

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026Gauss7Contest.html

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026GaussSolution.html

### 本讲使用

主课 Advanced 例2。

### 改编目的

用新的数值继续训练：

```text
离0最远 ↔ 到0距离最大
```

而不是凭正负号或原数排序做判断。

---

# 3. Ceiling Diagnostic 来源与原创必要性

## D1｜距离记录器

**标签**：`DESIGNED`  
**角色**：Ceiling Diagnostic / T0

题目核心：4个不同整数输入经过“只保存到0距离”的记录器，学生需要逆向恢复全部可能原坐标，并判断还缺多少方向信息。

### 为什么需要原创

本讲需要同时诊断以下能力：

1. 从绝对值输出逆向想到左右两个候选；
2. 发现0只有一个原像；
3. 使用“互不相同”筛选；
4. 完整枚举；
5. 判断信息不足；
6. 抽象“保留幅度、丢失方向”；
7. 进一步思考最少附加信息。

CEMC 2019/2021/2022/2026 的官方适龄问题很好地覆盖“离0近/远”，但并不同时覆盖上述逆向信息恢复目标。

因此本题为透明 `DESIGNED`，不是伪装竞赛真题。

### 当前可解性

只需要：

- 数轴；
- 相反数；
- 绝对值的距离定义；
- 基本分类枚举。

不需要 Lesson 6 的含字母分类公式。

---

# 4. Ceiling Builder 来源与训练增益

Builder 主要为 `DESIGNED / TEXTBOOK-MODEL`，围绕绝对值定义做认知重组，不追求赛事名气。

| Builder | 类型 | 训练目标 |
|---|---|---|
| 正向位置 ↔ 逆向距离 | TEXTBOOK-MODEL + DESIGNED | 表示转换、逆向恢复 |
| 删除“互不相同” | DESIGNED | 条件充分性、H3/H10 |
| 同绝对值反例 | TEXTBOOK-MODEL | 反例、边界、相反数连接 |
| 正距离两个位置/0一个位置 | DESIGNED | 特殊到一般 |
| 设计信息丢失机器 | DESIGNED | 逆向构造、信息意识 |

Builder 的目标不是重复求绝对值，而是让学生形成：

> **看到距离信息时主动问“方向是否丢失、答案是否唯一”。**

---

# 5. Mastery Challenge 来源与结构

## M1｜绝对值集合恢复原位置

**标签**：`SYNTHESIS`  
**角色**：Mastery Challenge / T1

结构来源：

- S3/S5/S6 的“到0距离比较与数轴解释”；
- 当前人教版绝对值距离定义；
- 本课程长期“条件充分性/唯一性”诊断模型。

题面本身不是任何一场竞赛原题，也不标为 `SOURCE`。

### 与 T0 的区别

T0：

```text
对象顺序已知
→ 每个对象的距离输出已知
→ 逆向枚举原输入
→ 找缺失方向信息
```

Mastery：

```text
只给无序绝对值集合
→ 利用重复值恢复相反位置
→ 再用数轴顺序排列
→ 用一个方向条件筛选唯一答案
```

不是简单换数字，新增了：

- 无序信息；
- 重复绝对值；
- 排序；
- 条件筛选。

---

# 6. 候选权威题源池审查｜v1.8 / v2.0

| 题源池 | 是否审查 | 是否采用 | 说明 |
|---|---|---|---|
| 教育部课标 | 是 | 是 | 决定 Core 边界 |
| 人民教育出版社 | 是 | 是 | 决定教材主线和知识依赖 |
| CEMC Gauss | 是 | 是 | 2019 G8 Q3、2021 G7 Q5、2022 G8 Q7、2026 G7 Q3 直接贴合“到0距离” |
| MAA AMC 8 | 是 | 否 | 当前公开检索未找到比上述 CEMC 结构更直接、且对本讲有额外诊断增益的官方题；不为赛事配额强行加入 |
| AMC 10/12、AIME、USAJMO/USAMO | 是 | 否 | 整体难度和工具层级高于本讲需要；基础绝对值概念无需借高级赛事制造假难度 |
| IMO 官方题 / Shortlist | 是 | 否 | 未选到只依赖当前知识且比适龄 CEMC 更匹配本讲核心的题 |
| UKMT JMC/JMO | 是 | 否 | 作为候选池保留；本讲已有可核验且更直接的 CEMC 数轴距离来源，不机械增加赛事数量 |
| CMO / 全国高中数学联赛 / 女子奥赛 | 是 | 否 | 高中竞赛知识与本讲概念层级不匹配；不因权威等级高而超纲 |
| 国内正式考试原卷 | 是 | 否 | 本次未使用来源不明题库；没有必要为基础定义额外引入无法优于教材/CEMC的一般校内题 |
| CSP-J / NOI | 是 | 否 | `abs()` 信息丢失作为 Informatics 迁移由数学语义直接设计，不伪装为竞赛原题 |

---

# 7. 三类高阶任务映射

| 任务角色 | 题目 | 标签 | 核心能力 |
|---|---|---|---|
| Ceiling Diagnostic | 距离记录器 | DESIGNED | 逆向恢复、完整枚举、信息充分性 |
| Ceiling Builder | 删条件/反例/逆向构造/信息机器 | DESIGNED / TEXTBOOK-MODEL | H3/H7/H10、特殊到一般 |
| Mastery Challenge | 绝对值集合恢复5个位置 | SYNTHESIS | 重复距离→相反位置→排序→条件筛选 |
| Olympiad迁移 | 最近/最远于0 | ADAPTED · CEMC | 区分原数大小与距离大小 |
| Informatics迁移 | `abs()` 不可逆 | DESIGNED | 数学对象→程序信息损失 |

---

# 8. 知识边界审查

本讲明确不使用：

- 含字母绝对值的完整分段/分类公式；
- 两点距离 `|a-b|`；
- 复杂绝对值方程/不等式；
- 函数图象；
- 有理数完整大小比较法则。

因此 Advanced、Diagnostic、Builder、Mastery 均保持“当前及此前知识可解”。

---

# 9. 发布结论

题源体系满足：

```text
课标/教材边界可核验
+ 适龄官方竞赛结构可追溯
+ 改编透明
+ 原创有明确诊断必要性
+ AMC/IMO/CMO 等候选池取舍可见
+ Diagnostic / Builder / Mastery 功能分离
```

最终是否发布 PASS 以：

`reviews/05-absolute-value-part1-release-review-v2.0.md`

为准。
