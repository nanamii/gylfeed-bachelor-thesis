********************************************
Anforderungen an die Software      *gylfeed*
********************************************



Allgemeine Anforderungen
========================

Entwicklung unter der GPL Lizenz....
Mit *gylfeed* soll ein leichtgewichtiger Feedreader entwickelt werden, an den
folgende allgemeine Anforderungen gestellt werden:





Funktionale Anforderungen
=========================


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

**Updateintervall:** Wurde die Einstellung *Automatisches Update* gewählt, kann
zusätzlich eingestellt werden, in welchem Intervall dies geschehen soll.

**Notifications:** Sind neue Nachrichten vorhanden, wird eine Systemnachricht gesendet.

**Automatisches Löschen von Entries nach X Tagen:** Entries, die größer als der
angegebene Zeitraum sind, werden gelöscht.

**Optionen im Nachhinein ändern:** Alle genannten Optionen können im Nachhinein
geändert werden.


Update von Feeds
----------------

**Manuelles Update von Feeds:** Feeds können durch manuelle Ausführung
aktualisiert werden.

**Automatisches Update von Feeds:** Feeds werden im gewählten Intervall
automatisch aktualisiert.

**Der Update-Vorgang soll andere Abläufe nicht blockieren:**


Suche
-----

**Suche innerhalb Feeds:** Ein Feed innerhalb der Gesamtheit der Feeds ist
suchbar.

**Suche innerhalb Entries nach Titel:** Ein Entry innerhalb der Gesamtheit der
Entries ist suchbar.


Anzeige von Daten
-----------------

Folgende Daten werden angezeigt:

 * Anzahl der Feeds 
 * Anzahl neuer Entries
 * Anzahl gelesener Entries
 * Anzahl aller Entries
 

Anzeige aller Feeds
Anzeige einzelner Feeds

Sortierte Darstellung der Entries
Darstellung des Inhalts des Entries

Browserfunktion innerhalb des Feedreaders
Aufruf von Links zum Entry


Bedienkonzept
-------------
**Navigation mit Tastatur:** Effiziente Bedienung mit der Tastatur.

**Einbindung von Shortcuts:** Shortcuts für häufig genutzte Funktionen.
**Navigation mit Maus:** Neben der Bedienung mit der Tastatur ist es auch
möglich, mit einer Computermaus zu navigieren.




Anforderungen an die Grafische Oberfläche
=========================================

**Entwicklung nach Gnome Design-Richtlinien:** Grundsätzlich soll nach den
GNOME Human Interface Guidelines entwickelt werden :cite:`GIG`.

**Minimalistisches Design:** Die GUI soll nicht überladen wirken, es soll nur
das wesentliche dargestellt werden.

**Kompaktheit der GUI:** 

**Einfachheit der Bedienung:** Es wird in der Regel ein Weg angeboten, dieser sollte der
geeigneste sein.

**Innovatives Navigationskonzept:** Es wird eine komfortable Navigation
angeboten.

**Responsive Design:** Werden Aktionen ausgeführt, die zur Änderung anderer
Komponenten führen, oder einen Hinweis erfordern wird sich die GUI anpassen.



