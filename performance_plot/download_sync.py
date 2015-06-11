# usr/bin/env python3
# encoding:utf8

from gi.repository import Soup
from gi.repository import GLib
from gi.repository import GObject
import timeit
import time
import sys
import pygal


class Downloader():
    def __init__(self):
        self._session = Soup.Session()

    def download_data(self, url):
        print("New URL")
        message = Soup.Message.new("GET", url)
        stream = self._session.send_message(message)
        # print(message.response_body.data)

def read_urllist(filename):
    with open(filename, 'r') as fd:
        return fd.read().splitlines()

def save_to_disk(average, len_urllist):
        try:
            with open('sync_data.txt', 'a') as tf:
                tf.write(str(average) + ",{}\n".format(len_urllist))
                print("Saving data to disk, average:", average)
        except IOError as ie:
            print("Fail to save data {ie}".format(ie=ie))



if __name__ == '__main__':

    url_list = read_urllist(sys.argv[2])

    loader = Downloader()
    #start = int(round(time.time() * 1000))
    result_list = []
    for x in range(int(sys.argv[1])):
        run_sum = 0
        for url in url_list:
            t = timeit.Timer("loader.download_data('{}')".format(url), "from __main__ import Downloader; loader = Downloader()")
            run_sum += t.timeit(number=1)
        result_list.append(run_sum)
    print(result_list)


    sum = 0
    for y in result_list:
        sum = sum + y
        print(sum)

    average = sum/(len(result_list))
    print(average)
    save_to_disk(average, len(url_list))

    chart = pygal.Bar()
    chart.title = "Download Performance"
    #chart.x_labels = map(str, range(4))
    chart.add('Synchron', [1,2,3,4,5,6])
    #chart.add('Asynchron', [0,2,3])
    chart.render_to_file('chart.svg')


    #t = timeit.Timer("download_sync.Downloader.download_data(download_sync.Downloader, download_sync.test_url)", setup)
    #end = int(round(time.time() * 1000))
    #print(end - start)
