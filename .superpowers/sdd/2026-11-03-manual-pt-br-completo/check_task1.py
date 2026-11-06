import hashlib
import os
import re
import sys

import polib


ROOT, BUILD, SOURCE = sys.argv[1:4]
PO_DIR = sys.argv[4] if len(sys.argv) > 4 else os.path.join(ROOT, "po", "pt_BR")
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
image_pattern = re.compile(r"@@image: '([^']+)'; md5=([0-9a-f]{32})")
problems = []
checked = 0

for catalog, target_files in TARGETS.items():
    current = polib.pofile(os.path.join(BUILD, catalog))
    local = polib.pofile(os.path.join(PO_DIR, catalog))
    local_by_key = {
        (entry.msgctxt, entry.msgid): entry for entry in local if not entry.obsolete
    }

    for source in current:
        refs = {ref.split(":")[0] for ref, _ in source.occurrences}
        if source.obsolete or not refs.intersection(target_files):
            continue
        checked += 1
        entry = local_by_key.get((source.msgctxt, source.msgid))
        if entry is None:
            problems.append(f"{catalog}: missing current message at {source.occurrences}")
            continue
        if entry.fuzzy or not entry.msgstr.strip():
            problems.append(f"{catalog}: fuzzy/empty current message at {source.occurrences}")
            continue

        if source.msgid.startswith("@@image:"):
            match = image_pattern.fullmatch(source.msgid)
            if match is None:
                problems.append(f"{catalog}: malformed source image reference at {source.occurrences}")
                continue
            image_path, expected_md5 = match.groups()
            relative_path = image_path.removeprefix("images/")
            image_files = [
                os.path.join(SOURCE, "images", directory, relative_path.replace("/", os.sep))
                for directory in ("C", "common")
            ]
            existing_images = [path for path in image_files if os.path.isfile(path)]
            if not existing_images:
                problems.append(f"{catalog}: missing base image {image_path}")
                continue
            actual_hashes = set()
            for image_file in existing_images:
                with open(image_file, "rb") as image:
                    actual_hashes.add(hashlib.md5(image.read()).hexdigest())
            if expected_md5 not in actual_hashes:
                problems.append(f"{catalog}: incorrect base image MD5 for {image_path}")
                continue

            localized_path = os.path.join(
                SOURCE, "images", "pt_BR", relative_path.replace("/", os.sep)
            )
            if os.path.isfile(localized_path):
                with open(localized_path, "rb") as image:
                    localized_md5 = hashlib.md5(image.read()).hexdigest()
                expected_translation = (
                    f"@@image: '{image_path}'; md5={localized_md5}"
                )
            else:
                expected_translation = source.msgid
            if entry.msgstr != expected_translation:
                problems.append(
                    f"{catalog}: incorrect localized image reference for {image_path}"
                )

print(f"Checked {checked} current messages in Task 1 sources.")
for problem in problems[:20]:
    print(problem)
if len(problems) > 20:
    print(f"... and {len(problems) - 20} more")
print(f"Unresolved: {len(problems)}")
sys.exit(bool(problems))
