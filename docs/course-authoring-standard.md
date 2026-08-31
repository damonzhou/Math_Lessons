# 课程统一编写与质量审核标准｜v1.4 工作版

> 当前规范以 `docs/standards/CURRENT.md` 为最高版本入口。

课程目标：

$$
\boxed{\text{概念完全理解}\rightarrow\text{规范解决问题}\rightarrow\text{真实应用}\rightarrow\text{陌生问题迁移}}
$$

---

# 一、主线与边界

1. 教育部课标决定学段目标；
2. 人教版教材/教师用书决定 Core 顺序和概念边界；
3. Advanced/Olympiad/Final Challenge 主要依赖本讲及此前已学知识；
4. 超前内容只能延后、适龄改编或标为 EXTENSION。

---

# 二、四轨体系

- **Core**：定义、性质、规范表达、教材典型模型、概念边界；
- **Advanced**：逆向、条件变化、综合、分类、整体、数形结合、校内高档题；
- **Olympiad**：数论、代数结构、组合、几何、构造、不变量、极端思想；
- **Informatics**：整数表示、offset、模运算、递推、组合、图论和算法证明。

---

# 三、概念深度

核心概念必须尽量回答：

- 为什么需要；
- 正式定义；
- 正例/反例/边界；
- 与相近概念区别；
- 表示形式与数学对象是否需要区分；
- 不同应用场景中的语义；
- 能否用自己的话解释；
- 能否迁移到陌生场景。

Core 最终稳定达到“会解释”，重要概念逐步达到“会迁移”。

---

# 四、应用场景

应用不能只换故事背景。应尽量覆盖不同数学语义：

- 状态；
- 位置/方向；
- 变化量；
- 偏差/误差；
- 比例/测量；
- 数据；
- 科学/工程；
- 金融/生活；
- 程序/算法。

---

# 五、例题体系

例题应形成：

```text
直接应用
→ 逆向读取
→ 概念辨析
→ 条件变化
→ 综合应用
→ 方法发现
→ 真实应用
→ 陌生迁移
```

重要例题说明突破口、关键条件、错误路径、检查点和可推广结构。

---

# 六、权威题源

课程依据和真题认证必须回到一手来源：

- 教育部、人教社；
- 正式考试原卷/教育主管部门/考试机构；
- MAA AMC、IMO 官方站、CEMC、UKMT；
- 中国数学会 CMO、全国高中数学联赛等正式赛事；
- 可靠正式出版物。

新闻、自媒体、商业题库转载、论坛和搜索摘要不得作为课程依据。

题源标签：

- `TEXTBOOK-MODEL`
- `SOURCE`
- `ADAPTED`
- `SYNTHESIS`
- `DESIGNED`

赛事选择按：

$$
\text{教学匹配度}+\text{权威性}+\text{当前可解性}+\text{思维价值}
$$

而不是赛事名气。

---

# 七、Po-Shen Loh 方法

参考：陌生题先独立探索、少机械重复、分级 hints、多方法、解后推广。

仅作为教学方法论，不作为题源认证。

---

# 八、做题习惯

统一流程：

$$
\boxed{\text{提取条件}\rightarrow\text{明确所求}\rightarrow\text{建立关系}\rightarrow\text{执行检查}\rightarrow\text{回代核对}}
$$

每讲明确 H1～H10 中的重点纠偏，并按需要设计 `DIAGNOSTIC-Hx`。

---

# 九、Final Challenge

必须：

1. 当前知识可解；
2. 题面不泄露方法；
3. 有真正突破口；
4. 优先有权威题源/结构；
5. Hint 1 → Hint 2 → Hint 3；
6. 解后一般化/第二方法/条件变化；
7. 真正服务本讲核心。

好题若主要训练下一讲，应移动到下一讲。

---

# 十、文档结构

```text
module/
├── XX-lesson.md
├── exercises/XX-lesson-homework.md
├── solutions/XX-lesson-classroom.md
├── solutions/XX-lesson-homework.md
├── sources/XX-lesson-provenance.md
├── reviews/XX-lesson-release-review-vX.Y.md
└── diagnostics/
```

当堂训练留主课；答案和课后题分离。

---

# 十一、强制 Release Review

新 Lesson 首次发布、重大修改或迁移新标准时，必须 Review：

- R1 课程逻辑；
- R2 课标/教材覆盖；
- R3 概念深度；
- R4 知识边界；
- R5 应用场景；
- R6 例题/训练梯度；
- R7 题源质量；
- R8 错误/习惯；
- R9 Final Challenge；
- R10 前后衔接。

结论：`PASS / PASS WITH MINOR FIXES / REVISE / BLOCK`。

只有完成修改并达到 PASS 才能标记课程完成。

---

# 十二、发布前硬检查

- [ ] 当前标准已读取；
- [ ] Core 覆盖无遗漏；
- [ ] 概念无内部逻辑冲突；
- [ ] 应用真正服务概念；
- [ ] 例题有梯度；
- [ ] 题源来自权威一手资料；
- [ ] AMC/IMO/CMO 等赛事题未因名气而超纲；
- [ ] 原创题有必要性；
- [ ] H 标签明确；
- [ ] Final Challenge 贴本讲核心；
- [ ] 前后课程不重复/断层；
- [ ] Release Review 已 PASS。
