# 第4讲题源与命题依据｜相反数｜v1.7

> 对应主课：[第4讲《相反数——为什么数轴上的对称位置代表一对特殊的数》](../04-opposite-numbers.md)
>
> 教材映射：[七上36讲 ↔ 当前人教版教材映射](../../../../docs/textbook-mapping-grade-07-semester-1.md)
>
> 发布 Review：[Lesson 4 v1.7 Review](../reviews/04-opposite-numbers-release-review-v1.7.md)

---

# 1. 课程与教材依据

## P0｜教育部《义务教育数学课程标准（2022年版）》

官方入口：

https://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582346895190.pdf

第四学段“有理数”要求明确包含：

- 用数轴上的点表示有理数；
- 借助数轴理解相反数和绝对值的意义；
- 掌握求相反数和绝对值的方法。

### 本讲用途

确定知识依赖：

```text
数轴 → 相反数 → 绝对值
```

并确定相反数是正式 Core，不是竞赛扩展。

---

## P1｜人教版义务教育数学（七～九年级）新教材介绍

官方页面：

https://www.pep.com.cn/xw/zt/hd/12/xjcjs/cz/202408/t20240826_1994351.html

用于确认当前新教材依据2022课标，并按照逻辑性、连续性、整体性、关联性组织课程。

---

## P2｜李海东《突出数学本质 重视思维过程 发展核心素养》

人教社官方页面：

https://www.pep.com.cn/xw/zt/hd/12/zbtjc/202410/t20241022_1996035.html

用于确认：

- 新版将旧“有理数”拆分为“有理数”和“有理数的运算”；
- 有理数概念学习得到更充分空间。

本讲因此定位在“有理数”概念知识群，不放到“有理数的运算”。

---

## P3｜人教社官方历史同步资源

官方页面：

https://www.pep.com.cn/products/jf/zhxxjf/qxktbljf/201509/t20150917_1246918.shtml

历史资源明确列出稳定的概念顺序：

```text
有理数
→ 数轴
→ 相反数
→ 绝对值
```

### 使用限制

该资源只用于辅助确认长期稳定的知识依赖和传统概念边界。

**不把其旧版小节编号冒充2026新版小节编号。**

---

# 2. 权威数学/竞赛结构来源

## C1｜CEMC Open Courseware · Opposite Integers

University of Waterloo CEMC 官方课程资源：

https://courseware.cemc.uwaterloo.ca/27/assignments/563/5

该资源从数轴说明：

- 正负整数位于0两侧；
- opposite integers 到0距离相同、方向相反；
- 0需要单独处理；
- 负数侧是正数侧的镜像结构。

### 本讲用途

支持：

- 相反数的数轴对称解释；
- “同样远 + 两侧”而不是只背符号；
- 0的特殊性；
- 从相反数连接后续整数运算。

这是一手官方教学资源，不是竞赛真题，因此不标 `SOURCE · Contest`。

---

## C2｜CEMC 2020 Gauss Grade 7 Q8

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020Gauss7Contest.html

该题使用等距数轴刻度结构，通过已知标记推断数值关系。

### 本讲用途

只提取：

> **等距点 + 已知结构 → 反推整体数轴**

用于 Final Challenge 的结构骨架。

Final Challenge 没有复制原题题面，属于：

> `SYNTHESIS · C1 opposite symmetry + C2 equal-spacing structure + current lesson model`

---

# 3. Mainline 内容审计

| 内容 | 类型 | 依据/用途 |
|---|---|---|
| 相反数数轴定义 | TEXTBOOK-MODEL | P0/P1/P3 |
| 0的相反数 | TEXTBOOK-MODEL | P0/P3 + definition boundary |
| $a$ 的相反数为 $-a$ | TEXTBOOK-MODEL | Core notation |
| $-a$ 不一定为负 | DESIGNED · DIAGNOSTIC | 防止字母符号误判 |
| $-(-a)=a$ | TEXTBOOK-MODEL | 连续两次原点对称 |
| 负号角色辨析 | DESIGNED · DIAGNOSTIC | 负数符号 / unary opposite / subtraction |
| 海拔、偏差、位移 | DESIGNED · Application | 检查“同基准 + 同大小 + 反方向” |
| 对称点相距18 | DESIGNED · Advanced | 中点/对称直觉，不用后续公式 |
| unary minus | DESIGNED · Informatics | 数学相反数→程序取负 |
| 八个等距点 | SYNTHESIS · C1+C2 | Final Challenge |

---

# 4. 知识边界审计

本讲故意**不把以下内容作为 Core**：

## 4.1 绝对值

虽然相反数的一对点到0距离相同，但不正式引入：

$$
|a|
$$

留给 Lesson 5。

## 4.2 相反数之和为0

这条性质很自然，但有理数加法正式安排在 Lesson 9。

本讲不把：

$$
a+(-a)=0
$$

作为必须掌握的法则，以免反过来用尚未正式学习的有理数加法定义相反数。

## 4.3 大小比较的代数变号规律

不正式教授：

$$
a<b\Rightarrow -a>-b
$$

该结构可在数轴上直观观察，但系统大小比较留到 Lesson 7。

## 4.4 两点距离公式

Final Challenge 只使用“等距”和“中间位置”，不使用：

$$
|a-b|
$$

---

# 5. Final Challenge 审计

## 题型

8个等距点 A～H：

- B、G 为一对相反数；
- C 表示 −6；
- 恢复原点、尺度和全部坐标。

## 突破口

不是先算刻度，而是：

$$
\boxed{\text{相反关系}\rightarrow\text{对称中心}\rightarrow\text{点对}\rightarrow\text{尺度}}
$$

## 当前知识可解性

只需：

- 数轴；
- 相反数；
- 等距；
- 小学除法与简单分数；
- Lesson 3 的刻度恢复直觉。

不需要：

- 绝对值；
- 有理数加法法则；
- 方程；
- 集合 Extension。

## 质量检查

- [x] 当前知识可解；
- [x] 题面不直接给方法；
- [x] 有“原点不在刻度上”的真实突破；
- [x] 有权威结构来源；
- [x] 有 Hint 1 → Hint 2 → Hint 3；
- [x] 能推广到参数 $k$；
- [x] 服务相反数核心，不是一般数轴重复题。

---

# 6. 题源标签纪律

本讲不把：

- CEMC courseware 称为竞赛真题；
- Final Challenge 称为 Gauss 原题；
- 历史人教版小节编号称为2026新版编号。

所有标签均按 v1.7 使用。

---

# 7. 禁止来源

本讲没有使用：

- 新闻报道；
- 自媒体；
- 商业题库转载；
- 论坛/博客；
- 搜索摘要；
- 无法核实出处的“奥赛题”。
