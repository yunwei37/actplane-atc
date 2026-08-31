# #479 English rebuttal working draft

工作稿，未提交。保留评审原话以便作者逐项修改。英文 Response 段共 815 whitespace words。问题、引文、表格和作者提示不是提交正文，不可整份粘贴；最终需合并并用 HotCRP 计数，硬上限 1000 words。证据/待核验/承诺见 analysis.md。

| Rev | Overall | Confidence/Notes | Key concerns | Rebuttal goal |
| --- | --- | --- | --- | --- |
| A | 3 weak accept | expertise3 | 范围/生成/测试pass | 巩固支持 |
| B | R1 2 weak reject | 未单列expertise | 循环信任/over-taint | 明确信任边界 |
| C | 2 weak reject | expertise4 | 样本/DSL/保证 | 争取转支持 |
| D | 1 reject | expertise3 | IFC/指标/基线 | 回应技术blocker |

## Q1. How is policy generation trusted when the executing agent may be compromised? (B)

**B:** "AgPlane assumes that the active agent is untrusted and might be subject to prompt injection or behavioral drift."

**Response:** The executing agent cannot modify the higher-authority policy installed before it starts (§4.1). A trusted operator or separate generator supplies that policy, whereas runtime self-rules provide assistance under a cooperative-but-fallible model and may be ineffective if their author is compromised. Earlier generation alone does not establish trust: correct policy construction and protected installation remain assumptions, and enforcing an incomplete policy cannot recover omitted intent. Thus the compiler-outside-TCB claim cannot cover higher-authority policy construction and loading.

## Q2. What exactly is guaranteed, and is enforcement merely probabilistic? (C)

**C:** "It seems that AgPlane does not provide a hard guanrantee that a certain policy would be followed."

**Response:** Given installed rules, checks at configured OS hooks are deterministic, and lower-authority updates cannot weaken inherited constraints (§§4.1,4.4). However, only block provides synchronous pre-operation denial; kill acts after an observed operation, and notify only reports. The guarantee is therefore conditional on concrete rule coverage, effect choice, and monitored hooks, not on recognizing every semantic equivalent or enforcing arbitrary natural-language intent.

## Q3. How is the .env policy expressed, and what do labels and the DSL mean? (D)

**D:** "How do you express the .env policy in the DSL?"

**Response:** Using Appendix A's grammar, the policy is: `source SECRET = file "**/.env"` followed by `rule no-exfil: block connect endpoint "*" if SECRET`. SECRET originates at the file, while `if AGENT` in Figure 8 instead selects processes carrying agent provenance. The language composes source/sink predicates, Boolean label expressions, lineage and freshness gates; §5 implements 64-bit labels and 128 concurrent rules, not unrestricted semantic or file-content reasoning.

## Q4. How do indirect flows propagate, and does a sensitive read over-taint the session? (D)

**D:** "Does the entire session/context get tainted?"

**Response:** Section 4.3 propagates labels along observed file-read, process-fork, and file-write edges, so a labeled read can taint a process, an intermediate file it writes, and a later reader. This is conservative object-level provenance, not byte-level inspection of what the model copied or deduced. Cross-prompt coverage requires continuous observed flow within retained enforcement state; sharing an LLM conversation alone does not establish that continuity. Later unrelated connections from a tainted process can also be denied, so process isolation mitigates but does not eliminate over-tainting.

## Q5. Do labels survive separate sessions or reboot, and can the agent declassify them? (D)

**D:** "What if these steps were executed over two different sessions or after a reboot in the middle?"

**Response:** The submitted evaluation does not establish durable label preservation across independent sessions or reboot. Section 4.3 reserves declassification to the rule's authority and forbids a child from clearing inherited safety labels. Appendix A exposes `declassify L by exec G`, an authority-approved label-release gate, not verification that G sanitized the data. Section 6.2 reports no declassify/endorse use in the corpus, so it supplies no measured evidence that these transforms resolve long-session over-tainting.

## Q6. Why does feedback increase false positives when the kernel rules are identical? (D)

**D:** "The enforcement and policy are the same in both cases, so why would the kernel block an action in AgPlane that it did not block in the OPAQUE case?"

**Response:** Table 2 evaluates final trajectories, not kernel verdicts: Appendix B counts wrongful reporting or discouragement as FP, while violation awareness can count as TP without task completion. Feedback itself can therefore change the measured labels. Section 6.3 attributes 17/18 FPs to overbroad translations, but alternative-path completion alone does not justify counting an identical wrongful block as TN. Without that per-trace distinction, the aggregate results establish neither a kernel false-positive rate nor a safe-task-completion rate.

## Q7. What do the remaining failures say about translation, expressiveness, and coverage? (D)

**D:** "To what extent is this measuring the quality of the translation, the expressivity of the DSL (or the friendliness of a DSL for an agent), or the enforcement design itself?"

**Response:** RQ2 deliberately measures the combined translation, enforcement, feedback, and agent-response pipeline (§6.3), rather than isolating those error rates. Narrow translations miss violations and broad ones misclassify permitted actions; §6.6 additionally identifies semantic harms, unsafe content, and service-side effects beyond current hooks. The reported correction of 26/28 failed traces uses their failure evidence to revise policies, so it is a repair result, not independent held-out generalization.

## Q8. What do the baselines establish about AgPlane's contribution? (D)

**D:** "AgPlane-OPAQUE is similarly something you created, and the reader has no reason to consider it representative of IFC approaches in general"

**Response:** OPAQUE is a same-engine feedback ablation, not a representative implementation of every IFC design; prompt-filter and tool-regex are configured reference layers, not independent research-system implementations. On the 190-trace benchmark, full AgPlane reaches 75.8% DCR versus 53.7% for OPAQUE and 48.9% for the evaluated FIDES configuration (Table 2). These comparisons support combining below-tool enforcement with actionable feedback on this workload, not superiority over all policy systems or novelty of label propagation itself.

## Q9. Is there evidence beyond coding repositories? (A)

**A:** "Policy enforcement for coding use cases is a very restricted subset of cases where policy enforcement is needed"

**Response:** Yes: §6.6 runs all 361 OpenAgentSafety workplace/personal-assistant tasks in OpenHands, independently of the instruction-file corpus. Description-only policy generation produces 303 nontrivial policies and 58 no-ops, and enforcement prevents 78 of the 106 baseline-unsafe outcomes, leaving 28. This is existing non-coding evidence, not universal safety: content-only and service-side effects remain limitations, and benign-operation activation is also reported.

## Q10. How are rules generated, and was runtime self-restriction actually exercised? (A)

**A:** "The paper doesn't really explore how the AgPlane's DSL is generated by natural language instructions, other than LLM magic."

**Response:** Section 6.2 gives the generator the directive, repository context, and DSL reference, followed by compilation and independent checks; all 607 eligible directives compile, with two rules requiring retry, but compilation alone is not semantic validation. Section 6.5 exercises 110 runtime deltas across 21 selected OctoBench tasks, with user-query, implementation/test, and compliance rewards improving by 9.9, 9.7, and 2.8 points. These are scoped task results, not adversarial certification of self-authored policy.

## Q11. Can the gate require tests to pass after the latest edit? (A)

**A:** "However, a more interesting constraint, "only commit if all the tests pass" is one that doesn't appear to be easily implemented by AgPlane."

**Response:** Figure 8 already uses `after exec "go" "test" exits 0 since write "**/*.go"`, and §5 arms exit-qualified gates only after the specified normal exit status. This distinguishes successful execution from merely invoking tests and invalidates the gate after a matching edit. It trusts the selected test command's coverage and exit status, not the semantic completeness of the tests.

## Q12. How representative is the corpus, and is DSL coverage held out? (C)

**C:** "Please explain why the applications studied in the empirical study are representative."

**Response:** CLAUDE.md and AGENTS.md expose repository-local agent instructions, so selecting them deliberately favors coding policies (§2). The 64-repository snapshot is a purposive study, not a representative census of all agent applications (§3.1). Its unit is the directive, not agents-per-system, and the 607-rule coverage experiment reuses that corpus rather than a held-out set. External OctoBench and OpenAgentSafety experiments provide separate task evidence but do not remove that sampling limitation.

## 作者核对提示（不属于回复正文）

此稿未承诺任何新实验、论文修改或公开材料。Q6 的 17/18 FP 解释与 Appendix B 的判定规则仍需逐 trace 核对；Q1 需作者确认高权限 policy compiler/loader 的实际信任边界。引用为所示评审的逐字摘句，完整评审保留在本地私有记录，未随本次 Git 提交。
