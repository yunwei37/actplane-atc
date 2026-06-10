# Paper Terminology Conventions

## Core terms: directive vs rule vs policy

| Term | Scope | Meaning | Example |
|------|-------|---------|---------|
| **directive** | Empirical study only (§3) | A classification label for NL statements that ask the agent to perform, avoid, or condition an action. Contrast with "description." | "64% of statements are directives" |
| **rule** | DSL and general usage | An individual constraint, whether in natural language or in the DSL. In the DSL, each `rule name:` block is one rule. | "38 randomly-selected rules"; `rule tests-before-commit:` |
| **policy** | DSL compilation unit | A collection of rules compiled into a single configuration blob. | "the agent generates a policy"; "per-task policy" |

### Usage guidelines

- **In the empirical study (§3)**: use "directive" as the classification label. "system-observable directives", "cross-event directives", etc.
- **When summarizing empirical study findings** (abstract, intro): "directive" is OK when directly citing the study's numbers (e.g., "83% of directives"). Otherwise prefer "rule."
- **Outside the empirical study**: use "rule" for individual constraints and "policy" for the compiled DSL unit. Do not use "directive" in design, implementation, or evaluation sections (except when explicitly referencing the empirical study's classification).
- **Avoid mixing in the same sentence**: e.g., ~~"Cross-event directives (18 of 38 rules)"~~ → "Cross-event rules (18 of 38)".

## Quantifier and precision conventions

- Avoid **"all"** in universal claims about external systems. Use "these" or name them.
- Avoid **"most"** unless the data shows >50% of the stated denominator. Prefer "many" when the fraction is 15-50%.
- Use **"suggest"** (not "confirm") for results from small or single-run experiments.
- Use **"observe"** (not "see") for kernel-level visibility; avoid "all" before "system actions."
- When citing percentages, **make the denominator explicit** or recoverable: "83% of those" not just "83%."
- **"may have reached"** (not "has reached") for the IFC invariant, since label propagation is a conservative over-approximation.

## Compound adjectives (hyphenation)

Hyphenate compound adjectives before nouns:
- cross-event, per-event, tool-level, tool-call, intent-level, system-level, OS-level
- Exception: after a verb ("enforcement operates at the OS level") — no hyphen.

## Words to avoid in paper text

- **Em-dashes (`---`)**: use commas, semicolons, or parentheses instead. Table cells using `---` for "not applicable" are OK.
- **"cannot be circumvented"**: too absolute; use "is not bypassed by" (threat model already lists bypass paths).
- **"irrevocable"** without qualification: use "irrevocable by default" since declassification exists.
- **"static"** without definition: clarify whether it means "human-authored," "pre-loaded," or "not runtime-updated."
