**********
Einleitung
**********

Feeds ermöglichen dem Benutzer, automatisch über Änderungen einer Webseite informiert zu
werden. Zum Verwalten und Lesen dieser Feeds wird häufig ein sogenannter Feedreader
genutzt. Die Software *gylfeed* ist ein eben solcher Feedreader, der innerhalb
der Projektarbeit *Entwurf und Implementierung eines Feedreaders* (vgl.
:cite:`SKPA`) entwickelt wurde. Die vorliegende Bachelorarbeit nimmt Bezug auf
diese Projektarbeit. Innerhalb der Projektarbeit wurde Grundsätzliches zu Feeds erläutert
und bereits vorhandene Feedreader analysiert. Für die gestellten Anforderungen 
an die Software wurde ein Entwurf der Softwarearchitektur und ein Entwurf der 
grafischen Benutzeroberfläche entwickelt. Diese Entwürfe wurden in der Programmiersprache 
Python und dem GUI-Toolkit GTK+ implementiert. Abschließend erfolgte eine Zusammenfassung der
erreichten Ziele und mögliche Verbesserungen, sowie Weiterentwicklungen.


Thema der Bachelorarbeit
========================

Innerhalb der Bachelorarbeit findet eine detailliertere Betrachtung der internen
Abläufe des entwickelten Feedreaders *gylfeed* statt. Es werden theoretische
Hintergründe erläutert und die entsprechende Umsetzung in *gylfeed* vorgestellt
und bewertet. Der Kern der Arbeit beschäftigt sich mit der Beschaffung und
Verarbeitung der Feed-Daten und zieht dazu unter anderem Stichprobentests heran. 


Aufbau und Herangehensweise
=========================== 

Anfangs wird ein kurzer Überblick zum Grundkonzepts des
Feedreaders *gylfeed* gegeben, um die darauf folgenden tiefergehenden Erläuterungen
besser nachvollziehen zu können. Im Anschluss wird der Hintergrund von Signalen
näher betrachtet, sowie die Verwendung von Signalen innerhalb von *gylfeed* vorgestellt.

Das zentrale Thema ist der Bereich Beschaffung und Verarbeitung der Feed-Daten.
Neben detaillierten Erläuterungen zum Ablauf des asynchronen Downloads, wird der
synchrone Download im Vergleich betrachtet. Dazu wird ein Performancetest
durchgeführt. Außerdem werden Möglichkeiten
aufgezeigt, die es ermöglichen festzustellen, ob ein Feed neue Nachrichten
enthält und ob ein Download überhaupt notwendig ist. Die dafür verwendeten
Attribute *ETag* und *last-modified* werden anhand einer Stichprobe auf die
Häufigkeit ihres Vorkommens bei Feeds getestet.

Das Kapitel *Verarbeitung der Feed-Daten* beginnt mit einer Analyse der
Feed-Daten. Es wird anhand einer Stichprobe die Häufigkeit von ve rschiedenen
Feedformaten untersucht. Eine weitere Untersuchung beschäftigt sich mit der
Häufigkeit verschiedener Inhaltselemente der Feed-Daten. Der Universal
Feedparser wird als Möglichkeit der Feed-Daten-Verarbeitung vorgestellt.
Anschließend wird näher auf die Umsetzung innerhalb von *gylfeed* eingegangen,
die abschließend bewertet wird.






Zielgruppe
==========

