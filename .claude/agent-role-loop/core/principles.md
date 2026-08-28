# Principles

This document states the four principles behind the role loop. The loop itself is described in [loop.md](loop.md). Everything in `core/` is deliberately independent of any specific model, platform, or vendor: the principles hold for any sufficiently capable agent, and equally for a team of humans.

## 1. Context isolation

Quality degrades when one context accumulates everything: the original request, exploration transcripts, logs, failed attempts, review comments, and stale assumptions. Late instructions get lost, early assumptions outlive their validity, and output trends toward confident mush.

The counter-measure is to give every role its own fresh, minimal context. The planner does not need the builder's test output. Reviewers do not need the planner's exploration transcript. Nobody needs every intermediate thought - only the current artifact, the decision, the evidence, and the next move.

Practical rules:

- Run each role in a fresh context (a new agent instance, a new chat window, a new API conversation).
- Keep the orchestrating context small: current stage, current artifact, decision, next action.
- Never paste a full transcript across a role boundary. If a role needs information, it belongs in the handoff contract; if it is not in the contract, the role works without it.

## 2. Explicit handoffs

Every transition between roles passes exactly one compact, structured artifact: a contract. The contracts (C0 through C7, defined in [contracts/](contracts/)) are the stable interface of the loop; the role prompts in [roles/](roles/) are the implementation behind that interface and may evolve freely as long as the contracts stand.

This is information hiding applied to a process. A role can be rewritten, swapped for a different model, or performed by a human, and the rest of the loop does not notice - exactly as a module with a stable interface can be reimplemented without breaking its callers.

Practical rules:

- A handoff that is not in the contract did not happen. Verbal context, vibes, and "as discussed" do not cross role boundaries.
- Contracts mark which fields may be omitted with `<none>`. Filling a field with plausible filler is worse than `<none>`: it manufactures false precision downstream.
- When a role discovers it needs information the contract does not carry, that is a contract change request, not an excuse to peek into another role's context.

## 3. Proportionality

Not every task deserves the full loop. Running six roles to fix a typo wastes time, money, and attention; pushing an oversized feature through the loop produces a plan too big to verify. The loop's sweet spot is small, medium, and large tasks - not extra-small, not extra-large.

That judgment is itself a role: Triage looks at the work item before anything else happens and decides between the full loop, a lightweight path straight to the builder, or rejection with advice (split the work, or just do it by hand).

Practical rules:

- Triage runs first, always, and is allowed to be fast.
- A lightweight path is a feature, not a violation of the process.
- When in doubt between light and full, consider the cost of being wrong: irreversible or contract-touching work earns the full loop.

## 4. Human in the loop

Between planning and building sits a gate that only a human may pass: the Human Gate. The point is to stop confident automation from charging past judgment calls - is this still the right goal, is the scope acceptable, are the risks reversible?

The gate is deliberately a role description for a person, not an agent prompt. Automating it would optimize away exactly the protection it exists to provide.

Practical rules:

- The gate decision (C4) is written down like every other handoff. "I skimmed it and it seemed fine" is not a gate decision.
- The gate may answer open questions, defer them explicitly, or stop the work. Deferring silently is the only forbidden move.
- Decisions made at the gate are recorded in the contract so that downstream roles can rely on them without re-litigating.
