# Lesson 7 题源与核验｜2026-09-15修订

## 教材定位与覆盖

对照[教材知识节点映射](../../../../docs/textbook-mapping-grade-07-semester-1.md)和[人教社官方解读](https://www.pep.com.cn/xw/zt/hd/12/zbtjc/202410/t20241022_1996035.html)：数轴顺序、正零负、负数绝对值反序、多数排序、分数小数表示转换。节点覆盖不等于逐页核验2026印次。高阶分组生成和范围推断为拓展。

## 实际引用

C1：ADAPTED，CEMC2018 Gauss G7 Q6。[原题](https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2018Gauss7Contest.html) / [解答](https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018GaussSolution.html)。补齐原来缺失的候选数，唯一严格区间答案−7/4。当前只是基础Bridge。

C2：ADAPTED，CEMC2026 Gauss G7 Q3。[原题](https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026Gauss7Contest.html) / [解答](https://cemc.uwaterloo.ca/sites/default/files/documents/2026/2026GaussSolution.html)。补齐实际数字和四个所求，不再只写来源及改编说明。

K1：SOURCE，2023 AMC8 P25。[主办方入口](https://maa.org/resource/sample-competition-2023-amc-8/) / [官方原卷PDF第9页](https://maa.org/wp-content/uploads/2024/08/2023-Problems-AMC8-PDF.pdf) / [官方解答链接](https://maa.org/wp-content/uploads/2024/08/2023_AMC8_Solutions_.pdf)。原卷读取并截图核验。解答链接由官方入口给出，本次访问403，未声称读到官方证明。课程自行用间隔16以下/18以上排除，再以范围夹定起点；有限枚举核验唯一(a₁,间隔,a₁₄)=(3,17,224)，答案8。

K1保持原条件，省略选项并追加解释，原始问题与课程追问分开。这个题把等距与区间推断相接，不靠未来等差数列公式；是具体官方难题，不代表所有原创Final都被AMC认证。

## 原创与难度校正

T0与一般排序压轴均DESIGNED。保留已正确的分组生成结论，补命名0条目变式：有0时所有组方向选择均可见，计数为2的k次方。主文不预先给计数公式，答案给完整双向证明。Builder已经讲过的外层方法只算训练，不再算Final的独立新突破。

作业10为AMC方法的近迁移，刻意保留两个合法答案以训练“范围未必唯一”；不是另外一题赛事原题。

## 候选题池

本次实际采用AMC2023P25；P18留Lesson8，UKMT2023B6及2024B3分别服务Lesson5、6。IMO/CMO/国内正式试题仍是允许池，本次没有具体一手匹配项，未完成的审查不写“是”。市面课程大纲不能替代实际原题核验。

## 回归范围

`tools/check_lessons_05_08.py`穷举k=1～5时每组1/2标签、全部符号分配、有无0，核验计数结论；并核验AMC整数约束。有限范围用于防退化，k任意的结论由课程证明支撑。
