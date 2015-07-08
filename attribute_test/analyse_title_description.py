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
            if feed.entries[0].summary:
                d["title and summary"] +=1
        if attr == "summary" and feed.entries[0].summary:
            d["summary"] +=1
            if feed.entries[0].title:
                d["title and summary, validation"] +=1
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


def save_to_disk(url):
    try:
        with open('url_missing_format.txt', 'a') as tf:
            tf.write(url+"\n")
            print("Saving data to disk, url:", url)
    except IOError as ie:
        print("Fail to save data {ie}".format(ie=ie))




for file_ in files:
    feed = feedparser.parse(os.path.join(absPath, file_))
    d["counter"] +=1
    if feed.version == '':
        save_to_disk(file_)
    if feed.version == 'rss20':

        attr_entries = ["title", "summary"]

        for attr in attr_entries:
            check_entries(feed, attr, d)
        print(d)
