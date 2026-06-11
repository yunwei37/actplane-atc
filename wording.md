# Paper Terminology Conventions

## Agent policy model

An AI agent operates through a harness that maintains the agent loop, tools, memory, and behavioral constraints.

| Term | Meaning | Example |
|------|---------|---------|
| **instruction** | A behavior the agent SHOULD do (positive). | "Run tests before committing." |
| **constraint** | A behavior the agent SHOULD NOT do (negative). | "Never delete R2 data." |
| **policy intent** | The semantic meaning of the set of instructions and constraints on an agent. Today encoded in natural language (CLAUDE.md, AGENTS.md), which is ambiguous and probabilistic. | "The policy intent of 'never modify upstream source' is to protect specific files from writes." |
| **reminder** | System-level enforcement of an instruction. Implemented by the DSL `notify` effect. Use both terms: "reminder" for the concept, `notify` for the DSL mechanism. | "a reminder that tests should run" |
| **restriction** | System-level enforcement of a constraint. Implemented by DSL `block` and `kill` effects. Use both terms: "restriction" for the concept, `block`/`kill` for the DSL mechanism. | "a restriction on deleting data files" |

### Where to define in paper

- **instruction, constraint, policy intent, policy engine**: Background, "AI agent policy enforcement" paragraph.
- **reminder, restriction**: Design, when introducing the three DSL effects (notify/block/kill).
- Do NOT define these terms in abstract or intro; just use them naturally after Background defines them.

### The semantic gap

Existing policy engines leave a semantic gap: policy intent is expressed in natural language, but enforcement needs to decide over system actions. Two sub-problems:

1. **Context/specificity**: many policies reference project or task context ("the test suite", "upstream source") that needs to be resolved into concrete commands and paths. Agents closest to the project have this context.
2. **Determinism**: natural-language compliance is probabilistic; enforcement needs to be deterministic.

The DSL lets agents express policy intent as enforceable system actions: reminders for instructions, restrictions for constraints.

### Instruction vs constraint

Most system-level instructions can be reframed as constraints ("run tests before committing" → "do not commit without running tests"). The distinction matters for enforcement effect: constraints map to block/kill (hard enforcement), while instructions map to notify (soft reminder). Some instructions are better as reminders because the agent may have a valid reason to deviate.

This maps to the empirical finding (Zhang et al., 2026) that negative constraints and positive directives affect agent behavior differently.

### Andi's model (reference)

```
Instruction = behavior agent SHOULD do     → notify (reminder)
Constraint  = behavior agent SHOULD NOT do → block/kill (restriction)
Intended policy = instructions + constraints
Today: encoded in NL (agents.md/claude.md) → ambiguous, probabilistic
Goal: language + runtime to codify → reminders + restrictions → deterministic
Two problems: (1) context/specificity (2) determinism
```

Andi's definitions (verbatim):

> An instruction is the behavior that an AI Agent should do.
> A constraint is the behavior that an AI Agent should not do.
> An AI agent's intended policy is the set of instructions and constraints on that agent.
> Today's tools encode an agent's intended policy in natural language through the file system (eg agents.md/claude.md).
> We find that many policies reference system-level behaviors, where the natural language interface is (inaccurate? faulty? probabilistic?)
> We aim to provide a language and runtime that enables agents to codify their policies into system-enforceable reminders (for instructions) and restrictions (for constraints).
> We show that this makes agents work better.

Andi's question: "Can we think of an instruction that is not enforceable as a constraint?"

> Separately, I think that the term "AI Agent Intent" also might be too general, because our dsl is really about helping with very specific types of issues that an AI agent might want to do. We don't mean all possible intents can be encoded with our dsl (I don't think?)
> My suggestion might be "The DSL provides a language for AI Agents to express their high-level constraints into enforceable system actions".

yunwei37's response:

> While there is one thing, just like the instruction files include descriptions, instructions(TODO) and constraints, "high-level constraints" only include constraints. Basically or informally, our goal of this project is to let AI express claude.md/agents.md in system layer. So we also include notifications, which allows agents to express instructions or goals.

yunwei37 on "AI agent intent":

> Maybe we shouldn't say AI Agent intent. It should be "The Intent of policy" / "The policy intent". I was using AI Agent intent from agentsight, but that was different.

yunwei37 on the semantic gap:

> However, existing policy engines leave a semantic gap: AI agent intent of constraints or instructions (directives?) are expressed in natural language, but enforcement needs to decide over system actions.
> The natural language interface is (Ambiguity and probabilistic). So, we want one that 1. solve the context problem, be specific so can be enforced 2. deterministic

### Decisions

1. Use **"policy intent"** (not "AI agent intent" or "intended policy").
2. **instruction vs constraint** defined in Background.
3. **reminder/restriction** used in paper alongside notify/block/kill, not as replacements.

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

## Policy isolation

| Term | Meaning |
|------|---------|
| **policy isolation** | The property that each domain's rules govern only its subtree and cannot be weakened by descendants or affected by siblings. |

Policy isolation is achieved through three mechanisms:

1. **Domain hierarchy** (structure): a tree of domains; each process belongs to exactly one domain.
2. **Layered authority** (upward immutability): a child domain inherits all parent rules and cannot remove, disable, or weaken any inherited rule.
3. **Scoped enforcement** (downward scoping + lateral non-interference): rules added by a domain take effect only within that domain and its descendants; sibling domains' local rules do not affect each other.

### Usage in paper

- Use **"policy isolation"** as the top-level property name. Section §4.4 title: "Policy Isolation via Domain Hierarchy."
- Use **"layered authority"** when discussing the specific mechanism that prevents weakening of inherited rules.
- First occurrence (§4.4 opening): define all three components in one sentence. Subsequent uses can say "policy isolation" alone.
- Do NOT use "resource isolation" or unqualified "isolation" interchangeably; policy isolation governs rule scope and mutability, not memory/fd/namespace boundaries.

## Words to avoid in paper text

- **Em-dashes (`---`)**: use commas, semicolons, or parentheses instead. Table cells using `---` for "not applicable" are OK.
- **"cannot be circumvented"**: too absolute; use "is not bypassed by" (threat model already lists bypass paths).
- **"irrevocable"** without qualification: use "irrevocable by default" since declassification exists.
- **"static"** without definition: clarify whether it means "human-authored," "pre-loaded," or "not runtime-updated."
