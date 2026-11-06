# SDD ledger — plan: docs/superpowers/plans/2026-11-03-manual-pt-br-completo.md

Setup: plan `2026-11-03-manual-pt-br-completo.md` and design spec are committed locally; task base is the current `main` HEAD. User approved executing inline on the current checkout; no linked worktree is used.

Ruling: work in the existing `main` checkout rather than creating a linked worktree — the user previously requested working in the current files without a worktree and approved this inline plan — cost if wrong: an interruption can leave partial translation commits directly on `main`.

Ruling: use target-source coverage checks as the RED/GREEN test for PO translation batches, followed by gettext/build/preview validation — the deliverables are translation data, not executable behavior — cost if wrong: a coverage check can miss semantic translation errors, which the required source review and rendered preview must catch.

Pre-flight: Task 1 → Task 2 — both edit `concepts.po` and `using.po`; Task 1 changes only the first-part source occurrences, Task 2 changes only the second-part occurrences. Keep shared messages consistent and preserve unaffected occurrences.
Pre-flight: Task 1 → Task 4 — both edit `gimp.po`; Task 1 changes `src/introduction.xml`, Task 4 changes `src/gimp.xml`, `src/key-reference.xml`, and `src/help-missing.xml`.
Pre-flight: Tasks 1–4 → Task 5 — all may update image references and localized captures; final audit must compare every active image reference with the actual PT-BR or base image and its hash.
Pre-flight: Tasks 1–4 share terminology — preserve one consistent PT-BR vocabulary across catalog boundaries; Task 4 glossary review and Task 5 rendered-manual review are the global checks.

Task 1: Started at base `214319d1a95e601b2c5a71a4309180e7d54b5be4`. Coverage RED initially found 513 current messages, including 187 fuzzy, empty, or missing messages in the target sources.
Task 1: Ruling: force-refresh the preview POTs after touching their source XML copies — Ninja's POT dependencies omit referenced image files, and the extracted Wilber image hash disagreed with the current source asset; cost if wrong: the coverage test might report stale image references even when the source image is current.
Task 1: Step 1 complete after refreshing all six catalog targets; the valid unresolved set is 168 text messages and 38 image references across 513 current messages. The 38 base-image hashes match the Linux preview source; six relevant PT-BR screenshot variants are present.
