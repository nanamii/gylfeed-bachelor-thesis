# usr/bin/env python3
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
        self.messages = {}
        self.streams = set()


    def download_data(self, url):
        print("NEW URL xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        message = Soup.Message.new("GET", url)
        document = Document()
        self.messages[document] = message
        self._session.send_async(
            message, callback=self._get_data_deferred, user_data=document
        )
        return document


    def _get_data_deferred(self, session, result, document):
        stream = session.send_finish(result)
        stream.read_bytes_async(
            self.CHUNK_SIZE, 0, callback=self._a_callback, user_data=document
        )
        self.streams.add(stream)

    def _a_callback(self, source, result, document):
        bytes_ = source.read_bytes_finish(result)
        data = bytes_.get_data()
        if not data:
            document._finish()
            return

        document._append(data)
        source.read_bytes_async(
            self.CHUNK_SIZE, 0, callback=self._a_callback, user_data=document
        )


    def init_download(self, url_list):
        for count, url in enumerate(url_list):
            try:
                print(count, url)
                document = self.download_data(url)
            except:
                print("URL failed")
            document.connect("finish", self.count_to_disk)
        self.loop.run()


    def count_to_disk(self, document):
        self.counter += 1
        save_to_disk(document.data.decode("utf8"), self.counter)
        print("counter: ", self.counter)
        if self.counter == 7000:
            self.loop.quit()


def read_urllist(filename):
    with open(filename, 'r') as fd:
        return fd.read().splitlines()

def save_to_disk(document_data, counter):
        try:
            with open("download/"+str(counter)+'.txt', 'w') as tf:
                tf.write(document_data)
                #print("Saving data to disk, counter:", counter)
        except IOError as ie:
            print("Fail to save data {ie}".format(ie=ie))





if __name__ == '__main__':

    url_list = read_urllist(sys.argv[1])
    loader = Downloader()
    loader.init_download(url_list)



