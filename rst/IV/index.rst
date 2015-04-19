
.. _anforderungen:

*****************************
Anforderungen an die Software 
*****************************

Im Folgenden werden die Anforderungen, die an die Software *gylfeed* 
gestellt werden, definiert. Die Aufteilung erfolgt in allgemeine Anforderungen,
funktionale Anforderungen und Anforderungen an die grafische Benutzeroberfläche.


Allgemeine Anforderungen
========================

Mit *gylfeed* soll ein leichtgewichtiger Feedreader entwickelt werden, an den
folgende allgemeine Anforderungen gestellt werden:

* Die Entwicklung erfolgt unter der GNU General Public License in der Version
  3.0 (vgl. :cite:`GNUGPL` -- offizielle Seite von GNU GPL).
* Entwicklung für Linux-Distributionen
* Entwicklung als Open-Source-Projekt
* Neues Konzept hinsichtlich der grafischen Oberfläche
* Komfortable Bedienung


.. _funkAnf:

Funktionale Anforderungen
=========================

Die funktionalen Anforderungen, die an die Software *gylfeed* gestellt werden, 
sind im Folgenden aufgeführt.


Verwaltung von Feeds
--------------------

**Feed hinzufügen:** Unter Angabe der URL und Eingabe eines Namens wird ein neuer Feed hinzugefügt.
An dieser Stelle wird geprüft, ob der Feed gültige Daten liefert und nicht
bereits vorhanden ist. Kommt es zu einem Fehler, wird dieser mitgeteilt.

**Feed löschen:** Durch die Auswahl eines Feeds besteht die Möglichkeit diesen zu
löschen. 


Optionen für Feeds
------------------
**Automatisches Update:** Für jeden Feed kann entschieden werden, ob dieser
automatisch aktualisiert werden soll.

**Update-Intervall:** Wurde die Einstellung *Automatisches Update* gewählt, kann
zusätzlich eingestellt werden, in welchem Intervall dies geschehen soll.

**Notifications:** Sind neue Nachrichten vorhanden, wird eine Systemnachricht gesendet.

**Automatisches Löschen von Entries nach X Tagen:** Entries, die größer als der
angegebene Wert sind, werden gelöscht.

**Optionen im Nachhinein ändern:** Alle genannten Optionen können im Nachhinein
geändert werden.


Update von Feeds
----------------

**Manuelles Update von Feeds:** Feeds können durch manuelle Ausführung
aktualisiert werden.

**Automatisches Update von Feeds:** Feeds werden im gewählten Intervall
automatisch aktualisiert.

**Der Update-Vorgang soll andere Abläufe nicht blockieren:** Grundsätzlich ist
gefordert, dass der Update-Vorgang wenig Ressourcen beansprucht und andere
Vorgänge, wie beispielsweise die Bedienung der grafischen Oberfläche, nicht
behindert.


Suche
-----

**Suche innerhalb von Feeds:** Ein Feed innerhalb der Liste von Feeds ist
suchbar. Die Ergebnisse werden angezeigt.

**Suche innerhalb von Entries nach Titel:** Ein Entry innerhalb der Liste von
Entries ist suchbar. Die Ergebnisse werden angezeigt.


Bereitstellung von Daten
------------------------

Folgende Daten werden zur Verfügung gestellt:

 * Anzahl der Feeds 
 * Anzahl neuer Entries
 * Anzahl gelesener Entries
 * Anzahl aller Entries
 * Inhalt der Entries


Browserfunktion
---------------

Innerhalb des Feedreaders gibt es eine Funktionalität, die den Inhalt von Links,
darstellt. Es soll möglich sein, innerhalb *gylfeed* den ursprünglichen Artikel,
zu dem der Entry erstellt wurde, anzuzeigen.

Bedienkonzept
-------------
**Navigation mit Tastatur:** Effiziente Bedienung mit der Tastatur. Darunter ist
das Navigieren zwischen den verschiedenen Ansichten und innerhalb der einzelnen
Ansicht zu verstehen.

**Einbindung von Shortcuts:** Shortcuts für häufig genutzte Funktionen.

**Navigation mit Maus:** Neben der Bedienung mit der Tastatur ist es auch
möglich, mit einer Computermaus zu navigieren.


Performance
-----------
Sowohl das Starten der Software als auch das Verhalten während der Laufzeit soll
für den Benutzer angemessen zügig ablaufen.


Anforderungen an die Benutzeroberfläche
=======================================

**Entwicklung nach Gnome Design-Richtlinien:** Grundsätzlich soll sich an den
GNOME Human Interface Guidelines orientiert werden (vgl. :cite:`GIG`). Zur Umsetzung
der grafischen Benutzeroberfläche wird das Gimp Toolkit (GTK) verwendet.

**Minimalistisches Design:** Die GUI soll klar strukturiert sein, es soll nur
das Wesentliche dargestellt werden.

**Kompaktheit der GUI:** Es soll kein an einen Mailclient angelehnter Aufbau der
Benutzeroberfläche entwickelt werden. Hier ist ein neues Konzept zu entwickeln.

**Einfachheit der Bedienung:** Es wird in der Regel nur ein Weg angeboten, dieser sollte der
geeigneste sein. 

**Innovatives Navigationskonzept:** Es wird eine komfortable Navigation
angeboten. Die Benutzeroberfläche muss neben der Navigation per Maus, 
vorallem die Navigation per Tasten umsetzen.

**Ausreichend Feedback geben:** Werden Aktionen ausgeführt, die zur Änderung anderer
Komponenten führen, oder einen Hinweis erfordern, wird sich die GUI anpassen.

**Darstellung der geforderten Funktionalitäten:** Die GUI muss alle geforderten
Funktonalitäten unter :ref:`funkAnf` (Funktionale Anforderungen) darstellen können.




