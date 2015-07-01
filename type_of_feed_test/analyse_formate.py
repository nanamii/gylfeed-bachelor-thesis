#!/usr/bin/env python
# encoding:utf8

from collections import defaultdict

import os
import sys
import feedparser



absPath = os.path.abspath(sys.argv[1])
files = os.listdir(sys.argv[1])

d = defaultdict(int)
counter = 0

for file_ in files:
    # print('Nur Datei:', file_)
    # print('Datei mit Pfad:', os.path.join(absPath, file_))
    feed = feedparser.parse(os.path.join(absPath, file_))
    d[feed.version] += 1
    d[counter] +=1
    print(d)
