# usr/bin/env python3
# encoding:utf8

from gi.repository import Soup
import time

URL = "http://golem.de.dynamic.feedsportal.com/pf/578068/http://rss.golem.de/rss.php?tp=av&feed=RSS2.0"

def download(lmdate=None):

    if lmdate is None:
        lmdate = "Mon, 15 Jun 2015 19:37:27 GMT"

    session = Soup.Session()
    message = Soup.Message.new("GET", URL)
    message.request_headers.append("if-modified-since", lmdate)
    r = session.send_message(message)
    print(message.response_body.data)

    print("Status code:", message.status_code)
    return message.response_headers.get("last-modified")


if __name__ == '__main__':
    date = download()
    print("Modified date:", date)
    time.sleep(5)
    date = download(date)
    print("Modified date:", date)
