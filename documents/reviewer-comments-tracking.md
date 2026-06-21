# ATC Reviewer Comments Tracking

Source: `actplane_atc_comments.pdf`

This document tracks all reviewer comments from the PDF, the corresponding text locations, and whether they have been addressed in the current revision.

---

## Summary

| Page | Comments | Addressed | Partially | Not Addressed |
|------|----------|-----------|-----------|---------------|
| 1    | 8        | 0         | 2         | 6             |
| 2    | 6        | 0         | 1         | 5             |
| 3    | 5        | 0         | 0         | 5             |
| **Total** | **19** | **0** | **3** | **16** |

---

## Page 1 (Abstract / Introduction)

### C1.1: Semantic Gap Not Defined

**Location:** After "directives" sentence, before "Yet existing policy engines..."

**Highlighted Text:**
> "Yet existing policy engines fail to connect policy intent to system-level actions, leaving a semantic gap."

**Comment:**
> A logic gap here: The prior sentence introduces "directives." But the following sentence shifts to discuss the "semantic gap." In fact, what semantic gap is has never been defined or explained.

**Status:** NOT ADDRESSED

**Notes:** The current main.tex introduction mentions "semantic gap" but does not define it before first use. Need to add a definition or example before using the term.

---

### C1.2: Too Many Jargons Without Explanation

**Location:** Same paragraph as C1.1

**Highlighted Text:**
> "system-level events" / "tool-call guardrails" / "indirect system actions" / "cross-event directives"

**Comment:**
> Many tech jargons are used here without explanations. It remains unclear what the "semantic gap" really is and how the mentioned quantitative evidences support the "semantic gap" argument?

**Status:** NOT ADDRESSED

**Notes:** Terms like "tool-call guardrails," "cross-event directives," and "system-level events" are used without definition. The statistics (64%, 83%, etc.) are presented without explaining how they relate to the semantic gap.

---

### C1.3: Why Existing Approach Falls Short Unclear

**Location:** Paragraph about OS-level sandbox-style mechanisms

**Highlighted Text:**
> "OS-level sandbox-style mechanisms confine process, file, and network actions, but they expect static policy that is hard to pre-define for the 74% of rules needing project or task context, and they return errors without semantic context that further confuse the agent."

**Comment:**
> I understand that this sentence intends to explain why existing approach falls short, but the narrative given here is really hard to understand. Readers cannot tell why existing approach cannot bridge the "semantic gap," which is left undefined anyway.

**Status:** PARTIALLY ADDRESSED

**Notes:** Current revision (01-introduction.tex L28-29) explains OS sandboxes "control resource access instead of actions and return opaque denials." This is clearer but still doesn't connect explicitly to the semantic gap concept.

---

### C1.4: Safety Constraints Introduced Without Explanation

**Location:** After the semantic gap discussion

**Highlighted Text:**
> "safety constraints"

**Comment:**
> Another term introduced without explanation. Why the discussion shifts to "safety constraints"?

**Status:** NOT ADDRESSED

**Notes:** In current L33, "safety constraints" appears without prior definition. Need to explain what safety constraints are and why they matter in the agent context.

---

### C1.5: Need Concrete Example for Semantic Gap

**Location:** Right column, introduction paragraph

**Highlighted Text:**
> "policy intent is expressed in underspecified natural language, but enforcement needs to decide over concrete system actions."

**Comment:**
> This explanation of a semantic gap does most of the job, but not all of them. Consider adding an example to give readers a more concrete idea what a semantic gap could be in a real agent scenario.

**Status:** PARTIALLY ADDRESSED

**Notes:** Current L21-22 gives examples ("never modify upstream source" requires knowing paths, "reviewer sub-agent only writes to its project directory" needs scope). These are good but could be expanded to show the gap more clearly.

---

### C1.6: Proposed Solution Too Vague

**Location:** After discussing the problem

**Highlighted Text:**
> "engine that allows agents to declare and enforce information-flow control (IFC) policies in the OS kernel with semantic feedback. Layered policy domains isolate agent policies and prevent weakening of inherited constraints."

**Comment:**
> The proposed solution is described in two vague sentences at a very high level. It is unclear what it is and how it addresses the "semantic gap" challenge facing current agent runtimes.

**Status:** NOT ADDRESSED

**Notes:** Current L47-56 describes ActPlane but doesn't explicitly connect the solution to the semantic gap problem. Need to explain HOW DSL + IFC + feedback addresses the gap.

---

### C1.7: Suggest Restructuring to Four-Step Narrative

**Location:** Same area as C1.5

**Comment:**
> The examples given here remain at a high level. I'd suggest restructuring this paragraph into a four-step narrative:
> 1. The semantic gap problem: define exactly what it is.
> 2. Give a concrete example to illustrate the gap between policy intent (e.g., all commits must be tested first) and action enforcement (e.g., run test before commits).
> 3. Give statistical numbers to illustrate the prevalence of directive instructions and system-level behaviors.
> 4. Why it is difficult to track system actions following directive instructions.

**Status:** NOT ADDRESSED

**Notes:** This is a structural suggestion. Current introduction does not follow this four-step structure. Consider rewriting to:
1. Define semantic gap with example
2. Show concrete policy-to-action gap
3. Present statistics
4. Explain why tracking is hard

---

### C1.8: OS-Level Enforcement Comes Out of Nowhere

**Location:** Right column, near "OS-level enforcement with static policy is also insufficient"

**Highlighted Text:**
> "OS-level enforcement with static policy is also insufficient."

**Comment:**
> OS-level enforcement comes out of no where. Readers might wonder: is this the current practice; why should we care about it?

**Status:** NOT ADDRESSED

**Notes:** Need to introduce why OS-level enforcement matters before criticizing it. Add context about current agent deployment practices (sandboxes, etc.).

---

## Page 2 (Introduction continued / Background)

### C2.1: Argument Not Obvious

**Location:** "agent-harness policy engine should be programmable by agents and take effect at OS level"

**Highlighted Text:**
> "an agent-harness policy engine should be programmable by agents and take effect at OS level."

**Comment:**
> This argument is not obvious to me. More explanation and justification are expected.

**Status:** NOT ADDRESSED

**Notes:** Current L31-36 makes this argument but doesn't justify WHY agents should write policies or WHY OS-level is necessary. Need to add reasoning.

---

### C2.2: Safety Constraints Used Before Defined

**Location:** Same paragraph

**Highlighted Text:**
> "safety constraints"

**Comment:**
> Used before defined.

**Status:** NOT ADDRESSED

**Notes:** Same issue as C1.4. "Safety constraints" needs definition before use.

---

### C2.3: Need More Concrete Examples

**Location:** Background section

**Comment:**
> Consider adding more concrete examples to illustrate instructions, constraints, intent, and actions.

**Status:** NOT ADDRESSED

**Notes:** The four terms (instructions, constraints, intent, actions) are used throughout but not illustrated with concrete examples showing their relationships.

---

### C2.4: Explain Information-Flow Rules

**Location:** Where "labeled information-flow rules" appears

**Highlighted Text:**
> "labeled information-flow rules"

**Comment:**
> Explain what it is.

**Status:** NOT ADDRESSED

**Notes:** IFC is mentioned but not explained until much later. Need a brief explanation when first introduced.

---

### C2.5: Terminologies Used Before Definition (Lost)

**Location:** Around "Layered policy domains isolate agent policies..."

**Highlighted Text:**
> "Layered policy domains isolate each agent's policy to its own subtree and prevent weakening of inherited constraints."

**Comment:**
> Terminologies used before definition. I'm completely lost here.

**Status:** NOT ADDRESSED

**Notes:** "Policy domains," "subtree," "inherited constraints" all need prior definition or at least brief explanation on first use.

---

### C2.6: Introduction Overall Assessment

**Location:** End of introduction

**Comment:**
> An introduction should answer the following four questions:
> 1) what is the problem and why it is important?
> 2) why current solution does not work well?
> 3) what is the proposed solution and how it works at a high level?
> 4) how does the proposed solution perform?
>
> Unfortunately, this introduction fails to do a good job. It half-answers Q1, mentions about Q2 but in a rather unclear way, and briefly talks about Q3 using many technical jargons without explanation or justification.

**Status:** PARTIALLY ADDRESSED

**Notes:** This is an overall structural critique. Current revision has improved clarity in some areas but still needs:
- Better Q1: clearer problem definition with concrete example
- Better Q2: clearer explanation of why existing approaches fail
- Better Q3: explain solution without assuming IFC/domain knowledge

---

## Page 3 (Background / Empirical Study)

### C3.1: Sandbox Statement Too Vague

**Location:** Top of page 3

**Highlighted Text:**
> "sandboxes, but they expect statically pre-written policies and return opaque errors with no connection to policy intent."

**Comment:**
> This is too vague to understand.

**Status:** NOT ADDRESSED

**Notes:** Need to be more specific about WHICH sandboxes, WHAT kind of policies, and WHY opaque errors are problematic for agents.

---

### C3.2: IFC in Background Disconnected

**Location:** "Information-flow control" paragraph in Background

**Comment:**
> Why mentioning IFC in the background section? It seems disconnected to the previous paragraphs.

**Status:** NOT ADDRESSED

**Notes:** IFC appears without connecting to the agent policy enforcement problem. Need transition explaining why IFC is relevant to solving the semantic gap.

---

### C3.3: Four RQs Look Fragmented

**Location:** Empirical Study section, E-RQ list

**Comment:**
> These four RQs look fragmented. It is less clear why the authors choose to study them, and how their characterizations can guide the later system design.

**Status:** NOT ADDRESSED

**Notes:** Need to add a sentence before the RQs explaining their purpose and how they connect to the design requirements.

---

### C3.4: Line Count Statement Confusing

**Location:** "so the same files appear balanced (49% directives) when measured by lines"

**Highlighted Text:**
> "average 6.8 lines, so the same files appear balanced (49% directives) when measured by lines."

**Comment:**
> I don't get it.

**Status:** NOT ADDRESSED

**Notes:** This sentence (current L89-90 in 02-motivation.tex) is confusing. Need to rewrite to clarify that statement-level vs line-level measurement gives different results.

---

### C3.5: Study Relevance Unclear

**Location:** "Which Topics Contain Directives?" section header

**Comment:**
> Why is this study relevant?

**Status:** NOT ADDRESSED

**Notes:** Need to add motivation before presenting the topic breakdown. Explain why understanding topic distribution matters for system design.

---

## Action Items

### High Priority (Structural Issues)

1. **Rewrite Introduction following four-step structure** (C1.7, C2.6)
   - Define semantic gap with concrete example first
   - Explain why existing approaches fail
   - Describe solution connecting to the problem
   - Preview results

2. **Define key terms before use** (C1.2, C2.2, C2.4, C2.5)
   - semantic gap
   - safety constraints
   - information-flow control
   - policy domains
   - tool-call guardrails

3. **Add concrete examples** (C1.5, C2.3)
   - Show a complete example: policy intent -> system actions -> gap
   - Illustrate instructions vs constraints

### Medium Priority (Clarity Issues)

4. **Connect OS-level enforcement to context** (C1.8, C2.1)
   - Explain current agent deployment practices
   - Justify why agents should write policies
   - Justify why OS-level is necessary

5. **Improve Background transitions** (C3.2)
   - Connect IFC to agent policy problem

6. **Clarify empirical study motivation** (C3.3, C3.5)
   - Add purpose statement before RQs
   - Explain relevance of topic breakdown

### Lower Priority (Minor Clarifications)

7. **Rewrite confusing sentences** (C1.3, C3.1, C3.4)
   - Sandbox limitations explanation
   - Line count vs statement count explanation

---

## Revision Log

| Date | Changes Made |
|------|--------------|
| 2026-06-20 | Initial comment extraction and tracking document created |
| | Identified 19 comments across 3 pages |
| | Status: 0 addressed, 3 partially addressed, 16 not addressed |
