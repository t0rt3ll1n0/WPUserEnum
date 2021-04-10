#!/usr/bin/env python3

import os
import sys

try:
    filelist = sys.argv[1]
except IndexError:
    print("Usage: python3 WP_LIST.py list.txt")
    exit(0)

f = open(filelist, "r")
x = f.read().split()
for site in x:
    os.system(f"python3 WP.py {site}")
