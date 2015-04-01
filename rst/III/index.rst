*********************
Vorhandene Feedreader
*********************

Um einen Eindruck von bereits vorhandenen Feedreadern zu erhalten und
anschließende Designentscheidungen bei *gylfeed* besser nachvollziehen zu
können, wird das Grundkonzept dieser Feedreader kurz vorgestellt. Eine genaue
Analyse der einzelnen Funktionalitäten, die von den Feedreadern bereitgestellt
werden und weiterführende Vergleiche, sind Bestandteil der Bachelorarbeit.


Konzept aktueller Feedreader
============================
Der Großteil der vorhandenen Feedreader, in diesem Fall speziell Feedreader, die
als eigenständige Desktopsoftware funktionieren, sind an den Aufbau eines
Mailclients angelehnt.
Als Veranschaulichung wird der Feedreader *Liferea* herangezogen. *Liferea*
deshalb, weil er wie es *gylfeed* sein wird:

 * Für Linux entwickelt ist.
 * Gtk als Oberflächentechnik verwendet.
 * Unter GNU GPL lizenziert ist.
 * Den Anspruch erhebt, leicht bedienbar zu sein.

Weitere Desktop-Feedreader, die vergleichbar im Aufbau sind, wären beispielsweise *RSSOwl*,
*Vienna* oder *QuietRSS* 


Der Feedreader *Liferea*
========================

*Liferea* steht für *Linux Feed Reader* und wird seit 2003 stetig
weiterentwickelt. Die Benutzeroberfläche hat den Aufbau eines klassischen
Mailclients. Entwickelt wurde *Liferea* hauptsächlich in der Programmiersprache
C. Die Projektseite selbst (siehe :cite:`PSL`) gibt den Umfang des Codes mit ca.
27.000 Zeilen an.


.. _liferea:

.. figure:: ./figs/liferea_screenshot.png
    :alt: Der Feedreader liferea.
    :width: 85%
    :align: center
    
    Der Feedreader liferea.


Die Grundfunktionalitäten von *Liferea* werden anhand der Benutzerobefläche (siehe Abbildung :num:`liferea`) erläutert.
In der Symbolleiste sind folgende Funktionalitäten zu finden:
 * Feed hinzufügen
 * Feed als gelesen markieren
 * Navigationspfeile
 * Nächsten ungelesenen Eintrag aufrufen
 * Alle aktualisieren
 * Alle Feeds durchsuchen

Links ist eine Baumansicht der Feeds implementiert. Die Feeds können in Ordnern
verwaltet werden. Zu jedem Feed gibt es ein Label, das die Anzahl der neuen
Nachrichten anzeigt.

Die rechte Seite enthält ein Fenster mit aufgelisteten Nachrichten und ein
Fenster, das den Inhalt der jeweils ausgewählten Nachricht anzeigt. Für die
Anordnung dieser beiden Fenster gibt es zusätzlich Einstellmöglichkeiten.
Im Grunde liegt hier tatsächlich der Aufbau eines klassischen Mailclients vor.

Neben den genannten Funktionalitäten kann über einen separaten
Einstellungsdialog beispielsweise der Updateintervall oder Optionen für Ordner
gesetzt werden. 

Es können die Formate RSS, Atom, CDF(Common Data Format), OCS(Open Collaboration Services) 
und OPML(Outline Processor Markup Language) gelesen werden. *Liferea* bietet außerdem einen 
eingebetteten Browser an. Zusätzlich können Links außerhalb von *Liferea* in gewünschten 
Browsern geöffnet werden.


Fazit für die Entwicklung von *gylfeed*
=======================================
*gylfeed* wählt vorallem beim Aufbau der Benutzeroberfläche und der Navigation
einen anderen Ansatz als bereits vorhandene Feedreader. Die Aufteilung
der Benutzeroberfläche nach dem Aufbau eines klassischen Mailclients ist bereits in
zahlreichen Feedreadern umgesetzt. Für die Entwicklung für *gylfeed* wird
unter anderem im Vordergrund stehen, eine kompakte Benutzeroberfläche anzubieten, die
sich von den bisherigen Benutzeroberflächen abhebt.







