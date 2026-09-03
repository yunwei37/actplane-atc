# AgPlane #479：rebuttal 分析

## 工作边界与来源

2026-08-31；ATC 2026；HotCRP single-document response；硬上限 1000 words；截止 2026-09-03 04:59:59 America/Los_Angeles (=11:59:59 UTC)。初轮只起草；本轮追加授权仅为 Git 提交，不保存或提交 HotCRP response，不修改论文或代码。

使用 academic-writing-skills/domain-skills/rebuttal/SKILL.md 及 references/workflow.md。输出只有本分析及 rebuttal.md；问题、证据、承诺、审计都在本文件。评审先于论文进入上下文，因此不声称完成 blind review；不执行 iter-review-critique 的盲审循环。

2026-08-31，作者在获知 actplane-atc 为公开仓库且草稿含评审引文后，明确授权 commit/push。本文件与 rebuttal.md 随该授权提交到论文仓库，完整评审原文 rebuttal/reviews.txt 现已提交到本公开仓库。精确投稿 PDF 由已登录 Chrome 下载并核对 HotCRP checksum。读远端源码只作证据，不重跑实验、不启动服务、不编译代码。


投稿: https://atc26.hotcrp.com/u/1/paper/479
PDF: HotCRP 精确投稿版本（文件名 atc26-paper479.pdf，使用下述 SHA256 标识；PDF 不随本次提交）。
SHA256: 326acc27fc8fe372c6f92d6795e5a7595d8fc047334d22913d44c9097c3a4d16
lab 源码: ActPlane checkout；论文: docs/papers/。
远端 main.pdf SHA256 为 12c88cd144545e00cb5ae9964aa74e6694f09f1dd76f67b26a072f8ea99dc091，与投稿不同，禁止把当前源码或文稿直接当成投稿版本。

## 评审格局与策略

| Reviewer | 分数 | Expertise | 立场/目标 |
| --- | --- | --- | --- |
| A | Overall 3 Weak accept | 3 Mild | 最可能 champion；用已有非 coding 实验与 tests-pass 回答巩固 |
| B | R1 2 Weak reject | 未显示独立 expertise | 关键 swing；解释预装高权限策略与低权限自限制不同 |
| C | Overall 2 Weak reject | 4 Knowledgeable | 关键 swing；解释确定性语义、实际 DSL 能力、外部基准 |
| D | Overall 1 Reject | 3 Mild | 最大 blocker；IFC 生命周期、指标与基线诚实解耦 |

粗略主观判断 20%-35%，不是统计预测。至少需要 B/C 中一位向支持移动，并让 D 接受安全与证据边界。优先顺序是威胁模型、IFC、指标，然后保护 A 的支持。不要写成逐一反驳；最大的现成筹码是 §6.6 的 361 个 OpenAgentSafety 任务，不是再许诺补实验。

## Concern board：逐项覆盖

全为 initial round。critical/major 须在 Q1-Q12 中有锚点；answered 指草稿回答问题，不表示已补齐缺失实验。

| issue_id / reviewer | concern / type | severity | stance / priority | mode / evidence | draft / status |
| --- | --- | --- | --- | --- | --- |
| B-C1; C-C3; D-C1 | 受攻击 agent 自己产策略的循环信任；谁可信、威胁从哪里来 | critical | swing / pivotal | assumption-hierarchy; paper §4.1,4.4,6.6 | Q1 / answered |
| D-C2 | 同一个还是两个 agent，self-restriction 是否真被用 | major | negative / pivotal | direct-clarification; §6.5 110 deltas/21 tasks | Q1,Q10 / answered |
| C-C6; D-C3 | 是否仅提高概率，覆盖与 hard guarantee 的准确含义 | critical | swing / pivotal | narrow-concession; §4.1 effects + hook scope | Q2 / answered |
| D-Q1 | .env DSL 如何写 | major | negative / pivotal | paper Appendix A + current rule-language.md:246-255 | Q3 / answered, connect scope only |
| D-Q2a | 跨 prompt、file intermediary、re-read、network 的 label 路径 | critical | negative / pivotal | §4.3 + current runtime source, not exact submission | Q4 / answered with observed-flow limit |
| D-Q2b; B-C2 | 整 session 被污染，over-tainting | major | negative / pivotal | narrow-concession; §4.3 | Q4 / answered |
| D-Q3 | 两 session / reboot 持续性 | critical | negative / pivotal | future-work-boundary; paper no persistence evidence | Q5 / answered with limitation |
| D-C4 | declassify 权限/API/是否能清 inherited label | major | negative / pivotal | §4.3,6.2, Appendix A + current code | Q5 / answered, persistence unestablished |
| D-C5 | Figure 8 的 if AGENT、sources 与 gates | major | negative / pivotal | §4.2 + Appendix A | Q3 / answered |
| D-C6 | feedback 为什么使相同 kernel 的 FP 上升 | critical | negative / pivotal | §6.3 Table2 p10 17/18 vs AppendixB | Q6 / limitation stated, per-trace reconciliation open |
| D-C7 | TP/FN 是否 kernel soundness、policy intent ground truth、翻译/执行/表达能力如何拆分 | critical | negative / pivotal | §6.3 + AppendixB end-to-end awareness metric | Q6,Q7 / answered |
| D-C8; B-C3 | prompt/regex 自制弱基线，OPAQUE 不是一般 IFC | major | negative / pivotal | narrow-concession; §6.3 | Q8 / answered |
| D-C9 | novelty 与 prior IFC 的区别 | major | negative / pivotal | structural-distinction; §4,7; avoid unverified superiority | Q8 / answered |
| A-C1; META-C1 | 仅 coding？personal assistant、email、financial task 多样性 | critical | positive / pivotal | grounded-evidence; §6.6 361/303/58/106/78/28 | Q9 / answered |
| A-C2; META-C2 | NL → DSL 具体输入、生成、编译重试、验证流程 | major | positive / pivotal | §6.2; §6.3 separate translator; §6.6 generator | Q10 / answered |
| A-C3 | tests run vs tests all pass、task-level context | major | positive / pivotal | Fig8 exits0 since write; §5 exit tracepoint | Q11 / answered |
| C-Q1; C-C1 | CLAUDE/AGENTS 文件筛选、64 repo、时间与选择偏差 | major | swing / pivotal | narrow-concession; §3.1 | Q12 / answered |
| C-C2 | project/task diversity 和 agent 数量是否测过 | major | swing / pivotal | §3 measures statements not agent populations | Q12 / answered |
| C-C4 | 正式 grammar、表达空间大小 | major | swing / pivotal | §4.2; AppA; 64 label bits/128 rules §5 | Q3 / answered |
| C-C5 | 同 corpus 评估偏差/holdout | major | swing / pivotal | §6.2 not holdout; §6.5/6.6 external tasks | Q9,Q12 / answered |
| C-C7 | coding gain 较小，机制是否更强 | major | swing / pivotal | §6.5 9.9/9.7/2.8 points not universal | Q10 / answered |
| META-C3 | 禁止承诺新数字/实验，现有数据怎么支持 | critical | all / pivotal | reuse paper only, no commitments | all / answered |

## 证据与可用回应

- §4.1 高权限策略在执行前加载且 agent 无写权限。不能说“先生成就自然可信”；安全依赖生成过程、输入和装载路径可信，错误 higher-authority blob 不会自动被 IFC 修复。
- §4.1 block 是同步 pre-operation，kill 是 post-operation，notify 只是观察。不可用 kill 的结果宣称绝对 pre-effect no-violation guarantee。
- §4.3 明确 object granularity union；不能吹成字节级/LLM 意图跟踪。跨 prompt 只在同 monitored state 内有效，reboot durability 未证明。
- Appendix A 有 surface grammar，不等于完整 PL soundness theorem。64-bit labels/128 concurrent rules 是当前实现界限，不是所有自然语言策略皆可表达。
- §6.2 607 = 392 per-event +215 cross-event；不是 83% 的所有 system-observable directives。内容检查类不在内。编译通过也不等于语义正确。
- §6.3 Table2：AgPlane TP86 TN58 FP18 FN28，DCR75.8%；opaque TP27 TN75 FP1 FN87，DCR53.7%。AppendixB 允许 report/notify awareness 算 TP，不要求完成任务，绝不能称 86 条全部安全执行成功。
- §6.3 p10 将 17/18 FPs 归于过宽规则，并说 opaque 同规则经替代路径完成被判 TN；但 Appendix B 仍把 wrongful block 算 FP，之后成功不自动撤销 FP。两处存在尚待逐 trace 对齐的解释缺口。反馈/steering 可以改变 outcome label，但不能借此声称相同 wrongful block 已合理变为 TN。
- §6.3 revising 28 FN ->26 recovered 是用失败样本再修规则，不能包装成独立 holdout 的94.7%泛化安全率。
- §6.5 21/217 OctoBench 子集；110 runtime deltas；奖励改善9.9/9.7/2.8 points；selection boundary 必须保留。
- §6.6 所有361任务，303非空策略/58no-op，baseline106 unsafe中78 prevented/28 unsafe；不得以361作prevention分母。58 no-op 以及服务侧/语义/内容失败说明边界；16% baseline-safe activation 不是严格可比 false-positive 率。

## 草稿安排

Q1 信任；Q2 保证；Q3 DSL；Q4 taint路径；Q5 persistence/declassification；Q6 confusion matrix；Q7 residual errors；Q8 baselines/contribution；Q9 非coding；Q10生成/自限制；Q11测试成功；Q12代表性/holdout。
问题与原话保留完整，Response 段组成约900-1000词正文。整份工作稿含引文会超1000，不能整份粘贴；只提取Response再人工合并。

## Verification checklist

- [x] 精确投稿全文16页、评审A-D及汇总已读。
- [x] Fig8 图像检查确认 exits 0；Table2/AppendixB指标文本已核对。
- [x] 有界核对当前文件label共享/declassification；当前代码不同于投稿，reboot durability 仍未建立。
- [x] 独立 adversarial review；结论 needs revision，已按下述修正，实证缺口未伪装成通过。
- [x] Round1 coverage/facts、Round2 commitments/overclaims、Round3 language/count；是工作稿审计，不是提交批准。

## Commitment ledger

already-done: 本次分析与草稿，不是论文改动。
approved-for-rebuttal: 无。
future-work-only: broader benchmarks、durable labels、更多独立baseline，不作承诺。
needs-user-input: 最终策略/文字确认与任何提交动作。

## Adversarial review 与三轮记录

2026-08-31 独立子代理 audit_agplane 完成投稿、评审、远端源码和草稿审查，首轮结论 needs revision。已修正 Q4 跨 prompt 连续性、Q5 实际 declassification 语法、Q6 FP 内部不一致、Q8 自建基线范围、Q12 文件选择偏差，并删除跨论文混入的提示。

当前源码检查范围（仅解释实现，不反推投稿版本）：

- bpf/taint_engine.bpf.h:263-298、423-428、689-699、1004-1023、1720-1801：session/file/process 状态与读写 label union。一个 LLM 对话不是自动全量 taint 跟踪；current pipe/socketpair 支持不能当作投稿保证。
- bpf/taint_engine.bpf.h:1518-1534、bpf/capability.bpf.h:124-135,171-195,369-378：authority-approved gate 清执行进程 label，不验证 redactor 实际净化数据，也不等于清 file/session 全部状态；child 无权清 inherited labels。
- bpf/src/lib.rs:1887-1925,2038-2057：可选 pinned engine 不证明独立 session/reboot 持久性。
- 高权限 blob 的构造/验证/装载必须可信；“compiler/runner outside TCB”只能在相应低权限边界内理解，待作者核对论文原句。

Round 1（覆盖与事实）：12 问对应 concern board；保留 12 条评审逐字引文；重新读 §6.2 确认是“两条规则需 retry”，不是限两次尝试；Fig8/Table2/AppendixB 数字和语义均按投稿核对。

Round 2（过度声称与承诺）：去掉整会话自动 taint、持久化、绝对安全和 FP 已解决的暗示；保留 26/28 为 failed-trace repair，非 held-out generalization；无新增实验/公开/改稿承诺。

Round 3（写作与词数）：每个实质 Response 为 3-4 句，无写作指令混入英文回应；最终计数见 rebuttal.md，未进入 HotCRP 输入框。最终状态 draft-ready / not submission-ready；Q6 逐 trace 解释和高权限生成边界仍待作者确认。

2026-09-02 语言与直接性修订：Q1-Q12 的 Response 均改为 direct-answer-first 结构，评审引文与数字保持不变，并落实 Q1/Q6/Q8/Q12 的直接性修正；最终作者说明已纠正，当前 Response 按空白分隔计数为 896 words。

## Follow-up log

当前只见 @A1 汇总，无已提交作者 response。
