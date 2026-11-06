import copy
import hashlib
import json
import os
import re
import sys

import polib


ROOT, BUILD, TRANSLATIONS, OUTDIR = sys.argv[1:5]
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
IMAGE_REFERENCE = re.compile(r"@@image: '([^']+)'; md5=([0-9a-f]{32})")

with open(TRANSLATIONS, encoding="utf-8") as file:
    translations = json.load(file)
os.makedirs(OUTDIR, exist_ok=True)
remaining = []
changed = 0


def key(entry):
    return entry.msgctxt, entry.msgid


def image_translation(msgid):
    match = IMAGE_REFERENCE.fullmatch(msgid)
    if match is None:
        raise ValueError(f"Malformed image reference: {msgid}")
    image_path, _ = match.groups()
    relative_path = image_path.removeprefix("images/").split("/")
    localized_path = os.path.join(ROOT, "images", "pt_BR", *relative_path)
    if not os.path.isfile(localized_path):
        return msgid
    with open(localized_path, "rb") as image:
        digest = hashlib.md5(image.read()).hexdigest()
    return f"@@image: '{image_path}'; md5={digest}"


def serialize_changes(raw, replacements):
    lines = raw.splitlines(keepends=True)
    newline = "\r\n" if "\r\n" in raw else "\n"
    ranges = []
    for line_number, entry in replacements:
        start = line_number - 1
        while start > 0 and lines[start - 1].strip():
            start -= 1
        end = line_number - 1
        while end < len(lines) and lines[end].strip():
            end += 1
        rendered = str(entry).replace("\n", newline).splitlines(keepends=True)
        ranges.append((start, end, rendered))
    for start, end, rendered in sorted(ranges, reverse=True):
        lines[start:end] = rendered
    result = "".join(lines)
    if not result.endswith(("\n", "\r")):
        result += newline
    return result


for catalog, target_files in TARGETS.items():
    local_path = os.path.join(ROOT, "po", "pt_BR", catalog)
    current_path = os.path.join(BUILD, catalog)
    with open(local_path, encoding="utf-8", newline="") as file:
        raw = file.read()
    local = polib.pofile(local_path)
    current = polib.pofile(current_path)
    local_by_key = {key(entry): entry for entry in local if not entry.obsolete}
    replacements = []
    additions = []

    for source in current:
        refs = {ref.split(":")[0] for ref, _ in source.occurrences}
        if source.obsolete or not refs.intersection(target_files):
            continue
        existing = local_by_key.get(key(source))
        is_image = source.msgid.startswith("@@image:")
        image_msgstr = image_translation(source.msgid) if is_image else None
        translations_by_ref = translations.get(catalog, {})
        translation = None
        if not is_image:
            translation = next(
                (
                    translations_by_ref[ref]
                    for ref, _ in source.occurrences
                    if ref.split(":")[0] in target_files
                    and ref in translations_by_ref
                ),
                None,
            )
        if existing and not existing.fuzzy and existing.msgstr.strip():
            if is_image and existing.msgstr == image_msgstr:
                continue
            if not is_image and (
                translation is None or existing.msgstr == translation
            ):
                continue

        updated = copy.deepcopy(existing if existing else source)
        updated.flags = [flag for flag in updated.flags if flag != "fuzzy"]
        updated.occurrences = sorted(
            set(updated.occurrences).union(source.occurrences)
        )
        if is_image:
            updated.msgstr = image_msgstr
        else:
            if not translation:
                remaining.append((catalog, source.occurrences, source.msgid))
                continue
            updated.msgstr = translation

        if existing:
            replacements.append((existing.linenum, updated))
        else:
            additions.append(updated)
        changed += 1

    result = serialize_changes(raw, replacements)
    if additions:
        result = result.rstrip("\r\n") + "\n\n"
        result += "\n\n".join(str(entry) for entry in additions) + "\n"
    output_path = os.path.join(OUTDIR, catalog)
    with open(output_path, "w", encoding="utf-8", newline="") as file:
        file.write(result)

print(f"Updated {changed} current messages.")
print(f"Untranslated text messages: {len(remaining)}")
for catalog, refs, msgid in remaining[:10]:
    print(f"{catalog}: {refs} — {msgid[:160]}")
if len(remaining) > 10:
    print(f"... and {len(remaining) - 10} more")
