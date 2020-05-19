#!/usr/bin/env python
from sys import argv
conf = str(argv[1])
print(conf)
with open(conf, 'r') as conf_sw:
    print(conf_sw.readline())
