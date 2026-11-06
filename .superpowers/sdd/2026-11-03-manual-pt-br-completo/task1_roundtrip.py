import sys

import polib


polib.pofile(sys.argv[1]).save(sys.argv[2])
