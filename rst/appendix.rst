.. raw:: latex

   \appendix


.. _performancesync:

Performancetest, synchroner Ansatz
==================================

Folgender Python-Code wurde zur Performance-Messung des synchronen Downloads
eingesetzt.

.. code-block:: python

    #!/usr/bin/env python3
    # encoding:utf8

    from gi.repository import Soup
    from gi.repository import GLib
    from gi.repository import GObject
    import timeit, time, sys

    class Downloader():
        def __init__(self):
            self._session = Soup.Session()

        def download_data(self, url):
            message = Soup.Message.new("GET", url)
            stream = self._session.send_message(message)
        
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
        result_list = []
        for x in range(int(sys.argv[1])):
            run_sum = 0
                for url in url_list:
                    t = timeit.Timer("loader.download_data('{}')".format(url),
                    "from __main__ import Downloader; loader = Downloader()")
                    run_sum += t.timeit(number=1)
                result_list.append(run_sum)
                print(run_sum)
            print(result_list)

            sum = 0
            for y in result_list:
                sum = sum + y
                print(sum)

            average = sum/(len(result_list))
            save_to_disk(average, len(url_list))


.. _performanceasync:

Performancetest, asynchroner Ansatz
===================================

Folgender Python-Code wurde zur Performance-Messsung des asynchronen Downloads
eingesetzt.

.. code-block:: python

    #!/usr/bin/env python3
    # encoding:utf8

    from gi.repository import Soup
    from gi.repository import GLib
    from gi.repository import GObject
    import timeit, sys

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
                document.connect("finish", self.do_counter)
            self.loop.run()

        def do_counter(self, document):
            self.counter += 1
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

        result_list = []
        for y in range(run):
            t = timeit.Timer("loader.init_download({})".format(url_list),
            "from __main__ import Downloader; loader = Downloader()")
            time = t.timeit(number=1)
            result_list.append(time)

        sum = 0
        for y in result_list:
            sum = sum + y

        average = sum/(len(result_list))
        save_to_disk(average, len(url_list))


.. _etaglastmodi:  

Stichprobentest: *ETag* und *last-modified*
===========================================

Das Vorkommen von *ETag* und *last-modified* in HTTP-Headern wurde mit folgendem
Python-Code getestet.

.. code-block:: python

     #!/usr/bin/env python3
     # encoding:utf8

     from gi.repository import GLib
     from gi.repository import GObject
     import requests, sys


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
                 cnt['lm'] += 1
             if 'etag' in r.headers:
                 cnt['etag'] += 1
             if 'last-modified' in r.headers and 'etag' in r.headers:
                 cnt['both'] += 1

     print(cnt)



.. _feedtest:

Stichprobentest: Feedformate
============================

Folgender Python-Code wurde zum Test auf die Häufigkeit der Feedformate
verwendet.

.. code-block:: python

    #!/usr/bin/env python
    # encoding:utf8

    from collections import defaultdict
    import os, sys, feedparser

    absPath = os.path.abspath(sys.argv[1])
    files = os.listdir(sys.argv[1])

    d = defaultdict(int)
    counter = 0

    for file_ in files:
        feed = feedparser.parse(os.path.join(absPath, file_))
        d[feed.version] += 1
        d[counter] += 1
        print(d)


.. _testinhaltselemente:

Stichprobentest: Inhaltselemente
================================

Mit folgendem Python-Code wurde der Test auf das Vorkommen verschiedener
XML-Elemente durchgeführt.

.. code-block:: python

   #!/usr/bin/env python
   # encoding:utf8

   from collections import defaultdict
   import os, sys, feedparser

   absPath = os.path.abspath(sys.argv[1])
   files = os.listdir(sys.argv[1])

   d = defaultdict(int)

   def check_entries(feed, attr, d):
       try:
           if attr == "title" and feed.entries[0].title:
               d["title"] += 1
           if attr == "summary" and feed.entries[0].summary:
               d["summary"] += 1
           if attr == "author" and feed.entries[0].author:
               d["author"] += 1
           if attr == "updated_parsed" and feed.entries[0].updated_parsed:
               d["updated_parsed"] += 1
           if attr == "id" and feed.entries[0].id:
               d["id"] +=1
           if attr == "link" and feed.entries[0].link:
               d["link"] +=1
       except Exception as e:
           print(e)

   def check_feed(feed, attr, d):
       try:
           if attr == "icon" and feed.feed.icon:
               d["icon"] += 1
           if attr == "image" and feed.feed.image:
               d["image"] += 1
           if attr == "logo" and feed.feed.logo:
               d["logo"] += 1
       except Exception as e:
           print(e)

   for file_ in files:
       feed = feedparser.parse(os.path.join(absPath, file_))
       d["counter"] +=1

       attr_entries = ["title", "summary", "author", "updated_parsed", "id", "link"]
       attr_feed = ["icon", "image", "logo"]

       for attr in attr_entries:
           check_entries(feed, attr, d)

       for attr in attr_feed:
           check_feed(feed, attr, d)

       print(d) 



.. _anforderungrss2:

Test: Anforderung RSS 2.0 Spezifikation
=======================================

Der folgende Python-Code wurde zur Prüfung der Anforderung aus der RSS 2.0
Spezifikation verwendet. Diese fordert, dass mindestens eines der Attribute
*title* oder *description* bezüglich einer Nachricht vorhanden sein sollte.

.. code-block:: python

    #!/usr/bin/env python
    # encoding:utf8

    from collections import defaultdict
    import os, sys, feedparser

    absPath = os.path.abspath(sys.argv[1])
    files = os.listdir(sys.argv[1])

    d = defaultdict(int)

    def check_entries(feed, attr, d):
        try:
            if attr == "title" and feed.entries[0].title:
                d["title"] += 1
                if feed.entries[0].summary:
                    d["title and summary"] += 1
            if attr == "summary" and feed.entries[0].summary:
                d["summary"] += 1
                if feed.entries[0].title:
                    d["title and summary, validation"] += 1
        except Exception as e:
            print(e)

    for file_ in files:
        feed = feedparser.parse(os.path.join(absPath, file_))
        d["counter"] +=1
        if feed.version == 'rss20':
            attr_entries = ["title", "summary"]

            for attr in attr_entries:
                check_entries(feed, attr, d)
            print(d)





.. _heruntergeladenedatenanhang:
    
Unverarbeitete Feed-Daten
=========================

Der folgende Byte-String enthält die XML-Daten zum Feed der Sueddeutschen
Zeitung. Das sind die unbearbeiteten Daten, die das Objekt *Feed* zum Parsen
erhält.

.. code-block:: xml

   b'<?xml version="1.0" encoding="UTF-8" ?>\n
   <rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">\n  
   <channel>\n    
       <title>Alle Artikel - Nachrichten aus Politik, Wirtschaft und Sport</title>\n    
       <link>http://www.sueddeutsche.de</link>\n    
       <description>aktuelle Nachrichten, Kommentare und Huntergrundberichte 
       online auf sueddeutsche.de</description>\n    
       <pubDate>Tue, 21 Jul 2015 21:12:00 +0200</pubDate>\n    
       <managingEditor>wir@sueddeutsche.de 
       (S\xc3\xbcddeutsche Zeitung Digitale Medien GmbH)</managingEditor>\n    
       <language>de</language>\n    
       <image>\n      
           <url>http://polpix.sueddeutsche.com/staticassets/img/siteheader/logo_rss.png
           </url>\n      
           <title>Artikel / S\xc3\xbcddeutsche.de</title>\n      
           <link>http://www.sueddeutsche.de/</link>\n      
           <width>144</width>\n      
           <height>20</height>\n    
       </image>\n    
       <item>\n      
            <link>http://sz.de/1.2576678</link>\n      
            <title><![CDATA[T\xc3\xb6lzer Pr\xc3\xbcgel: Minigolf im Kurpark]]></title>\n
            <description><![CDATA[Alles so still. Gabriel von Seidls B\xc3\xbcste wacht 
            \xc3\xbcber die Ruhe. Vielleicht sollte er einmal einen kleinen 
            wei\xc3\x9fen Ball auf die Nase bekommen...]]></description>\n      
            <guid isPermaLink="false">http://sz.de/1.2576678</guid>\n      
            <pubDate>Tue, 21 Jul 2015 21:12:00 +0200</pubDate>\n\n    
       </item>\n
       <item> ... </item>
   </channel>\n
   </rss>'


.. _geparstedatenanhang:

Geparste Feed-Daten
===================

Im Folgenden ist das Ergebnis der Funktion *parse* des Universal Feedparser zu
sehen, ein Dictionary mit Feed-Daten zum Feed der Sueddeutschen Zeitung. 

.. code-block:: xml

   {'bozo': 0, 
   'namespaces': {'content': 'http://purl.org/rss/1.0/modules/content/'}, 
   'feed': {'author': 'wir@sueddeutsche.de (Süddeutsche Zeitung Digitale Medien GmbH)', 
           'authors': [{}], 
           'subtitle_detail': {'language': None, 'base': '', 
           'value': 'aktuelle Nachrichten, Kommentare und Huntergrundberichte 
            online auf sueddeutsche.de', 'type': 'text/html'}, 
           'title_detail': {'language': None, 'base': '', 
               'value': 'Alle Artikel - Nachrichten aus Politik, 
               Wirtschaft und Sport', 'type': 'text/plain'},
           'title': 'Alle Artikel - Nachrichten aus Politik, Wirtschaft und Sport', 
           'published': 'Tue, 21 Jul 2015 21:12:00 +0200', 
           'link': 'http://www.sueddeutsche.de', 
           'subtitle': 'aktuelle Nachrichten, Kommentare und Huntergrundberichte 
           online auf sueddeutsche.de', 
           'links': [{'rel': 'alternate', 'href': 'http://www.sueddeutsche.de', 
                   'type': 'text/html'}], 
           'published_parsed': time.struct_time(tm_year=2015, tm_mon=7, tm_mday=21, 
           tm_hour=19, tm_min=12, tm_sec=0, tm_wday=1, tm_yday=202, tm_isdst=0), 
           'author_detail': {'name': 'Süddeutsche Zeitung Digitale Medien GmbH', 
           'email': 'wir@sueddeutsche.de'}, 
           'language': 'de',
           'image': {'width': 144, 'link': 'http://www.sueddeutsche.de/', 
                   'href': 'http://polpix.sueddeutsche.com/staticassets/img/
                   siteheader/logo_rss.png', 
                   'links': [{'rel': 'alternate', 'href': 'http://www.sueddeutsche.de/', 
                   'type': 'text/html'}], 
                   'height': 20, 
                   'title_detail': {'language': None, 'base': '', 
                   'value': 'Artikel / Süddeutsche.de', 'type': 'text/plain'}, 
                   'title': 'Artikel / Süddeutsche.de'}}, 
   'version': 'rss20', 'encoding': 'utf-8', 
   'entries': [
           {'summary_detail': {'language': None, 'base': '', 
           'value': 'Alles so still. Gabriel von Seidls Büste wacht über die Ruhe. 
           Vielleicht sollte er einmal einen kleinen weißen Ball auf 
           die Nase bekommen...', 'type': 'text/html'}, 
           'link': 'http://sz.de/1.2576678', 
           'published_parsed': time.struct_time(tm_year=2015, tm_mon=7, tm_mday=21, 
           tm_hour=19, tm_min=12, tm_sec=0, tm_wday=1, tm_yday=202, tm_isdst=0), 
           'guidislink': False, 
           'published': 'Tue, 21 Jul 2015 21:12:00 +0200', 
           'links': [{'rel': 'alternate', 'href': 'http://sz.de/1.2576678', 
           'type': 'text/html'}], 
           'summary': 'Alles so still. Gabriel von Seidls Büste wacht über die Ruhe. 
           Vielleicht sollte er einmal einen kleinen weißen Ball 
           auf die Nase bekommen...', 
           'id': 'http://sz.de/1.2576678', 
           'title_detail': {'language': None, 'base': '', 'value': 'Tölzer Prügel: M 
           Prügel: Minigolf im Kurpark', 'type': 'text/plain'}, 
           'title': 'Tölzer Prügel: Minigolf im Kurpark'}, 
           }]
   }
