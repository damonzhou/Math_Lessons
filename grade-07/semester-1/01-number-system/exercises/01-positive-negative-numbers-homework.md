# 第1讲 课后练习

> 对应主课：[第1讲《从“3−5”到负数——数系为什么必须继续扩展》](../01-positive-negative-numbers.md)
>
> 题源与改编依据：[第1讲题源与命题依据](../sources/01-positive-negative-numbers-provenance.md)
>
> 建议完成主课后至少间隔数小时再做，不要边看讲义边答。

## 题源标记

- **TEXTBOOK-MODEL**：依据人教版 1.1 和教师用书的知识/题型模型重新组织，不是教材原题；
- **ADAPTED**：有明确竞赛真题结构依据；
- **DESIGNED**：少量教学原创，用于教材和现有题库难以精确覆盖的方法或迁移目标。

---

## A 组：基础巩固

### 1｜TEXTBOOK-MODEL · PEP

写出 3 个正数、3 个负数，并说明为什么 0 不放入其中任何一类。

### 2｜TEXTBOOK-MODEL · PEP

规定上升为正，下降为负：

- 上升 6.5 m；
- 下降 2.8 m；
- 没有变化。

分别怎样记录？

### 3｜TEXTBOOK-MODEL · PEP

规定“超过标准质量”为正，标准质量为 100 g。

实际质量分别为：

$$
103,\quad 98,\quad 100,\quad 99.5\text{ g}
$$

写出对应偏差。

### 4｜TEXTBOOK-MODEL · PEP

偏差记录为：

$$
+2.5,\quad -1.2,\quad 0
$$

标准值为 50，求三个实际值。

---

## B 组：理解与应用

### 5｜ADAPTED · S1

某地上午气温为 $-2^\circ\mathrm C$，中午升高 7℃，晚上又比中午降低 10℃。

1. 中午多少度？
2. 晚上多少度？
3. 晚上比早晨高还是低？相差多少？

> 这是 CEMC 2023 Gauss Grade 7 Q4“负温度跨越 0 比较”的多步改编。

### 6｜TEXTBOOK-MODEL · PEP

一名运动员目标成绩为 60 秒，规定“比目标慢”为正，“比目标快”为负。

实际成绩分别为：

$$
58.7\text{ s},\quad 61.2\text{ s},\quad 60\text{ s}
$$

写出对应记录。

### 7｜TEXTBOOK-MODEL · PEP + 轻度拓展

同一温度是 $12^\circ\mathrm C$。

- 以 $0^\circ\mathrm C$ 为基准；
- 以 $10^\circ\mathrm C$ 为基准；
- 以 $15^\circ\mathrm C$ 为基准。

分别记录其偏差。

说明：实际温度有没有改变？

### 8｜TEXTBOOK-MODEL · PEP

解释为什么下面这句话不严谨：

> “负数就是比没有还少。”

至少给出两个反例。

---

## C 组：Olympiad

### 9｜DESIGNED

用基准法计算：

$$
197+203+199+205+196
$$

### 10｜ADAPTED · S3/S5

7 个数的平均数为 30，其中 6 个数相对 30 的偏差为：

$$
+5,-2,+1,-6,+4,-3
$$

求第 7 个数。

> 结构参考 CEMC 2016 Gauss Grade 7 Q18 的“整体总量与平均数变化”以及 2026 Gauss Grade 7 Q11 的实际测量平均数模型。

### 11｜ADAPTED · S2

某班 4 人小组的平均身高为 160 cm。前三人身高分别比平均值高 3 cm、低 5 cm、高 4 cm。第四人身高是多少？

> 结构参考 CEMC 2017 Gauss Grade 7 Q17 的“平均数约束下求未知数据”。

### 12｜DESIGNED

一个数相对基准 40 的偏差是 $-7$。如果把基准改成 35，新偏差是多少？尝试不用先求实际值的方法解决。

---

## D 组：Informatics

### 13｜DESIGNED

程序记录某个量相对于昨日基准值的变化：

```cpp
int yesterday = 120;
int today = 116;
int delta = today - yesterday;
```

`delta` 是多少？它表达的数学含义是什么？

### 14｜DESIGNED

一个机器人以起点为 0，规定向前为正、向后为负。它依次移动：

$$
+5,\quad -2,\quad -4,\quad +3
$$

暂时不要使用正式的有理数加法规则，只根据动作含义判断机器人最后在起点前方还是后方，距离起点多少单位。

### 15｜DESIGNED

为什么游戏地图、图形程序和机器人控制中通常不能只使用非负坐标？写出一个自己的场景。

---

## 完成后

做完后再打开：[课后练习答案与提示](../solutions/01-positive-negative-numbers-homework.md)

如果有错题，回到主课的“错因记录表”进行分类，而不是只抄正确答案。
