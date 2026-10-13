# Contributing

Contributions that make the skill more usable, clearer, or better grounded are welcome.

## Start with a concrete problem

For a bug or improvement, include the prompt, anonymized source material, the actual response, and the expected behavior. Explain whether the issue concerns product truth, scope, scripting, production feasibility, language, analytics, or documentation.

Do not include private client material, access credentials, or unpublished business data in public issues or pull requests. Use a fictional minimal example where possible.

## Make a focused change

1. Keep `psychological-content-strategy` stable unless a deliberate breaking migration is documented.
2. Keep the main `SKILL.md` compact and route detail into the appropriate reference.
3. Preserve claims and output scope. Prefer a generalized decision rule to a fix that only works for one example.
4. Distinguish primary-source findings, practical heuristics, and creative hypotheses.
5. Give sources for exact scientific or platform claims, including their context and verification date.
6. Keep examples self-contained and mark fictional assets or unsupported proof requirements.
7. Update docs or the changelog when behavior changes.

## Validate locally

Python 3.10+ runs the dependency-free repository checker:

```bash
python scripts/validate.py
```

To check discovery through the official installer:

```bash
npx skills add . --list
```

When changing behavior, try the relevant prompts in `evals/evals.json`. Save meaningful evidence and explain limitations. Structural validation alone does not establish writing quality or audience performance.

## Pull requests

Describe the problem, the resulting behavior, relevant tradeoffs, and validation. Avoid promising performance improvements without actual evidence. Contributions are made under the repository's [MIT license](LICENSE); linked external materials retain their own rights.
