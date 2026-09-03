# #479 English rebuttal working draft

工作稿，未提交。保留评审原话以便作者逐项修改。英文 Response 段共 896 whitespace words。问题、引文、表格和作者提示不是提交正文，不可整份粘贴；最终需合并并用 HotCRP 计数，硬上限 1000 words。证据/待核验/承诺见 analysis.md。

| Rev | Overall | Confidence/Notes | Key concerns | Rebuttal goal |
| --- | --- | --- | --- | --- |
| A | 3 weak accept | expertise3 | 范围/生成/测试pass | 巩固支持 |
| B | R1 2 weak reject | 未单列expertise | 循环信任/over-taint | 明确信任边界 |
| C | 2 weak reject | expertise4 | 样本/DSL/保证 | 争取转支持 |
| D | 1 reject | expertise3 | IFC/指标/基线 | 回应技术blocker |

## Q1. How is policy generation trusted when the executing agent may be compromised? (B)

**B:** "AgPlane assumes that the active agent is untrusted and might be subject to prompt injection or behavioral drift."

**Response:** The executing agent is not trusted to generate its own mandatory higher-authority policy. For a safety claim, the submitted higher-authority policy and its protected installation must be trusted, and it may be prepared by a human or separate generator before the executing agent starts (§4.1). Runtime self-rules instead assume a cooperative-but-fallible author and may fail if that author is compromised. Enforcement cannot recover intent omitted from the installed policy.

## Q2. What exactly is guaranteed, and is enforcement merely probabilistic? (C)

**C:** "It seems that AgPlane does not provide a hard guanrantee that a certain policy would be followed."

**Response:** Enforcement is deterministic for an installed rule at a configured OS hook, but it does not guarantee arbitrary natural-language intent. Lower-authority updates cannot weaken inherited constraints (§§4.1,4.4), and only block provides synchronous pre-operation denial. Kill acts after an observed operation, while notify only reports. The supported guarantee is therefore conditional on rule coverage, effect choice, and monitored hooks.

## Q3. How is the .env policy expressed, and what do labels and the DSL mean? (D)

**D:** "How do you express the .env policy in the DSL?"

**Response:** Appendix A expresses the policy as `source SECRET = file "**/.env"` followed by `rule no-exfil: block connect endpoint "*" if SECRET`. SECRET is intrinsic to matching file objects and propagates to readers (§4.3), while `if AGENT` in Figure 8 selects processes carrying agent provenance. The grammar composes source and sink predicates, Boolean label expressions, lineage gates, and freshness gates. Section 5 implements 64-bit labels and 128 concurrent rules, so the DSL does not provide unrestricted semantic or file-content reasoning.

## Q4. How do indirect flows propagate, and does a sensitive read over-taint the session? (D)

**D:** "Does the entire session/context get tainted?"

**Response:** Labels propagate across the observed file-read, process-fork, and file-write edges described in §4.3. Thus a labeled read can taint a process, an intermediate file it writes, and a later reader, but this is object-level provenance rather than byte-level inspection of what the model copied or deduced. Across prompts, coverage requires continuous observed flow within retained enforcement state, since a shared LLM conversation alone does not establish continuity. Unrelated later connections from a tainted process may therefore be denied, and process isolation mitigates but does not eliminate over-tainting.

## Q5. Do labels survive separate sessions or reboot, and can the agent declassify them? (D)

**D:** "What if these steps were executed over two different sessions or after a reboot in the middle?"

**Response:** The submitted evaluation does not establish label preservation across independent sessions or reboot. The actual release mechanism is Appendix A's `declassify L by exec G`, which permits the rule's authority to clear label L when execution passes the approved gate G, while a child cannot clear inherited safety labels (§4.3). The gate does not verify that G sanitized the data, and it does not establish a durable reset of all related state. Because §6.2 reports no declassify/endorse use in the corpus, the evaluation does not show that these transforms resolve long-session over-tainting.

## Q6. Why does feedback increase false positives when the kernel rules are identical? (D)

**D:** "The enforcement and policy are the same in both cases, so why would the kernel block an action in AgPlane that it did not block in the OPAQUE case?"

**Response:** The kernel does not block differently: identical monitored events under identical rules receive the same verdict. Table 2 instead labels end-to-end trajectories, and Appendix B counts visible wrongful reporting or discouragement as FP while allowing violation awareness to count as TP without task completion. Feedback can therefore change a trajectory label even when the kernel rule is unchanged. Section 6.3 attributes 17/18 FPs to overbroad translations, but the aggregate account still requires per-trace separation of feedback-only interventions from wrongful denials, so it should not be read as a kernel false-positive rate.

## Q7. What do the remaining failures say about translation, expressiveness, and coverage? (D)

**D:** "To what extent is this measuring the quality of the translation, the expressivity of the DSL (or the friendliness of a DSL for an agent), or the enforcement design itself?"

**Response:** RQ2 measures the combined translation, enforcement, feedback, and agent-response pipeline rather than isolating each component (§6.3). Narrow translations miss violations, broad translations misclassify permitted actions, and §6.6 identifies semantic harms, unsafe content, and service-side effects beyond current hooks. The reported correction of 26/28 failed traces uses their failure evidence to revise policies. It is therefore a repair result, not independent held-out generalization.

## Q8. What do the baselines establish about AgPlane's contribution? (D)

**D:** "AgPlane-OPAQUE is similarly something you created, and the reader has no reason to consider it representative of IFC approaches in general"

**Response:** The prompt-filter, tool-regex, and OPAQUE baselines are diagnostic baselines, not representative independent implementations of all prior approaches. OPAQUE isolates feedback using the same engine, while prompt-filter and tool-regex are configured reference layers. On the 190-trace benchmark, full AgPlane reaches 75.8% DCR versus 53.7% for OPAQUE and 48.9% for the evaluated FIDES configuration (Table 2). These results support below-tool enforcement with actionable feedback on this workload, not superiority over all policy systems or novelty of label propagation itself.

## Q9. Is there evidence beyond coding repositories? (A)

**A:** "Policy enforcement for coding use cases is a very restricted subset of cases where policy enforcement is needed"

**Response:** Yes, §6.6 provides non-coding evidence from all 361 OpenAgentSafety workplace and personal-assistant tasks in OpenHands, independently of the instruction-file corpus. Description-only generation produces 303 nontrivial policies and 58 no-ops, and enforcement prevents 78 of the 106 baseline-unsafe outcomes, leaving 28. This does not establish universal safety because content-only and service-side effects remain outside the demonstrated scope, and benign-operation activation is also reported.

## Q10. How are rules generated, and was runtime self-restriction actually exercised? (A)

**A:** "The paper doesn't really explore how the AgPlane's DSL is generated by natural language instructions, other than LLM magic."

**Response:** Rules are generated from the directive, repository context, and DSL reference, then compiled and independently checked (§6.2). All 607 eligible directives compile, with two rules requiring retry, although compilation is not semantic validation. Section 6.5 exercises 110 runtime deltas across 21 selected OctoBench tasks, with user-query, implementation/test, and compliance rewards improving by 9.9, 9.7, and 2.8 points. These scoped results do not provide adversarial certification of self-authored policy.

## Q11. Can the gate require tests to pass after the latest edit? (A)

**A:** "However, a more interesting constraint, "only commit if all the tests pass" is one that doesn't appear to be easily implemented by AgPlane."

**Response:** Yes, the gate can require a successful test command after the latest matching edit. Figure 8 uses `after exec "go" "test" exits 0 since write "**/*.go"`, and §5 arms exit-qualified gates only after the specified normal exit status. A matching edit invalidates the gate, which distinguishes successful execution from merely invoking tests. The guarantee trusts the selected command's coverage and exit status, not the semantic completeness of the tests.

## Q12. How representative is the corpus, and is DSL coverage held out? (C)

**C:** "Please explain why the applications studied in the empirical study are representative."

**Response:** The corpus represents popular coding-project instruction files, not all agent applications. CLAUDE.md and AGENTS.md expose repository-local agent instructions (§2), and the 64-repository snapshot is a purposive study rather than a representative census (§3.1). Its unit is the directive, not agents per system, and the 607-rule coverage experiment reuses that corpus rather than a held-out set. OctoBench and OpenAgentSafety provide separate task evidence, but they do not remove this sampling limitation.

## 作者核对提示（不属于回复正文）

需作者核对两点：Q1 所述高权限 policy 构造与受保护加载是否准确反映实际信任边界；Q6 的 17/18 FP 解释是否能与 Appendix B 的判定规则逐 trace 对齐。
