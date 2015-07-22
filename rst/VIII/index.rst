***************
Zusammenfassung
***************

Die Bachelorarbeit hat einen detaillierteren Einblick in die
Beschaffung und Verarbeitung der Feed-Daten innerhalb des Feedreaders *gylfeed*
gegeben. Es wurden die theoretischen Hintergründe erläutert und
Stichprobentests durchgeführt. Die Vorstellung des Feedreaders *gylfeed* hat es
erleichtert, spätere detailliertere Betrachtungen
nachvollziehen zu können. Die Grundlage und die Verwendung von Signalen
innerhalb *gylfeed* wurden erläutert.


Ergebnisse im Bereich der Feed-Daten-Beschaffung
================================================

Im Bereich der Feed-Daten-Beschaffung wurde die Performance der Anwendung im
Hinblick auf den Download der Feed-Daten betrachtet. Die in der Theorie
erläuterten Vorteile des asynchronen Downloads gegenüber dem synchronen Download
konnten anhand einer Stichprobe bestätigt werden (vgl. :ref:`performancetest`).
Dafür wurde für eine steigende Anzahl an URLs der Inhalt der Webseiten
heruntergeladen und die verbrauchte Zeit gemessen. Der Test konnte die Vorteile
des asynchronen Ansatzes für die Performance der Andwendung bestätigen und wird
in dieser Form im Feedreader *gylfeed* umgesetzt.

Um die Problematik des erneuten Herunterladens aller Feed-Daten zu umgehen,
wurden die Attribute *ETag* und *last-modified* des HTTP-Headers vorgestellt. Um den Nutzen
der Prüfung auf diese beiden Attribute zu validieren, wurde für eine Testmenge
von 3.512 Feeds der HTTP-Header auf das Vorhandensein dieser Attribute getestet.
Der Test hat ergeben, dass von 83,88 % der untersuchten Feeds mindestens eines
der Attribute geliefert wird (vgl. :ref:`etagtest`). Dieses Ergebnis unterstützt die Entscheidung, die
Prüfung auf die beiden Attribute im Feedreader *gylfeed* einzusetzen.

Nach der theoretischen Betrachtung und Ausführung von Stichprobentests wurde die
Umsetzung der Feed-Daten-Beschaffung innerhalb von *gylfeed* vorgestellt.
Die abschließende Bewertung ergab, dass es bei der Prüfung auf
Aktualisierung mittels *ETag* und *last-modified* Verbesserungsbedarf gibt.
Statt der clientseitigen Prüfung, sollte die Prüfung durch den Server
stattfinden, wie es zuvor theoretisch erläutert wurde. Die Umsetzung des asynchronen
Downloads der Feed-Daten ist nicht zu bemängeln.


.. raw:: Latex

   \newpage

Ergebnisse im Bereich der Feed-Daten-Verarbeitung
=================================================

Eine Analyse der Feed-Daten sollte zu Beginn des Bereichs
Feed-Daten-Verarbeitung Erkenntnisse über die Beschaffenheit der vorliegenden
Daten geben. Dazu wurde im ersten Schritt ein Stichprobentest durchgeführt, der
die Verteilung der verschiedenen Feedformate untersucht. Von 5.092 Feeds hatten
69,89 % das Format RSS 2.0 und 19,07 % das Format Atom 1.0 (vgl. :ref:`testfeedformate`).

Im zweiten Schritt wurden die Inhaltselemente der Feed-Daten analysiert. Die
Elemente, die für *gylfeed* am wichtigsten sind, wurden auf ihr Vorkommen
untersucht. Dabei kamen die Elemente betreffend einer Feed-Nachricht, *title
(97,16 %)*,
*link (97,64 %)*, und *description (96,38 %)*, bei einem Großteil der getesteten
5.092 heruntergeladenen Feed-Daten vor. Zusätzlich wurde eine Untersuchung
durchgeführt, die die Forderung der Spezifikation von RSS 2.0 überprüft. Demnach
gibt es bei Feed-Nachrichten (nach RSS-Spezifikation Items) keine
Pflicht-Elemente, aber entweder *title* oder *description* vorhanden sein
sollte. Der Test ergab, dass in 97,53 % der getesteten RSS 2.0 Feeds mindestens
eines der beiden geforderten Attribute vorhanden ist (vgl. :ref:`testxmlelemente`).

Innerhalb von *gylfeed* wird der Universal Feedparser zur Verarbeitung der
Feed-Daten genutzt. Dieser wurde vorgestellt. Die Umsetzung der
Feed-Daten-Verarbeitung innerhalb von *gylfeed* wurde erläutert. Die Bewertung
der Umsetzung ergab, dass das Parsen der Feed-Daten, das an verschiedenen
Stellen ausgeführt wird, aufgrund der Wartbarkeit zentral an einer Stelle
ausgeführt werden sollte. Der Vergleich vorhandener Nachrichten mit den neu
heruntergeladenen Nachrichten anhand deren ID, wäre beispielsweise auch mittels Bildung
eines Hashwerts möglich. Aktuell ist die Speicherung der Daten mit dem
Python-Modul *pickle* vertretbar. Sollen die Daten aber auch außerhalb von
*gylfeed* nutzbar sein, wäre der Einsatz einer Datenbank sinnvoll.

Fazit & Ausblick
================

Die detailliertere Betrachtung der internen Abläufe des Feedreaders *gylfeed*
hat es ermöglich, noch vorhandene Schwachstellen zu erkennen und tiefer in die
theoretischen Grundlagen einzusteigen, wofür während der Projektarbeit teilweise
weniger Zeit übrig war.

Die weiterführenden Konzepte in Kapitel :ref:`weiterfuehrendekonzepte` 
haben im Ansatz gezeigt, welche
zukünftigen Erweiterungen denkbar sind. Der Feedreader *gylfeed* hat im
aktuellen Entwicklungszustand noch einigen Entwicklungsbedarf, bietet aber
eine solide Grundbasis. Gerade der Ausbau der Suchfunktion mit Hilfe der
vorgestellten Algorithmen wäre für *gylfeed* ein Zugewinn an Funktionalität.
Die Einbindung von Nutzer-Präferenzen ist nach Meinung der Autorin ein sehr
interessantes Gebiet, das es lohnt innerhalb der Weiterentwicklung von
*gylfeed* mit einbezogen zu werden.

Ziel ist es, die Entwicklung von *gylfeed* weiterzuführen. Es wird angestrebt,
den Feedreader auf der Plattform für Python Pakete, PyPI zu veröffentlichen
(vgl. :cite:`pypi`).




 
