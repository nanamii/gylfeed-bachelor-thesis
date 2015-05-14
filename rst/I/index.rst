**********
Einleitung
**********

Die vorliegende Bachelorarbeit bezieht sich auf die Projektarbeit mit dem Titel
*Entwurf und Implementierung eines Feedreaders* (vgl. :cite:`SKPA`). Innerhalb
dieser Projektarbeit wurde der Feedreader *gylfeed* entworfen und implementiert.
Es wurde Grundsätzliches zu Feeds erläutert und bereits vorhandene Feedreader
analysiert. Für die gestellten Anforderungen an die Software wurde ein Entwurf
der Softwarearchitektur und ein Entwurf der grafischen Benutzeroberfläche
entwickelt. Diese Entwürfe wurden in der Programmiersprache Python und dem
GUI-Toolkit GTK implementiert. Abschließend erfolgte eine Zusammenfassung der
erreichten Ziele und mögliche Verbesserungen, sowie Weiterentwicklungen.


Thema der Bachelorarbeit
========================

Innerhalb der Bachelorarbeit findet eine genauere Betrachtung der internen
Abläufe des entwickelten Feedreaders *gylfeed* statt. Die verwendete Algorithmik
wird näher erläutert und es werden Vergleiche zu alternativen Lösungen
gezogen. Im Allgemeinen beschäftigt sich die Bachelorarbeit mit der Theorie, die
hinter dem Feedreader *gylfeed* steckt. Zudem werden Entwurfsentscheidungen
bewertet und diskutiert.


Aufbau und Herangehensweise
===========================

Anfangs wird ein kurzer Überlick zum Grundkonzepts des
Feedreaders *gylfeed* gegeben, um die darauf folgenden tiefergehenden Erläuterungen
besser nachvollziehen zu können. Im Anschluss wird der Hintergrund von Signalen
näher betrachtet, sowie die Verwendung von Signalen innerhalb *gylfeed* vorgestellt.
Das zentrale Thema wird der Bereich Download und Parsen der Feed-Daten sein.
Neben detailierten Erläuterungen zum Ablauf des asynchronen Downloads, wird der
synchrone Download im Vergleich betrachtet. Außerdem werden Möglichkeiten
aufgezeigt, die es ermöglichen festzustellen, ob ein Feed neue Nachrichten
enthält und ein Download überhaupt notwendig ist.
Zum besseren Verständnis bestimmter
Sachverhalte werden Diagramme eingesetzt. Dies wird gezielt geschehen und nicht
global für alle Sachverhalte.


Titel der Software
==================

Um innerhalb der Projektarbeit die Software bei ihrem Namen nennen zu können,
soll an dieser Stelle der Titel eingeführt und kurz erläutert werden. Der Name
soll gleichermaßen die Funktionaliät der Software widerspiegeln, als auch
sympathisch klingen. Einerseits, um beim Nutzer besser im Gedächtnis zu bleiben 
und andererseits leicht Sympathie für die Software entwickeln zu können, als
wäre es ein bloßer technischer
Name. Auf diese Weise ist der Name *gylfeed* entstanden. Dies setzt sich aus dem
Namen einer Figur der Buchreihe ,,Die Legende der Wächter'' -- *gylfie* und *Feed*
zusammen  (vgl. :cite:`DLW` -- Ein Portrait der Figur *gylfie*). 
Für die Außendarstellung wurde ergänzend ein Logo entwickelt (siehe Abbildung :num:`gylfeedlogo` ). Dieses
Logo stellt eine Eule der Gattung Elfenkauz dar, wie es die Figur *gylfie* ist.
Das Logo wird in abgewandelter Form als Icon und gemein als Logo für die Software benutzt.

.. _gylfeedlogo:

.. figure:: ./figs/gylfeed_logo.png
    :alt: Logo von gylfeed
    :width: 40%
    :align: center
    
    Das Logo von *gylfeed*.

Für den Schriftzug wird die Schriftart *Portal* mit angepasstem Kerning verwendet. Die
Eule wurde als Vektorgrafik erstellt. Skalieren auf die passende Größe, je nach
Verwendungszweck innerhalb der Software ist somit problemlos möglich. Die
Platzierung der Eule wurde bewusst gewählt, um zwischen Schriftzug und Eule
eine Verbindung und Harmonie zu erzeugen. Hier wurde das Stilmittel des Goldenen
Schnitts angewendet (vgl. :cite:`GS` -- eine mathematische Herleitung des goldenen Schnitts.)
