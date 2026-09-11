# Lesson 7 题源、教材与课程对标｜有理数大小比较｜v2.4

> 课标/人教版决定主线；公开优秀课程只做横向benchmark；官方竞赛题做真实迁移；最高层按 R3.8 独立审核。

---

# 1｜权威主线

## S0｜教育部《义务教育数学课程标准（2022年版）》

https://www.moe.gov.cn/srcsite/A26/s8001/202204/W020220420582346895190.pdf

## S1｜人民教育出版社当前初中数学新教材介绍

https://www.pep.com.cn/xw/zt/hd/12/xjcjs/cz/202408/t20240826_1994351.html

## S2｜人教社新教材结构解读

https://www.pep.com.cn/xw/zt/hd/12/zbtjc/202410/t20241022_1996035.html

## S3｜人教社官方七上历史教材目录

https://www.pep.com.cn/products/jc/czjks/201510/t20151026_1250813.shtml

用途：确认数轴、相反数、绝对值、大小比较处于同一有理数知识链。不把旧目录当2026新版细目录。

---

# 2｜公开优秀课程横向对标

## B1｜猿辅导公开课程：相反数与绝对值 / 有理数与数轴 / 真题追踪

https://www.yuanfudao.com/lessons/13541538.html

## B2｜猿辅导公开人教版系统班：有理数综合、绝对值代数/几何意义

https://www.yuanfudao.com/lessons/13307972.html

## B3｜北京新东方公开初一数学课程页

https://bj.xdf.cn/ucan1v1/ketang/chuyi/31368.html

这些公开页面说明优质同步/进阶课程通常不会把“有理数、绝对值、数轴”完全割裂，而会安排综合和真题追踪。

本课程进一步要求：

```text
会比较
→ 能从距离结构推排序
→ 能从排序反推符号
→ 能证明不可能/完整
→ 能推广到任意绝对值组
```

商业课程不作为知识真伪判据，也不复制其讲义。

---

# 3｜实际采用的官方竞赛来源

## S4｜CEMC 2018 Gauss Grade 7 Question 6

**标签**：`ADAPTED`  
**角色**：Competition Bridge

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2018Gauss7Contest.html

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018GaussSolution.html

用途：区间定位/双重大小关系。

## S5｜CEMC 2026 Gauss Grade 7 Question 3

**标签**：`ADAPTED`  
**角色**：Competition Bridge

官方原题：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026Gauss7Contest.html

官方解答：

https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026GaussSolution.html

用途：区分原数大小与离0距离。

两题均不作为★★★★★证据。

---

# 4｜v2.4 T0 / Final 为什么是 DESIGNED

无单一原题。

设计知识核：

```text
数轴左右顺序
+ 相反数
+ 绝对值分层
+ 负数区镜像反序
```

T0 新增“重复绝对值组”：

```text
0<|A|=|B|<|C|<|D|=|E|
```

迫使学生同时使用：

- 固定正距离最多两个位置；
- 互异 + 同绝对值 → 相反数对；
- 最大绝对值控制两端；
- 标签排序与符号恢复。

Final 再推广到任意 k 个绝对值组，每组1或2个标签，要求推出合法标签排序数量与符号可恢复性的一般定理。

---

# 5｜R3.8 难度真实性

Final 至少有三个非显然节点：

1. 从最大绝对值组向内递归，而不是枚举全部正负；
2. 单点组与相反数对虽然结构不同，但在非最小层都只贡献一个“可见二选一”；
3. 最小组若为单点，其符号不会改变标签排名，因此计数少一个因子；若为相反数对，该二选一仍可见。

最高层即使把具体数字全部去掉，思维核心仍存在，所以不是计算伪难度。

---

# 6｜知识边界

不依赖：

- 排列组合公式；
- 有理数加减；
- 不等式系统变形；
- 函数单调性。

`2^k` 只作为“k个独立可见二选一”的结果，不要求组合数学术语。

---

# 7｜发布规则

- `ADAPTED` 题旁必须有官方原题/解答链接；
- T0 / Final 明确 `DESIGNED`；
- 公开商业课程benchmark只进入本 provenance，不作为原题来源；
- T0 前不得泄露“最小单点组不贡献可见二选一”的 Final 结论。
