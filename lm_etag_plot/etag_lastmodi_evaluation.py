# usr/bin/env python3
# encoding:utf8

from gi.repository import Soup
from gi.repository import GLib
from gi.repository import GObject
import requests
import sys


def read_urllist(filename):
    with open(filename, 'r') as fd:
        return fd.read().splitlines()


url_list = read_urllist(sys.argv[1])

cnt = {'lm': 0, 'etag': 0, 'both':0, 'all': 0}



for n, url in enumerate(url_list):
    try:
        r = requests.head(url)
    except:
        print("URL failed", url)
        continue

    print(n, url, r.status_code, cnt)
    if r.status_code == 200:
        cnt['all']+=1
        if 'last-modified' in r.headers:
            cnt['lm']+=1
        if 'etag' in r.headers:
            cnt['etag']+=1
        if 'last-modified' in r.headers and 'etag' in r.headers:
            cnt['both']+=1

print(cnt)
