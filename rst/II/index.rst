.. _ch-refs:

================================
Überblick zum Feedreader gylfeed
================================

Um zu einem späteren Zeitpunkt auf tiefergehende interne Abläufe und die Theorie
des Feedreaders *gylfeed* eingehen zu können, werden im Folgenden das Grundkonzept
und wesentliche Eigenschaften von *gylfeed* erläutert.


Entstehung und Motivation
=========================

Der Feedreader *gylfeed* ist eine Desktopanwendung, die es ermöglicht, Newsfeeds
zu abonnieren und zu verwalten. Entwickelt wurde dieser Feedreader
innerhalb der Projektarbeit *Entwurf und Implementierung eines Feedreaders*
(vgl. :cite:`SKP`). Innerhalb der Projektarbeit wurden die Anforderungen an den
Feedreader definiert, ein Entwurf der Softwarearchitektur, sowie ein Entwurf der
grafischen Benutzeroberfläche erstellt. Anschließend erfolgte die
Implementierung der Entwürfe.

Eine Analyse der bestehenden Feedreader hat ergeben, dass sich ein Großteil der
Feedreader dem klassischen Design eines Mailclients bedienen (vgl. :cite:
bestimmte Stelle). Die Motivation für den Entwurf und die Umsetzung von
*gylfeed* bestand darin, einerseits eine alternative Lösung für den
Aufbau der grafischen Benutzeroberfläche zu entwickeln und andererseits eine
komfortable Bedienung anzubieten.


Leistungsumfang
===============

Zusammengefasst bietet der Feedreader *gylfeed* folgende Funktionalitäten:

 * Verwaltung von Feeds: Hinzufügen, ändern, löschen eines Feeds.
 * Optionen für Feeds: Update-Intervall, Notifications, Automatisches Löschen
   von Entries nach X Tagen.
 * Update von Feeds: Manuelles Update, automatisches Update.
 * Suche nach Inhalten
 * Eingebetteter Webbrowser
 * Bedienkonzept: Navigation mit Tastatur, Einbindung von Shortcuts.
 * Bereitstellung sämtlicher Daten für die Darstellung auf der grafischen
   Benutzeroberfläche.


Für die grafische Benutzeroberfläche wurden folgende Anforderungen umgesetzt:
 
 * Entwicklung nach GNOME Design-Richtlinien
 * Minimalistisches Design
 * Kompaktheit
 * Innovatives Navigationskonzept
 * Ausreichend Feedback geben
 * Darstellung der Funktionalitäten

Eine ausführlichere Beschreibung der Funktionalitäten und Anforderungen an die
grafische Benutzeroberfläche ist in der
Projektarbeit in Kapitel *Anforderungen an gylfeed* XXXX zu finden.
 
Implementierung
===============

Die Umsetzung von *gylfeed* erfolgte mit der Programmiersprache Python in der
Version 3.3. Die grafische Benutzeroberfläche wurde mit GTK3, dem Gimp Toolkit,
umgesetzt.

Es wurden die in Abbildung :cite:`klassendiagramm` dargestellten Klassen
implementiert.

.. _klassendiagramm:

.. figure:: ./figs/klassendiagramm.png
    :alt: Klassenübersicht von gylfeed.
    :width: 100%
    :align: center
    
    Klassenübersicht von *gylfeed*.



Grundkonzept von *gylfeed*
==========================

In Abbildung :num:`funktionsprinzip` ist das Funktionsprinzip von *gylfeed*
dargestellt. Anhand dieser Darstellung soll ein Grundverständnis für den 
Aufbau und die Abläufe innerhalb des Feedreaders geschaffen werden.

.. _funktionsprinzip:

.. figure:: ./figs/funktionsprinzip.png
    :alt: Funktionsprinzip von gylfeed.
    :width: 100%
    :align: center
    
    Funktionsprinzip von *gylfeed*.


Die Nummerierungen der Aktionen dienen zur Orientierung und werden an dieser
Stelle verwendet, um mit der Beschreibung des Diagramms zu beginnen.

Es wird angenommen, im Objekt Feed wird gefordert ein Update durchzuführen (1).
Dieser Auftrag wird an den Downloader weitergegeben. Dieser lädt die angefragten
Daten über das Web herunter (2). An dieser Stelle ist anzumerken, dass hier nicht
immer die kompletten Daten des Feeds heruntergeladen werden. Lässt es
die Struktur des betreffenden Feeds zu, wird nur dann ein kompletter Download
der Daten des Feeds durchgeführt, wenn sich dieser tatsächlich geändert hat.
Hier gibt es verschiedene Möglichkeiten festzustellen, ob eine Änderung vorliegt,
dies wird innerhalb des Kapitels XX!!!!! näher betrachtet.


Im nächsten Schritt empfängt der Downloader die Daten aus dem Web (3). 
Document wird vom Downloader als Future-Objekt verwendet (4).
Die Instanz des Documents wird an den Feed zur weiteren
Verarbeitung gegeben (5). Das Weiterverarbeiten im Feed wird dadurch ausgelöst,
indem sich der Feed auf ein Signal von der Instanz Document registriert. Sobald
das Document komplett heruntergeladen ist, wird das entsprechende Signal
ausgelöst und die im Document enthaltenen Daten werden im Feed geparst (6).
Signale werden im Anschluss an die Beschreibung der Abbildung näher erläutert.

Der Feed kommuniziert an den Feedhandler, dass er sich aktualisiert hat. Der
Feedhandler reicht das Signal an die Benutzeroberfläche weiter. Die Änderungen
werden grafisch dargestellt.

Im Feedhandler werden Updates ausgelöst, die manuell vom Benutzer angefordert
werden. Da dies für alle Feeds geschieht, ist es die Aufgabe des Feedhandlers, der
als Verwalter der Feeds funktioniert. Er lässt für jeden Feed eine
Aktualisierung durchführen. Die Aktualisierung im Feed selbst entspricht dem
Ablauf von den genannten Schritten (1) bis (6). Eine weitere Aufgabe des
Feedhandlers ist die persistente Speicherung der Daten, sowie das Laden dieser
Daten beim Start der Software.

Die Benutzeroberfläche kommuniziert Eingaben des Benutzers unter der Verwendung von
Signalen an die jeweilige logische Einheit. Die Theoretischen Grundlagen zu
Signalen und die Verwendung von Signalen innerhalb *gylfeed* wird in Kapitel XX
betrachtet. 



