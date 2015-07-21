#!/usr/bin/env python3
# encoding:utf8

from gi.repository import Soup
from gi.repository import GLib
from gi.repository import GObject
import timeit
import sys


class Document(GObject.Object):
    __gsignals__ = {
        'finish': (GObject.SIGNAL_RUN_FIRST, None, ())
    }

    def __init__(self):
        GObject.Object.__init__(self)
        self._document = b''

    def _append(self, chunk):
        self._document += chunk

    def _finish(self):
        self.emit('finish')

    @property
    def data(self):
        return self._document


class Downloader():
    def __init__(self):
        self._session = Soup.Session()
        self.CHUNK_SIZE = 16 * 1024
        self.counter = 0
        self.loop = GLib.MainLoop()


    def download_data(self, url):
        print("NEW URL xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        message = Soup.Message.new("GET", url)
        document = Document()
        stream = self._session.send_async(
            message, callback=self._get_data_deferred, user_data=document
        )
        return document


    def _get_data_deferred(self, session, result, document):
        stream = session.send_finish(result)
        stream.read_bytes_async(
            self.CHUNK_SIZE, 0, callback=self._a_callback, user_data=document
        )

    def _a_callback(self, source, result, document):
        bytes_ =  source.read_bytes_finish(result)
        data = bytes_.get_data()
        if not data:
            document._finish()
            return

        document._append(data)
        source.read_bytes_async(
            self.CHUNK_SIZE, 0, callback=self._a_callback, user_data=document
        )


    def init_download(self, url_list):
        for url in url_list:
            document = self.download_data(url)
            #document.connect("finish", lambda doc: print(doc.data, type(doc.data)))
            document.connect("finish", self.do_counter)
        self.loop.run()


    def do_counter(self, document):
        self.counter += 1
        print("counter: ", self.counter)
        if self.counter == 40:
            self.loop.quit()


def read_urllist(filename):
    with open(filename, 'r') as fd:
        return fd.read().splitlines()

def save_to_disk(average, url_count):
        try:
            with open('async_data.txt', 'a') as tf:
                tf.write(str(average)+",{}\n".format(url_count))
                print("Saving data to disk, average:", average)
        except IOError as ie:
            print("Fail to save data {ie}".format(ie=ie))





if __name__ == '__main__':

    url_list = read_urllist(sys.argv[2])
    run = int(sys.argv[1])
    print(run)

    result_list = []
    for y in range(run):
        t = timeit.Timer("loader.init_download({})".format(url_list), "from __main__ import Downloader; loader = Downloader()")
        time = t.timeit(number=1)
        print(time)
        result_list.append(time)

    sum = 0
    for y in result_list:
        sum = sum + y
        print(sum)

    average = sum/(len(result_list))
    print("average: ", average)
    save_to_disk(average, len(url_list))


