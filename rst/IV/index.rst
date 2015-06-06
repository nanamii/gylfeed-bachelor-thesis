
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


Performance der Anwendung
-------------------------

Der Main-Event-Loop, der in Kapitel :ref:`signale` vorgestellt wurde,
verarbeitet Aufgaben grundsätzlich synchron. Bei einer synchronen Verarbeitung,
wird gewartet, bis eine Aufgabe abgeschlossen ist, erst dann wird mit der
Verarbeitung der nächsten Aufgabe begonnen. Bei einer großen Anzahl an Feeds,
für die ein Download der Daten erfolgen soll, kann während der Beschaffung
nichts anderes ausgeführt werden. Die Anwendung ist in diesem Moment
aussschließlich mit dem Download der Feed-Daten beschäftigt. Das bedeutet, dass
sich in dieser Zeit weder die grafische Benutzeroberfläche aktualisieren kann,
noch Benutzereingaben vorgenommen werden können. Für den Benutzer der Anwendung
ist das wenig erfreulich, er bekommt den Eindruck, dass die Anwendung nicht
ausreichend flüssig läuft.


Bandbreite des Downloads
------------------------

Werden bei jeder Aktualisierung, die vom Client angestossen wird, alle Feed-Daten
der Feeds
heruntergeladen, obwohl bei Teilen der Feeds keine Änderung vorliegt, 
benötigt dies unnötige Download-Bandbreite. Auf Seiten des
Clients würde festgestellt, dass keine Aktualisierungen vorliegen. Diese Prüfung
beansprucht zusätzlich unnötige Rechenkapazität.


Fehlerbehandlung
----------------

Beim Download der Feed-Daten können verschiedenste Fehler auftreten. Beispielsweise
ist die URL nicht erreichbar oder der Download wird unterbrochen.




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
