import hashlib
import json
import os
import re
import sys


SOURCE, PENDING, OUT = sys.argv[1:4]
pattern = re.compile(r"@@image: '([^']+)'; md5=([0-9a-f]{32})")

with open(PENDING, encoding="utf-8") as source, open(
    OUT, "w", encoding="utf-8"
) as output:
    for line in source:
        record = json.loads(line)
        if record["type"] != "image":
            continue
        image_path, expected = pattern.fullmatch(record["source"]).groups()
        relative = image_path.removeprefix("images/").replace("/", os.sep)
        candidates = [
            os.path.join(SOURCE, "images", "C", relative),
            os.path.join(SOURCE, "images", "common", relative),
        ]
        base = next((path for path in candidates if os.path.isfile(path)), "")
        base_hash = ""
        if base:
            with open(base, "rb") as image:
                base_hash = hashlib.md5(image.read()).hexdigest()
        localized = os.path.join(SOURCE, "images", "pt_BR", relative)
        localized_hash = ""
        if os.path.isfile(localized):
            with open(localized, "rb") as image:
                localized_hash = hashlib.md5(image.read()).hexdigest()
        output.write(
            f"{record['catalog']} | {record['refs'][0]} | {image_path} | "
            f"base={base_hash or 'MISSING'} expected={expected} | "
            f"pt_BR={localized_hash or 'none'}\n"
        )
