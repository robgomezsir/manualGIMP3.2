# Final review fix wave

## Context

This is the single fix wave after the final review of the initial PT-BR manual block. Work only in `C:\Users\robgo\GIMP\manualGIMP3.2`, on the current `main` branch.

## Findings and scope

1. Improve the translation of the current source title `What to do if you are stuck` in `src/gimp.xml`, catalog entry in `po/pt_BR/gimp.po`. Use a clear PT-BR phrase that cannot be mistaken for the application freezing; reviewer suggestion: “O que fazer se você não souber como prosseguir”.
2. Improve the current translation of `Transformation tools including rotate, scale, shear and flip.` in `src/introduction.xml` / `po/pt_BR/gimp.po`: translate `flip` as “espelhamento” to make the image transformation specific.
3. Verify the review concern that “Starting GIMP” and “Fire up the GIMP” become duplicate current index labels. The exact `msgid` “Fire up the GIMP” is absent from current `src/`; its catalog entry points to an old source line. Do not edit obsolete catalog entries. Use current XML/build extraction to confirm whether a true duplicate remains; if there is no current duplicate, record this as not applicable in the report.

## Constraints

- Modify only current relevant messages in `po/pt_BR/gimp.po`; do not change XML source, other catalog entries, assets, or plan.
- Preserve `msgid`, links, references, DocBook tags, placeholders, and existing facts.
- Validate with `msgfmt --check`, `git diff --check`, and a focused build or HTML/source check sufficient to confirm current index labels and the two revised translations.
- Create a local commit in PT-BR if the changes pass. Do not push; the controller will review the fix diff first.
- Do not dispatch other subagents.

## Report

Write the full report to `.superpowers/sdd/2026-11-03-manual-pt-br-translation/final-fix-report.md`, including findings addressed/not applicable, commands and exact outcomes, changed files, commit and concerns.
