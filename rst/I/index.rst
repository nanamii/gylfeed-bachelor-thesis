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


Zielgruppe
==========

