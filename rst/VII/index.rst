***************
Implementierung
***************

Dieses Kapitel wird einen Eindruck von der Umsetzung der 
Entwürfe von Architektur und Benutzeroberfläche geben. Eine detailliertere
Analyse der verwendeten Algorithmik und Umsetzung, ist Teil der Bachelorarbeit.

Grundsätzliches
===============

Bevor auf Details der Implementierung eingegangen wird, soll kurz erläutert
werden, welche Programmiersprache für das Projekt gewählt wurde. Ebenso die
Werkzeuge für die Erstellung der Benutzeroberfläche und die
Entwicklungsumgebung.

**Programmiersprache:** Das Projekt wird mit der Programmiersprache Python in
der Version 3.3 umgesetzt. Einerseits, weil Python zahlreiche Vorteile - 
vorallem bei relativ kurzem Entwicklungszeitraum - bietet und andererseits, weil sich 
hiermit die Möglichkeit bietet, eine weitere Programmiersprache zu erlernen.
Die Vorteile von Python zusammengefasst:

.. aufzeahlung python vorteile

:Plattformübergreifend:
    
:Umfangreiche Standardbibliothek:    

:Relativ schnell erlernbar:

:Open Source Sprache:

**Tool für die Erstellung der GUI:**

Für die Erstellung der grafischen Benutzeroberfläche wird GTK, das GIMP
Toolkit, in der Version 3.14 verwendet. GTK ist plattformunabhängig, dies
bietet den Vorteil, dass *gylfeed* zu einem späteren Zeitpunkt für andere
Plattformen, außerhalb Linux, angeboten werden kann. GTK bietet eine leicht
anzuwendente, jedoch mächtige API. Für die Umsetzung innerhalb der
Projektarbeit wurde auf den Einsatz eines GUI-Builders verzichtet, um GTK
von Grund auf zu erlernen und anzuwenden.

   
**Entwicklungssytem:**
Die Software *gylfeed* wird unter der Linux Distribution *Fedora 21* entwickelt. Für die Entwicklung wird der
Editor *gVim* mit entsprechenden Python--Plugins zur Validierung der Python
PEP--Stilrichtlinien (siehe :cite:`pep`) verwendet. Als weiteres Werkzeug
wird die interaktive Python Shell *IPython* eingesetzt. Das erlaubt das 
Testen von Funktionalitäten außerhalb des eigentlichen Quelltextes.

**Quellcodeverwaltung:**
Zur Verwaltung des Quellcodes wird *git*, ein Versionsverwaltungssystem,
eingesetzt. Der Quellcode selbst wird auf dem Hosting--Dienst für
Software--Entwicklungsprojekte *GitHub* (siehe :cite:`github`) gelagert. Das
Projekt ist über folgenden Link zur GitHub-Seite erreichbar:

    * https://github.com/nanamii/gylfeed 
/
**Projektumfang:**
Der Projektumfang beträgt ca. 3500 *lines of code*,  hinzu kommt noch
die Onlinedokumentation. Eine Statistik zum Projekt, welche mit dem Tool
*cloc* erstellt wurde, ist im Anhang unter :ref:`ref-cloc` zu finden.


**Externe Bibliotheken:**
Die Tabelle :num:`table-libs` listet alle verwendeten externen Abhängigkeiten
für die *libhugin*--Bibliothek.


Implementierte Anforderungen
============================

Die Anforderungen aus Kapitel XX wurden in vollem Umfang implementiert. Es
wurde in der Weise entwickelt, dass zur Abgabe der Projektarbeit eine
lauffähige Software vorliegt. Selbstverständlich sind noch weitere
Funktionalitäten denkbar, die innerhalb des beschränkten Projektzeitraums
nicht umgesetzt werden konnten. Auf Erweiterungen, die noch denkbar sind,
wird in der Zusammenfassung eingegangen.


Einblick in die Implementierung
===============================

Im Folgenden wird ein Einblick in die Implementierung von *gylfeed* gegeben.


Implementierung der Klassen
---------------------------

Die Klassen wurden anhand des Klassendiagramms XX implementiert. Folgend sind
die Klassen, die mit Python implementiert wurden, aufgeführt.

Download mit *libsoup*
----------------------

Der Download der Daten wird mit der Bibliothek *libsoup* umgesetzt. 
*libsoup* ist eine client-/serverseitige HTTP-Bibliothek und ermöglicht
innerhalb *gylfeed* das asynchrone Herunterladen der Feed-Daten.  

Die im Folgenden aufgeführte Bibliothek *Universal Feedparser* ermöglicht zwar
das direkte Herunterladen und anschließende Parsen eines Feeds, jedoch nur
synchron. Eine Anforderung an *gylfeed* ist, dass das Herunterladen der Daten
andere Prozesse nicht behindert. Werden die Daten synchron heruntergeladen,
blockt dies solange, bis der Download abgeschlossen ist. Aus diesem Grund erfolgt
eine Trennung zwischen Download und Parsen der Daten. Der Download erfolgt mit
*libsoup*, das Parsen mit *Universal Feedparser*.


Einbindung der Bibliothek *Universal Feedparser*
------------------------------------------------

Zum Parsen der heruntergeladenen Daten wird die externe Bibliothek *Universal
Feedparser* in der Version 5.1.3 verwendet. Die Bibliothek ermöglicht das
Parsen folgender Formate: RSS 0.90, 0.91, 0.92, 0.93, 0.94, 1.0, 2.0; 
Atom 0.3 und 1.0; CDF (Common Data Format). 

In *Developing Feeds with RSS and Atom* (siehe :cite:`DFRA`) erwähnt Ben
Hammersley den *Universal Feedparser* als 
hervorragend umgesetzten und großartig dokumentierten Feedparser. Tatsächlich
kann beim Benutzen des *Universal Feedparser* festgestellt werden, dass eine
ordentliche Dokumentation vorliegt (siehe :cite:`FPD` - Online Dokumentation).

Der *Universal Feedparser* ermöglicht das Parsen eines Feeds auf folgende
drei Arten:
 * Parsen des Feeds über die URL: Der Feedparser übernimmt hier auch das 
   Herunterladen der Daten, jedoch nur synchron.
 * Parsen des Feeds aus einer lokal gespeicherten Datei
 * Parsen des Feeds aus einem String

Alle drei Wege liefern ein Objekt vom Typ feedparser.FeedParserDict. Es
handelt sich um ein Dictionary mit den geparsten Feed-Daten.

Folgendes Code-Beispiel einer bpython-Sitzung soll die Grundfunktionaliät 
*parse* demonstrieren.


.. code-block:: python

    import feedparser

    # Der Funktion *parse* wird die URL vom Feed der 
    # Sueddeutschen Zeitung übergeben und der Variable *feed_dict* zugewiesen
    >>> feed_dict = feedparser.parse("http://suche.sueddeutsche.de/?output=rss")

    # Zugriff auf den Wert, des Schlüssels *title*
    >>> feed_dict["feed"]["title"]

    # Ausgabe: Titel des Feeds der Sueddeutschen Zeitung
    'Alle Artikel - Nachrichten aus Politik, Wirtschaft und Sport' 


In Anhang :ref:`dict` ist die komplette Struktur des Dictionary zu sehen. Innerhalb
*gylfeed* ist dieses Dictionary Teil eines jeden Feedobjekts.


Eingebetteter Browser mit *Webkit*
----------------------------------

Innerhalb von *gylfeed* ist es möglich, Webseiten darzustellen. Umgesetzt
wird dies mit der HTML-Rendering Engine *WebKit* (siehe :cite:`WebKit`). Die aktuelle Version von
*gylfeed* ermöglicht innerhalb der *EntryDetailsView* die Darstellung von
Webinhalten. Der Benutzer kann den originalen
Artikel zur jeweiligen Feed-Nachricht aufrufen. An dieser Stelle bieten sich
für *gylfeed* auch zukünftige Erweiterungen, die durch die Verwendung von
*WebKit* möglich sind.


Kommunikation durch Signale
---------------------------
Zum Benachrichtigen von anderen Instanzen, werden Signale eingesetzt ...


Umsetzung der grafischen Benutzeroberfläche
===========================================

Im Folgenden wird die Umsetzung der grafischen Benutzeroberfläche vorgestellt
. Im Grunde wurden die Entwürfe aus Kapitel XX mit GTK umgesetzt. Für Feeds,
die kein Icon liefern, wurde ein Standardicon entworfen, dass sich an das RSS
-Logo anlehnt. Auch für die Listbox Row *All Feeds* wurde ein Icon entworfen.
Entsprechende Details werden anhand der Ansichten erläutert.


.. _feedview:

.. figure:: ./figs/feedview.png
    :alt: Implementierte Ansicht *FeedView*.
    :width: 70%
    :align: center
    
    Implementierte Ansicht *Feedview*.


.. _entrylistview:

.. figure:: ./figs/entrylistview.png
    :alt: Implementierte Ansicht *EntryListView*.
    :width: 70%
    :align: center
    
    Implementierte Ansicht *EntryListView*.


.. _feedoptionsview:

.. figure:: ./figs/feedoptionsview.png
    :alt: Implementierte Ansicht *FeedOptionsView*.
    :width: 70%
    :align: center
    
    Implementierte Ansicht *FeedOptionsView*.


Testumgebung
============
Zum Testen .....





