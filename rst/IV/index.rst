
.. _beschaffung:

**************************
Beschaffung der Feed-Daten 
**************************

Bevor es zur Verarbeitung und der Anzeige der Feed-Daten kommt, müssen diese
Daten beschafft werden. Worum es sich bei diesen Daten genauer handelt und auf
welche Weise diese Daten beschafft werden können, wird innerhalb diese
Kapitels näher betrachtet.


Ausgangssituation und Problemstellungen
=======================================

- Performance
- update nur, wenn neue Daten vorhanden sind
- Daten liegen in XML vor

In Abbildung :num:`feedprinzip` ist das
Funktionsprinzip eines Newsfeeds dargestellt. Es wird angenommen, dass eine
beliebige Webseite ihre Änderungen über einen Newsfeed mitteilt. 
Die Daten eines Feeds liegen im Regelfall als XML-Datei vor. Aktualisiert die Webseite ihre
Inhalte, werden die Änderungen der XML-Datei hinzugefügt. Zugänglich wird
diese XML-Datei über eine URL gemacht. Die XML-Datei liegt auf einem Webserver und
soll heruntergeladen werden. Der Feedreader fragt in regelmäßigen Abständen beim
Webserver an und holt sich die aktualisierte XML-Datei. An dieser
Stelle wird deutlich, dass sich der Client die Daten beschaffen muss.
Anschließend verarbeitet der Feedreader die XML-Datei und zeigt dem Benutzer die Inhalte an. 


.. _feedprinzip:

.. figure:: ./figs/feedprinzip.png
    :alt: Funktionsprinzip eines Newsfeeds.
    :width: 80%
    :align: center
    
    Funktionsprinzip eines Newsfeeds.

    
Bei der Beschaffung der Feed-Daten ergeben sich folgende Problemstellungen:


Performance
-----------

Ab einer bestimmten Anzahl an Feeds, für die eine Beschaffung der Daten erfolgen soll,
treten Schwierigkeiten bei der Download-Performance auf. Dies ist vorallem dann
der Fall, wenn sich für eine synchrone Umsetzung des Downloads entschieden wird.


Lösungsansätze
==============

Synchroner im Vergleich mit asynchronem Ansatz
----------------------------------------------

beschreiben, Ablauf etc.
möglich mit Universal Feedparser, ...
In Abbildung :num:`syncasync` ist der zeitliche Ablauf einer synchronen und
asynchronen Ausführung zu sehen.


.. _syncasync:

.. figure:: ./figs/syncasync.png
    :alt: Schematische Darstellung des synchronen und asynchronen Ansatzes.
    :width: 80%
    :align: center
    
    Schematische Darstellung des synchronen und asynchronen Ansatzes.



Asynchroner Download
--------------------
beschreiben, Ablauf etc.
möglich mit libsoup, ...


Prüfung auf Änderungen 
----------------------

etag und lastmodified

Umsetzung in *gylfeed*
======================

Asynchroner Download mit libsoup
--------------------------------
