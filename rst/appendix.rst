.. raw:: latex

   \appendix

Anhang A
========
Die Feedparser *QuiteRSS* und *RSSOwl* als weitere Beispiele von 
Desktop-Feedreadern, die an den Aufbau eines Mailclients angelehnt sind.

.. _quiterss:

.. figure:: ./figs/quite_rss.png
    :alt: Benutzeroberfläche des Feedreaders *QuiteRSS*
    :width: 70%
    :align: center
    
    Benutzeroberfläche des Feedreaders *QuiteRSS*.


.. figure:: ./figs/rss_owl.jpg
    :alt: Benutzeroberfläche des Feedreaders *RSSOwl*
    :width: 70%
    :align: center
    
    Benutzeroberfläche des Feedreaders *RSSOwl*, Quelle: http://www.heise.de/.



.. _dict:

Struktur des Feedparser-Objekts
===============================


Struktur des Feedparser-Objekts, Rückgabewert der Funktion *parse*
des *Universal Feedparsers*.

.. code-block:: xml

    {   bozo,
        bozo_exception,
        encoding,
        entries
        [
           {
            entries[i].author
            entries[i].author_detail
            entries[i].comments
            entries[i].content
            entries[i].contributors
            entries[i].created
            entries[i].created_parsed
            entries[i].enclosures
            entries[i].expired
            entries[i].expired_parsed
            entries[i].id
            entries[i].license
            entries[i].link
            entries[i].links
            entries[i].published
            entries[i].published_parsed
            entries[i].publisher
            entries[i].publisher_detail
            entries[i].source
            entries[i].summary
            entries[i].summary_detail
            entries[i].tags
            entries[i].title
            entries[i].title_detail
            entries[i].updated
            entries[i].updated_parsed
            entries[i].vcard
            entries[i].xfn
            }
        ]
        etag
        feed
            {
            feed.author
            feed.author_detail
            feed.cloud
            feed.contributors
            feed.docs
            feed.errorreportsto
            feed.generator
            feed.generator_detail
            feed.icon
            feed.id
            feed.image
            feed.info
            feed.info_detail
            feed.language
            feed.license
            feed.link
            feed.links
            feed.logo
            feed.published
            feed.published_parsed
            feed.publisher
            feed.publisher_detail
            feed.rights
            feed.rights_detail
            feed.subtitle
            feed.subtitle_detail
            feed.tags
            feed.textinput
            feed.title
            feed.title_detail
            feed.ttl
            feed.updated
            feed.updated_parsed
            }
        headers
        href
        modified
        namespaces
        status
        version
    }


Anhang C
========

