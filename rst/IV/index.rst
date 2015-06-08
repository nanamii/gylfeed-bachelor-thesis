
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

Für die genannten Problemstellungen werden im Folgenden Lösungsanzätze
diskutiert.


Synchroner im Vergleich mit asynchronem Ansatz
----------------------------------------------

möglich mit Universal Feedparser, ...

Eine Alternative zum synchronen Download der Daten ist der asynchrone Ansatz.
In Abbildung :num:`syncasync` ist der Ablauf beider Varianten zu sehen. Mit
Hilfe der Abbildung werden beide Varianten vorgestellt und mögliche Vorzüge des
asynchronen Ansatzes erläutert.


.. _syncasync:

.. figure:: ./figs/syncasync.png
    :alt: Schematische Darstellung des synchronen und asynchronen Ansatzes.
    :width: 80%
    :align: center
    
    Schematische Darstellung des synchronen und asynchronen Ansatzes.


Jeder Pfeil beschreibt den Ablauf folgender Aufgaben, die abgearbeitet werden
sollen:

 * Klick auf einen Button, um Download auszulösen
 * Download von Daten
 * grafische Benutzeroberfläche: Daten aktualisieren, Benutzereingaben
   entgegennehmen
    
Der klassische synchrone Ansatz verarbeitet die drei Aufgaben nacheinander. Die
nächste Aufgabe wird erst ausgeführt, sobald die aktuelle beendet ist. Als
erstes wird der Klick auf den Button verarbeitet, anschließend der Download und
abschließend die Belange der grafischen Benutzeroberfläche. Ein
Nachteil dieser Herangehensweise ist, dass während des
Downloads keinerlei Aktualisierungen oder Eingaben auf der grafischen
Benutzeroberfläche getätigt werden können. Da ein Download, im Vergleich zu
einfachen Operationen, wie beispielsweise den Klick auf einen Button, relativ
viel Zeit in Anspruch nimmt, ist das für die Performance der Anwendung suboptimal.

Aus diesem Grund wird der Download häufig manuell in Teilpakete aufgeteilt.
Diese Herangehensweise stellt der zweite Pfeil dar. Hier erfolgt ebenso als
erstes der Klick auf den Button. Anschließend wird der Download, in der
entsprechend angegebenen Größe abgearbeitet. Darauf folgt die Abarbeitung der
Anliegen der grafischen Benutzeroberfläche. Dieser Wechsel zwischen Download und
grafischer Benutzeroberfläche wird bis zum Abschluss des Downloads durchgeführt.
Auf diese Weise kann der Nachteil des klassischen synchronen Ansatzes umgangen
werden. Die grafische Benutzeroberfläche hat immer wieder Gelegenheit
Aktualisierungen durchzuführen und Benutzereingaben entgegenzunehmen. Bei dieser
Herangehensweise kommt jedoch ein anderer Nachteil hinzu. In der Abbildung wird
bereits deutlich, dass dieser Ansatz, im Vergleich zum klassischen synchronen
Ansatz, mehr Zeit in Aspruch nimmt. Nach der Abarbeitung von Aufgaben der
grafischen Benutzeroberfläche kommt es zu Wartezeiten. Ein Grund dafür ist beispielsweise, dass
der Download nicht sofort weitergeführt werden kann ... XX.

Genau an dieser Stelle setzt der asynchrone Ansatz an. Der grundsätzliche
Unterschied zum synchronen Ansatz ist, dass der asynchrone Ansatz nicht wartet,
bis eine Aufgabe abgearbeitet ist. Diese Unterscheidung kann genutzt werden, um
in den Wartephasen andere Aufgaben abzuarbeiten. Das hat zur Folge, dass der
asynchrone Ansatz nicht mehr Zeit in Anspruch nimmt, als der synchrone Ansatz
und zudem den Vorteil bietet, dass verschiedene Aufgaben im Wechsel ausgeführt
werden können. Wie in der Abbildung zu sehen ist, nutzt der asynchrone Ansatz
mögliche Wartezeiten beim Download, um Belange der grafischen Benutzeroberfläche
abzuarbeiten.

Um den Vorteil des asynchronen Ansatzes bei der Performance zu untermauern,
wurden ....



Prüfung auf Änderungen der Feed-Daten 
-------------------------------------

Um zu vermeiden, dass Feed-Daten heruntergeladen werden, die keine
Aktualisierungen enthalten, sind die Attribute *etag* und *lastmodified*
hilfreich. In diesem Zusammenhang soll vorerst der Hintergrund dieser Attribute
geklärt werden. 

Das *Hypertext Transfer Protocol* (HTTP) stellt Methoden zur Verfügungen, die
für die Kommunikation zwischen Client und Server eingesetzt werden. Der Client
sendet eine Anfrage unter Angabe einer dieser Methoden und der Server sendet
eine Antwort. Mit der Methode *GET* stellt der Client die Anfrage, die hinter
der Quelle befindlichen Daten zu senden. Will man lediglich Informationen
zur Quelle und nicht sofort die dazugehörigen Daten mitgeliefert bekommen, ist
die Methode *HEAD* zu verwenden. In diesem Fall liefert der Server den *Header*
der Quelle. Dieser sogenannte Header enthält die Attribute *etag* und
*lastmodified*. Anhand dieser Attribute kann festgestellt werden, ob sich der Inhalt der Quelle
aktualisiert hat.

- Beispiel eines Headers, mit lastmodified bzw. etag.
- Etag, lastmodified erklären



Umsetzung in *gylfeed*
======================

Asynchroner Download mit libsoup
--------------------------------
