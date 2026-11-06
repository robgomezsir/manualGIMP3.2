import json
import os
import sys

import polib


ROOT, BUILD, OUT = sys.argv[1:4]
TARGETS = {
    "preface.po": {"src/preface/authors.xml"},
    "introduction.po": {"src/introduction/whats-new.xml"},
    "gimp.po": {"src/introduction.xml"},
    "concepts.po": {
        "src/concepts/intro.xml",
        "src/concepts/concepts.xml",
        "src/concepts/basic-setup.xml",
        "src/concepts/undo.xml",
    },
    "tutorial.po": {"src/tutorial/quickies.xml"},
    "using.po": {
        "src/using/getting-unstuck-intro.xml",
        "src/using/getting-unstuck.xml",
        "src/using/getting-unstuck-gui.xml",
        "src/using/getting-unstuck-export.xml",
    },
}

with open(OUT, "w", encoding="utf-8") as output:
    for catalog, target_files in TARGETS.items():
        current = polib.pofile(os.path.join(BUILD, catalog))
        local = polib.pofile(os.path.join(ROOT, "po", "pt_BR", catalog))
        local_by_key = {
            (entry.msgctxt, entry.msgid): entry for entry in local if not entry.obsolete
        }
        selected = []
        for source in current:
            refs = {ref.split(":")[0] for ref, _ in source.occurrences}
            if source.obsolete or not refs.intersection(target_files):
                continue
            entry = local_by_key.get((source.msgctxt, source.msgid))
            if entry is None or entry.fuzzy or not entry.msgstr.strip():
                selected.append((source, entry))
        print(f"{catalog}: {len(selected)} unresolved")
        for source, entry in selected:
            record = {
                "catalog": catalog,
                "type": "image" if source.msgid.startswith("@@image:") else "text",
                "status": "missing" if entry is None else (
                    "fuzzy" if entry.fuzzy else "empty"
                ),
                "merged_status": "fuzzy" if source.fuzzy else (
                    "empty" if not source.msgstr.strip() else "translated"
                ),
                "refs": [ref for ref, _ in source.occurrences],
                "source": source.msgid,
                "translation": "" if entry is None else entry.msgstr,
                "merged_translation": source.msgstr,
            }
            output.write(json.dumps(record, ensure_ascii=False) + "\n")
