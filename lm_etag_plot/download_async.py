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
        self._session.props.max_conns = 4096
        self.CHUNK_SIZE = 4 * 1024
        self.counter = 0
        self.loop = GLib.MainLoop()
        self.messages = {}
        self.streams = set()


    def download_data(self, url):
        message = Soup.Message.new("GET", url)
        # message.request_headers.set("connection", "keep-alive")
        document = Document()
        # self.messages[document] = message
        self._session.send_async(
            message, callback=self._get_data_deferred, user_data=(document, url, message)
        )
        return document


    def _get_data_deferred(self, session, result, document_url_msg):
        document, url, msg = document_url_msg
        stream = session.send_finish(result)
        stream.read_bytes_async(
            self.CHUNK_SIZE, 0, callback=self._a_callback, user_data=(document, session, msg)
        )
        self.streams.add(stream)

    def _a_callback(self, source, result, document_session_msg):
        document, session, msg = document_session_msg
        bytes_ = source.read_bytes_finish(result)
        data = bytes_.get_data()
        if not data:
            session.cancel_message(msg, 200)
            document._finish()
            return

        document._append(data)
        source.read_bytes_async(
            self.CHUNK_SIZE, 0, callback=self._a_callback, user_data=(document, session, msg)
        )


    def init_download(self, url_list):
        self.url_cnt = len(url_list) - 1
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
        if self.counter == self.url_cnt:
            self.loop.quit()


def read_urllist(filename):
    with open(filename, 'r') as fd:
        return fd.read().splitlines()

def save_to_disk(document_data, counter):
    try:
        with open("download/"+str(counter)+'.txt', 'w') as tf:
            tf.write(document_data)
            print("Saving data to disk, counter:", counter)
    except IOError as ie:
        print("Fail to save data {ie}".format(ie=ie))


if __name__ == '__main__':

    url_list = read_urllist(sys.argv[1])
    loader = Downloader()
    loader.init_download(url_list)
