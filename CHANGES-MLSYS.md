# MLSys 2027 revision: change log

Scope: anonymized AgPlane submission (OpenReview #369), revised from the ATC '26 version.
Nothing is committed. Build both PDFs with:

```
latexmk -pdf -interaction=nonstopmode appendix.tex
latexmk -pdf -interaction=nonstopmode main.tex
```

## Result of the revision

- `main.pdf`: 15 pages. The body (abstract through Section 7, Conclusion) ends at the bottom of **page 10**. References start at the top of **page 11**. The unnumbered "AI Usage Disclosure" follows the references on page 15.
- `appendix.pdf`: 11 pages, a standalone mlsys2025 document titled "Supplementary Material for AgPlane: ..." (Appendices A to L, with figures numbered S1, S2, ... and tables numbered S1, S2, ...).
- No Type 3 fonts in either PDF (`pdffonts`). The 8 matplotlib figures with Type 3 fonts were replaced in place by the supervisor; this revision did not regenerate or edit any existing figure file.
- PDF text and decoded streams contain no "ActPlane", "eunomia", "yunwei", "ucsc", "Santa Cruz", author names or `PTEX.FileName`. The only self-citations are AgentSight and Crab, cited in the third person.

## Principle followed

Every experiment, number and finding from the ATC version is still present, either in the body or in the supplementary PDF. New results were added next to the old ones. Space was recovered by moving figures, tables and secondary detail into the supplement and by tightening prose.

## Format work

- **Appendix split.** `\input{sections/06-appendix}` was removed from `main.tex`. The new `appendix.tex` inputs `sections/06-appendix.tex` (unchanged: A, grammar; B, judge prompt), the new `sections/07-supp-study.tex` (C to E), and the new `sections/08-supp-eval.tex` (F to L), and has its own bibliography.
- **Cross-references.** The main text refers to the supplement as "supplementary Appendix X", "supplementary Figure Sn" or "supplementary Table Sn". These are literal strings resolved once from `appendix.aux` (no `xr` dependency), so `main.tex` builds on its own. A comment in `main.tex` says to recheck them if the supplement is reordered. Current mapping: A grammar, B judge prompt, C original study, D expanded study, E trajectories, F RQ1, G translation across models, H RQ2, I RQ3/RQ4, J RQ5, K authority boundary, L benign utility.
- **AI Usage Disclosure.** Added as `\section*{AI Usage Disclosure}` after `\bibliography`, preceded by `% TODO(authors): confirm disclosure wording`. It covers coding agents (Codex, Claude Code) for orchestration, scripts and data processing; LLMs as experimental subjects and components; and AI-assisted editing.
- **References (`references.bib`).**
  - `qwen2025qwen3`: replaced "and others" with all 60 authors from the arXiv API record for 2505.09388.
  - New `terminalbench2` (arXiv 2601.11868, all 85 authors from the arXiv API), `anthropic2025srt` (Anthropic sandbox runtime), and `docker-seccomp` (Docker seccomp profiles).
  - No "and others" or "et al." remains in the file.
- **Anonymity.** Removed the commented-out GitHub URL of the public repository from the old commented abstract in `main.tex`. The `\mlsysauthor` and `\mlsysaffiliation` block in `main.tex` still holds the real names, affiliations and email for camera-ready. Review mode does not print it; the PDF shows "Anonymous Authors".
- `\pdfsuppressptexinfo=-1` is kept in `main.tex` and also set in `appendix.tex`.

## Changes by section

### Abstract (`main.tex`)
- **Added:** our own evidence for indirect paths (45.7% of writes to tracked project files are not named in the initiating tool call); the policy-authorship framing (an agent with task context declares policies before untrusted input is consumed, enforced above the executing agent); the replication on 325 repositories, the seven translating LLMs, the shipping sandbox baselines and the benign-utility benchmarks.
- **Reworded:** the key-insight sentence ("an agent that knows the task" replaces "the agent closest to the task").

### 1 Introduction
- **Added:**
  - the 325-repository replication numbers (53.0%, 76.4%, 80.1%) after the original 64/83/74%;
  - the trajectory evidence (11.8–33.9% indirect calls in 3,156 trajectories; 45.7% of tracked-file writes unnamed in 40 replays);
  - the reframed policy authorship (planner, parent or dedicated policy agent writes before untrusted input; loaded at higher authority; the executing agent may only add stricter rules);
  - the shipping-sandbox result (Codex 15/111, Docker 0/111, SRT 93/111 with 72/76 compliant denied).
- **Reworded:** the Figure 1 caption, to state the authorship model. The figure itself still labels the author "Worker Agent (closest to the task)"; see Remaining issues.
- **Tightened:**
  - the two design requirements merged into one paragraph;
  - the three-item contribution list folded into one sentence.

### 2 Motivation
- **Added:**
  - **Replication at scale** paragraph and **Table 1** (original vs. 325-repository automated replication with bootstrap intervals). It includes the calibration (type and topic κ 0.83/0.68; enforcement and context rescued by a dev/test split, test κ 0.69/0.68), an honest statement that the magnitudes differ, the exploratory noncoding slice (4,315 statements, 50.0% policies, 70.2% system-observable), and the limitations.
  - New **§2.3 Indirect Execution in Agent Trajectories**: static results (3,156 trajectories, 89,176 calls, 5 frameworks, 11.8–33.9% indirect, 71.5–100% of trajectories), dynamic results (40 replays; 45.7% (80/175) of tracked-file writes and 37.6% (56/149) of call–file pairs unnamed; 72.1% of execs unnamed), precision/recall of the static label (77.7%/50.3%), and the caveats. The pooled 98.9% write figure is not used in the body.
- **Moved to the supplement (Appendix C):**
  - Table 1 (representative statements S1–S8; now Table S1);
  - Figure "policy fraction per repository" (S1);
  - "policy ratio by topic" (S2);
  - "enforcement-level waterfall" (S3);
  - "enforcement profile by topic" (S4);
  - "context-requirement waterfall" (S5);
  - "context by enforcement level" (S6);
  - the three-step extraction and validation detail.
- **Kept in the body:** every number from Q1–Q3 and the three takeaways (shortened wording).
- **Removed:** the commented-out duplicate drafts in `02-motivation.tex` (comments only; no visible change).
- **Fixed:** a hard-coded "(Figure 2)" reference.
- **Tightened:** §2.1, the dataset paragraph, §2.4 and §2.5.

### 3 Design
- **Threat model:** rewritten around two roles (to answer reviewer B's circular trust and reviewer D's "one agent or two").
  - The *policy author* (planner, parent or dedicated policy agent with task context) writes before consuming untrusted input. The *executing agent* may be compromised.
  - The temporal trust boundary.
  - The executing agent may add only stricter rules.
  - The evaluation follows the split (RQ2 separate translator, RQ4 Codex policy agent for a sub-agent, RQ5 pre-execution generator).
  - An explicit statement that AgPlane does not make the author's rules correct.
  - The authority-boundary validation (7/7 on Linux 6.8), cited to Appendix K.
- **Reworded:**
  - The TCB sentence now says that the compiler and runner that produce higher-authority policy are trusted, and only the runtime-delta path is re-validated in kernel. It used to say that the userspace compiler and runner sit entirely outside the TCB.
  - The sentence "spawning a fresh subprocess clears inherited labels" was replaced with what the long-session experiment supports: labels attach to the reading lineage, and a sibling stays clean.
- **Added:**
  - what `if AGENT` means (reviewer D);
  - how the `.env` policy is written in the DSL and how a label flows through an intermediate file (reviewer D);
  - label lifetime (across prompts while the engine runs, not across reboots; the model context is not labeled);
  - the `declassify ... by exec` form and the fact that the sanitizer is not verified.
- **Tightened:**
  - the DSL and IFC prose;
  - the `pid -> domain` verbatim block replaced by the one-line formula `policy(D) = policy(parent(D)) + local(D)`.

### 4 Implementation
- **Tightened** only; no content removed.

### 5 Evaluation
- **RQ list:** now six RQs in one paragraph. RQ1 adds translation across models, RQ2 adds sandbox baselines, and the new RQ6 covers benign utility.
- **RQ1:**
  - Kept: the 607-policy GPT-5.5 compile result, cost and time.
  - Moved to Appendix F: the policy-structure and DSL-feature statistics (one summary sentence stays).
  - Added: **Translation across models**, with **Table 2** (7 models: compile @1/@3 on 607, detection, false trigger and F1 by kernel replay of the 190 traces; reference 0.773). It reports the F1-vs-always-trigger caveat (0.750), the 156/190 reference agreement, GLM-4.7-Flash's 323 access failures, and that this measures generality across translators, not held-out policies. Full table, method and figure are in Appendix G.
- **RQ2:**
  - Moved to Appendix H: the pipeline figure (S13) and the two-model DCR bar chart (S14). The DeepSeek 77.4% and κ numbers stay in the text.
  - Reworded:
    - "Agents can learn from failure, raising detection from 77.2% to 94.7% with one revision" now states that the rules were repaired with the same failed traces they are scored on, so this shows iterative refinement, not held-out accuracy.
    - "rules that are too broad … causing 17 of the 18 false positives" was replaced with the trace audit: 9 translation, 4 historical path lowering, 4 replay-harness helpers, 1 judge protocol (`rq2-fp-attribution.md`).
  - Added:
    - the explanation of why the opaque ablation has 1 FP and full AgPlane has 18 (14 hidden notifications counted as TN; the one opaque FP is a `kill`). This answers reviewer D.
    - **Shipping sandbox baselines** paragraph and **Table 4** (Codex workspace-write 15/111 and 6/76; SRT standalone defaults 93/111 and 72/76; SRT cwd-write analogue 33/111 and 1/76; Docker default 0/111 and 0/76). AgPlane rows are notify-mode detections (reference 80/114 with 13/76; GLM-4.5-Air 58/114 with 10/76), explicitly a different metric. Details, the per-family table and the figure are in Appendix H.
  - All five original systems, Table 3 (the confusion matrix) and the family heatmap are kept.
- **RQ3:**
  - Moved: the macro-overhead figure (S16) and the per-syscall latency table (S8) to Appendix I.
  - Kept in the text: every headline number (1.9%, 6.5%, 8.4%, 13.4 µs open, 26.3 µs reload, 176.4 µs).
- **RQ4:**
  - Moved: the OctoBench figure (S17) to Appendix I.
  - Reworded: it now states that the policy author (a Codex policy agent) is separate from the task-executing sub-agent.
  - All numbers are kept.
- **RQ5:**
  - Figure 5 is kept.
  - Moved: the failure-analysis detail to Appendix J (a summary sentence stays).
  - Added: the 18/18 live firing audit on Linux 6.8 (Appendix J, Table S9).
- **RQ6 (new): Benign Utility and Over-Tainting.** It answers reviewers B and D:
  - Terminal-Bench 2.0: 4/6, 6/6 and 4/6, with no IPv4 connections, so no enforcement effect;
  - network follow-up: 2/3 each, with false interventions 12/51 (broad) vs 1/67 (narrowed);
  - public replays: 2.85–2.92% (broad) vs 0 (narrowed);
  - long-session lineage growth: 1/5/20, a descendant 5, a sibling 0.
  - The section states that the samples are small and purposive, that narrowed sources missed one new private key, and that the trusted redaction gate and model-context propagation are untested. Details are in Appendix L.

### 6 Related Work
- **Added:** one sentence on shipping agent sandboxes (Codex, SRT) pointing to RQ2.
- **Tightened:** otherwise only tightened.

### 7 Conclusion
- **Added:** a sentence on the limits: guarantees are bounded by the policy author; faithful translation, source scoping and trusted declassification remain open.

## Supplementary material (`appendix.pdf`)

| Appx | Content | Status |
|---|---|---|
| A | Policy language grammar | unchanged (moved from the main PDF) |
| B | LLM-as-judge prompt | unchanged (moved from the main PDF) |
| C | Original study: Table S1 (examples), Figures S1–S6, extraction details | moved from §2 |
| D | Expanded study: selection, annotation, calibration (Table S2), rescue protocol, comparison with recovered labels, per-family and per-scope results (Table S3), noncoding slice, misclassification-corrected estimates, Figures S7–S9, limitations | new |
| E | Trajectories: sources, static classes (Table S4, Figure S10), dynamic replay method, tracked-file breakdown (Table S5), shell-profile sensitivity, Figure S11, limitations | new |
| F | RQ1 policy structure and DSL feature use | moved from §5.1 |
| G | Translation across models: method, replay, full Table S6 (compile on the sample and the corpus, per-family detection, cost), Figure S12, compiled-only F1, limitations | new |
| H | RQ2: pipeline (S13), two-model DCR (S14), FP attribution, sandbox configuration, oracle and fidelity, Table S7, Figure S15 | moved and new |
| I | RQ3 micro-latency (Table S8) and macro figure (S16); RQ4 OctoBench figure (S17) | moved |
| J | RQ5 failure analysis; OAS firing audit (Table S9) | moved and new |
| K | Policy authority boundary matrix (Table S10) | new |
| L | Benign utility: policies and coverage, Table S11, adjudications, Codex auth-source control, Figure S18, long-session label growth (Table S12) | new |

New figure files (copied unchanged, already TrueType) in `figures/`:

| File | Source |
|---|---|
| `scale_policy_fraction.pdf` | `corpus-scale/figures/empirical_rq1_policy_fraction.pdf` |
| `scale_enforcement_by_topic.pdf` | `corpus-scale/figures/empirical_rq3_enforcement_by_topic.pdf` |
| `scale_context_by_enforcement.pdf` | `corpus-scale/figures/empirical_rq4_context_by_enforcement.pdf` |
| `traj_indirect_execution.pdf` | `trajectory-indirect/indirect_execution.pdf` |
| `traj_dynamic_effects.pdf` | `trajectory-indirect/dynamic_effects.pdf` |
| `translation_models.pdf` | `translation-models/comparison.pdf` |
| `sandbox_baselines.pdf` | `sandbox-baselines/results/comparison.pdf` |
| `benign_utility.pdf` | `benign-utility/results/benign-utility.pdf` |

## Evidence sources for new numbers

All paths are relative to `ActPlane/docs/empirical-study/` on branch `experiments/mlsys27`.

| Topic | Source files |
|---|---|
| Replication | `corpus-scale/README.md`, `corpus-scale/summary.csv` |
| Trajectories | `trajectory-indirect/README.md` (static, dynamic, tracked-scope and confusion tables) |
| Translation | `translation-models/README.md` |
| Sandboxes | `sandbox-baselines/README.md`, `sandbox-baselines/results/comparison.csv` |
| Benign utility | `benign-utility/README.md`, `benign-utility/SUMMARY.md`, `benign-utility/benchmark/policies/{b,c}.dsl` |
| Authority boundary | `policy-authority-boundary-plan.md`, `results/policy-authority-boundary-vm/counts.tsv` |
| Firing audit | `openagentsafety-policy-firing-audit.md` |
| FP attribution | `rq2-fp-attribution.md`, `rq2-lowering-eval.md` |
| Long-session over-taint | `rq2-reviewer-audit-plan.md`, `results/long-session-overtaint-vm/{counts.tsv,policy.dsl}` |

`injection-bench/` is **not used**, as instructed: every condition shows 0% attack success and the failures are unexplained.

## Remaining issues for the authors

1. **Figure 1 artwork** still labels the policy writer "Worker Agent (closest to the task)". The caption now explains the authorship model, but the figure source is not in this repository, so the drawing was not changed.
2. **Disclosure wording** has a `TODO(authors)` marker.
3. **Cross-document numbers** ("Appendix K", "Figure S14", and so on) are literal. Recheck them if the supplement is reordered.
4. **Self-citations** remain for AgentSight (Zheng et al.) and Crab (Wu et al.). Both are cited in the third person; confirm this is acceptable.
5. **Paper numbers not re-derived:** pre-existing paper numbers (for example, RQ2's 94.7% after repair, 97.7% recovery, and the RQ3–RQ5 numbers) were kept as written. This revision did not re-derive them from artifacts.
6. **Recovered labels vs. paper:** recovering the original labels gives 79.7% of repositories with cross-event policies, against the rounded 81% stated in the paper. The body keeps 81%; Appendix D reports the discrepancy.
7. **Body length:** the body ends at the bottom of page 10 with only a few lines of slack, so any added text will push the conclusion onto page 11.
8. **Line endings:** edited `.tex` and `.bib` files were converted back to CRLF to match the checkout (`core.autocrlf=true`).
9. **New bib entries to confirm:**
   - `anthropic2025srt`: the year 2025 is assumed; the evidence lane records only version 0.0.81.
   - `docker-seccomp`: 2026 is the access year of a documentation page.
   - `terminalbench2`: cites the Terminal-Bench arXiv paper for the Terminal-Bench 2.0 tasks.
10. **Makefile:** the `Makefile` was not changed. Its `paper` target still builds only `main.pdf`, so build `appendix.pdf` with the latexmk command above.
11. **Figure description fix:** the invisible `\Description` of the RQ5 figure now says 197 safe instead of 139, matching the counts in `scripts/plot_rq4_safety.py`. `\Description` is defined empty, so nothing changes in the PDF.
