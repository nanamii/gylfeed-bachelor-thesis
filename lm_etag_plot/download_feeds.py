# usr/bin/env python3
# encoding:utf8

from gi.repository import Soup
from gi.repository import GLib
from gi.repository import GObject
import requests
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
        self.dict_etag = {}
        self.dict_lastmodi = {}

    def download(self, url, check_if_needed=True):
        if check_if_needed:
            # TODO: Async header check.
            header = Soup.Message.new("HEAD", url)
            stream = self._session.send(header)
            stream.read_bytes(self.CHUNK_SIZE)

            etag = self._get_etag(header)
            print("checking etag for ", url)
            if etag and etag == self.dict_etag.get(url):
                return None

            self.dict_etag[url] = etag

            print("checking lastmodi for ", url)
            lastmodi = self._get_lastmodified(header)
            if lastmodi and lastmodi == self.dict_lastmodi.get(url):
                return None

            print("No etag or lastmodi, get all.")
            self.dict_lastmodi[url] = lastmodi

        return self._get_data(url)

    def _get_data(self, url):
        message = Soup.Message.new("GET", url)
        document = Document()
        stream = self._session.send_async(
            message, callback=self._read_stream, user_data=document
        )
        return document


    def _read_stream(self, session, result, document):
        stream = session.send_finish(result)
        stream.read_bytes_async(
            self.CHUNK_SIZE, 0, callback=self._fill_document, user_data=document
        )

    def _fill_document(self, source, result, document):
        bytes_ =  source.read_bytes_finish(result)
        data = bytes_.get_data()
        if not data:
            document._finish()
            return

        document._append(data)
        source.read_bytes_async(
            self.CHUNK_SIZE, 0, callback=self._fill_document, user_data=document
        )

    def _get_etag(self, header):
        return header.response_headers.get("Etag")

    def _get_lastmodified(self, header):
        return header.response_headers.get("Last-Modified")

    
    def read_urllist(filename):
        with open(filename, 'r') as fd:
            return fd.read().splitlines()



if __name__ == '__main__':
    
    url_list = read_urllist(sys.argv[1])
    
    
    loader = Downloader()
    
    for n, url in enumerate(url_list):
    try:
        document = loader.download(url)
        document.connect("finish", lambda doc: print(doc.data, type(doc.data)))
    except:
        print("URL failed", url)
        continue

    
    
    
    
       loop = GLib.MainLoop()
    loop.run()






cnt = {'lm': 0, 'etag': 0, 'both':0, 'all': 0}



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
