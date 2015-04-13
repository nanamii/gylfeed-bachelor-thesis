***************
Zusammenfassung
***************

Zum Zeitpunkt der Abgabe der Projektarbeit liegt eine lauffähige
Implementierung von *gylfeed* vor. Im Folgenden wird nochmals kurz auf
die Erfüllung der gestellten Anforderungen, Verbesserungsmöglichkeiten und
denkbare Erweiterungen eingegangen.


Aktueller Stand des Projekts
============================

Die gestellten Anforderungen wurden in vollem Umfang umgesetzt.
Zusammengefasst sind dies folgende Bereiche:

 * Verwaltung von Feeds
 * Optionen für Feeds
 * Update von Feeds
 * Suche
 * Bereitstellung von Daten
 * Browserfunktion
 * Bedienkonzept
 * Performance
 * Anforderungen an die grafische Benutzeroberfläche

Für Teile dieser umgesetzten Anforderungen gibt es Verbesserungspotential. 
Optimierungen, die sinnvoll erscheinen, werden im folgenden Abschnitt
aufgeführt.


Optimierungsmöglichkeiten
=========================

**Ausnahmebehandlung**: 



Denkbare Erweiterungen
======================

Mögliche Erweiterungen, die noch im Sinne der ursprünglichen Zielsetzung 
von *gylfeed* sind, wären beispielweise:

**Automatischen Vorschlag für Namen des Feeds:** Aktuell wird vom Benutzer
erwartet, dass er den Namen für einen Feed manuell erfasst. Dies erscheint
sicherlich sinnvoll, da der Nutzer möglicherweise einen bestimmten Namen
vergeben möchte. Zusätzlich wär es wünschenswert, dass beim Hinzufügen des
Feeds ein automatischer Vorschlag vorgegeben wird. Das kann beispielsweise
durch die Extraktion aus der URL erfolgen.

**Icon für Feed beschaffen:** Wird aktuell von Seiten des Feeds kein Icon
geliefert, wird ein Standardicon verwendet. Hier wäre eine denkbare Lösung,
für diese Feeds das Icon von der Quell-Webseite zu beschaffen.

**Bearbeitungsfunktionen**: Im Allgemeinen sind noch Funktionalitäten denkbar
, die eine umfassendere Bearbeitung der Inhalte ermöglichen. Beispielsweise
alle Entries global als gelesen markieren, oder Markierung von Entries als
Favoriten.

**webKit für weitere Funktionen nutzen:** Die Engine *webKit* könnte
in größerem Umfang genutzt werden. Denkbar sind hier weiterreichende 
Implementierungen von Browser-Funktionalitäten. Aktuell wird mit 
*webKit* innerhalb der *EntryDetailsView* der Inhalt einer Webseite
dargestellt. Klassische Funktionalitäten, die ein Webbrowser bietet, wie
beispielsweise in der Navigation einen Schritt zurück gehen, wäre eine 
denkbare Erweiterung.

**Einbindung von Datamining:** Eine Interessante Erweiterung wäre die
Einbindung von Datamining-Algorithmik. Denkbar wäre hier die Suche nach 
ähnlichen Inhalten, oder Vorschläge für Inhalte, die für den Benutzer als
potenziell relevant erkannt wurden.


Fazit & Ausblick
================

Abschließend kann festgehalten werden, dass die anfangs gesetzten Ziele für
die Projektarbeit erreicht wurden. Mögliche Verbesserungen und denkbare
Erweiterungen wurden aufgeführt. 

Die Entwicklung von *gylfeed* war teilweise eine Herausforderung, da
einerseits mit Python eine neue Programmiersprache angeeignet werden musste
und GTK mit seiner mächtigen Bibliothek für einen Neueinsteiger nicht
weniger Einarbeitung gefordert hat. Rückblickend auf die Entwicklungszeit 
kann jedoch erwähnt werden, dass es alles in allem eine Bereicherung an
Wissen und Erfahrung gebracht hat. Es ist geplant, die Entwicklung von 
*gylfeed* weiterzuführen und die genannten Verbesserungen umzusetzen.






