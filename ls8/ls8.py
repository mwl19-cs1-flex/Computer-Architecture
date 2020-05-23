#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

if len(sys.argv) != 2:
    print("Improper format, please use ls8.py examples/file_to_parse format!")
    sys.exit(1)
    
cpu.load(sys.argv[1])
# cpu.run()