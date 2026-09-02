# Lesson 3 v2.0 题源补充｜Ceiling Diagnostic / Builder

本文件补充原 `03-number-line-provenance.md`。

## 1. Ceiling Diagnostic

类型：`SYNTHESIS · CEMC number-line structures + DESIGNED-DIAGNOSTIC`

冷启动题使用“6个等距点、B = −1、E = 5”的结构。

它不是某一道 CEMC 原题；设计目的是在系统讲“恢复刻度”之前测试：

- 是否拒绝默认每格1；
- 是否用两个锚点恢复尺度；
- 是否接受原点落在两个刻度之间；
- 删除“等距”后能否构造反例。

## 2. Ceiling Builder

类型：`DESIGNED · TRAINING`

Builder 分别训练：

- 两锚点恢复尺度；
- 删除等距条件后的不唯一性；
- 逆向设计非单位刻度数轴；
- 从具体刻度推广到“起点 + 间隔数 × 每格变化”的一般结构。

## 3. Mastery Challenge

原“损坏数轴恢复”继续作为 `SYNTHESIS · MASTERY`。

它在学生已经学过非单位刻度、两锚点和尺度恢复后使用，所以明确定位为教学后的综合迁移。

## 4. 已采用的权威结构

原 provenance 已核对并记录：

- CEMC 2016 Gauss Grade 7 Q10；
- CEMC 2018 Gauss Grade 7 Q6；
- CEMC 2020 Gauss Grade 7 Q8；
- CEMC 2026 Gauss Grade 7 Q3；
- 教育部2022课标与人教社官方数轴主线。

v2.0 新题只提取这些适龄数轴结构，不冒充原题。

## 5. 候选权威题源池审查

| 题源池 | 审查 | 结论 |
|---|---|---|
| 人教版 / 课标 | 已审查 | 决定数轴三要素、数与点、大小顺序的 Core |
| CEMC Gauss | 已审查 | 数轴、等距、位置恢复高度匹配，继续作为主要结构来源 |
| MAA AMC 8 | 已审查 | 有适龄数轴/位置结构，但本轮未发现比现有 CEMC 结构更必要的替换 |
| UKMT JMC | 已审查 | 保留候选，适合后续陌生迁移 |
| IMO / Shortlist | 已审查 | 当前数轴基础主题不需要高阶证明，不强行采用 |
| CMO / 中国数学会赛事 | 已审查 | 知识层级过高，不适合直接作为本讲来源 |
| 国内正式考试 | 已审查 | 可用于阶段复测；本次 Builder 更强调条件充分性和反例能力 |

## 6. 三种角色

- `Diagnostic`：B = −1、E = 5 的6点等距冷启动；
- `Builder`：尺度、删条件、逆向构造、一般化；
- `Mastery`：损坏数轴综合恢复。