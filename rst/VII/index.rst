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
der Version 3.3 umgesetzt. Einerseits, weil Python zahlreiche Vorteile,
vorallem bei kurzem Entwicklungszeitraum, bietet und andererseits, weil sich 
hiermit die Möglichkeit bietet, eine weitere Programmiersprache zu erlernen.
Die Vorteile von Python zusammengefasst:

.. aufzeahlung python vorteile

:Plattformübergreifend:
    
:Umfangreiche Standardbibliothek:    

:Relativ schnell erlernbar:

:Open Source Sprache:

**Tool für Erstellung der GUI:**



   
**Entwicklungssytem:**
Die Software *gylfeed* wird unter der Linux Distribution *Fedora 21* entwickelt. Für die Entwicklung wird der
Editor *gVim* mit entsprechenden Python--Plugins zur Validierung der Python
PEP--Stilrichtlinien (siehe :cite:`pep`) verwendet. Des Weiteren wird die
interaktive Python Shell *IPython* eingesetzt.

**Quellcodeverwaltung:**
Für die Quellcodeverwaltung wird das Versionsverwaltungssystem *git*
eingesetzt. Der Quellcode selbst wird auf dem Hosting--Dienst für
Software--Entwicklungsprojekte *GitHub* (siehe :cite:`github`) gelagert. Das
Projekt ist auf folgender GitHub Seite zu finden:

    * https://github.com/qitta/libhugin

**Projektumfang:**
Der Projektumfang beträgt ca. 3500 *lines of code*,  hinzu kommt noch
die Onlinedokumentation. Eine Statistik zum Projekt, welche mit dem Tool
*cloc* erstellt wurde, ist im Anhang unter :ref:`ref-cloc` zu finden.


**Externe Bibliotheken:**
Die Tabelle :num:`table-libs` listet alle verwendeten externen Abhängigkeiten
für die *libhugin*--Bibliothek.


Download mit libSoup
====================

Der Download der Daten wird mit der Bibliothek ........



Einbindung der Bibliothek Universal Feedparser
==============================================

Zum Parsen der heruntergeladenen Daten wird die Bibliothek *Universal
Feedparser* in der Version 5.1.3 verwendet. Die Bibliothek ermöglicht das
Parsen folgender Formate: RSS 0.9X, 1.0, 2.0; Atom 1.0 und ....


Kommunikation durch Signale
===========================
Zum Benachrichtigen von anderen Instanzen, werden Signale eingesetzt ...


Design der Benutzeroberfläche
=============================




