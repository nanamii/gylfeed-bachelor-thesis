#!/usr/bin/env python
# encoding:utf8

from collections import defaultdict

import os
import sys
import feedparser



absPath = os.path.abspath(sys.argv[1])
files = os.listdir(sys.argv[1])

d = defaultdict(int)


def check_entries(feed, attr, d):
    try:
        if attr == "title" and feed.entries[0].title:
            d["title"] +=1
        if attr == "summary" and feed.entries[0].summary:
            d["summary"] +=1
        if attr == "author" and feed.entries[0].author:
            d["author"] +=1
        if attr == "updated_parsed" and feed.entries[0].updated_parsed:
            d["updated_parsed"] +=1
        if attr == "id" and feed.entries[0].id:
            d["id"] +=1
        if attr == "link" and feed.entries[0].link:
            d["link"] +=1
    except Exception as e:
        print(e)


def check_feed(feed, attr, d):
    try:
        if attr == "icon" and feed.feed.icon:
            d["icon"] +=1
        if attr == "image" and feed.feed.image:
            d["image"] +=1
        if attr == "logo" and feed.feed.logo:
            d["logo"] +=1
    except Exception as e:
        print(e)




for file_ in files:
    feed = feedparser.parse(os.path.join(absPath, file_))
    d["counter"] +=1


    attr_entries = ["title", "summary", "author", "updated_parsed",
                    "id", "link"]

    attr_feed = ["icon", "image", "logo"]


    for attr in attr_entries:
        check_entries(feed, attr, d)

    for attr in attr_feed:
        check_feed(feed, attr, d)

    print(d)
