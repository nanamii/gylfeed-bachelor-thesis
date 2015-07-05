.. _verarbeitung:

***************************
Verarbeitung der Feed-Daten
***************************

Nach der Beschaffung der Feed-Daten stellt sich die Frage, wie diese Daten
verarbeitet werden können. Innerhalb der Projektarbeit *Entwicklung und
Implementierung eines Feedreaders* (vgl. :cite:`kiessling`) wurde Grundlegendes zu Feeds, deren Format
und Aufbau erläutert. An dieser Stelle soll nun eine Analyse der zu
verarbeitenden Feed-Daten durchgeführt werden. Die Verarbeitung der Feed-
Daten innerhalb von *gylfeed*, sowie der dazu eingesetzte Universal Feedparser
werden vorgestellt. 


Analyse der Feed-Daten
======================

Die heruntergeladenen Feed-Daten liegen im Falle von RSS und Atom Feeds als XML-Datei vor. Nun gilt es,
die Daten aus der XML-Datei zu verarbeiten. Um mehr über die Beschaffenheit
der vorliegenden Daten aussagen zu können, werden die Daten verschiedener
Feeds hinsichtlich deren Format und gelieferten XML-Elemente untersucht. 
Diese beiden Faktoren können bei der Verarbeitung der Feed-Daten zu Problemen
führen. Auf diese Probleme wird an späterer Stelle eingegangen. 

Als Analysewerkzeug wurde der Universal Feedparser verwendet. In Abschnitt
:ref:`feedparser` wird dieser Feedparser näher vorgestellt. Für beide Tests 
wurde die bereits in KAPITEL IV verwendete Testmenge von 6.203 Feeds genutzt.



Feedformate
-----------

Wie bereits in der Projektarbeit *Entwicklung und Implementierung eines
Feedreaders* (vgl. :cite:`kiessling`) erwähnt, gibt es eine Vielzahl an Feedformaten und diese in
verschiedenen Versionen. Allein das Format RSS (Really Simple Syndication) 
wurde in sechs verschiedenen Versionen veröffentlicht (vgl. :cite:`HU` - Historie der RSS-Versionen).

Es soll nun anhand einer
Stichprobe untersucht werden, wie häufig die verschiedenen Feedformate in der
Praxis eingesetzt werden. Ziel ist es, einen Eindruck zu gewinnen, welche
Feedformate tendenziell häufiger als andere verwendet werden.

Das Ergebnis in Tabelle :num:`format-statistics` zeigt, dass von den 5.092 Dateien,
die von der gesamten Testmenge (6.203) heruntergeladen werden konnten, das Format
RSS in der Version 2.0 am häufigsten vorkommt. Atom in der Version 1.0 ist mit
einem Vorkommen von 971 das zweithäufigste Format. Alle anderen erkannten
Formate machen zusammen mit einem Wert von 79 einen geringen Anteil aus.
Dateien, die entweder kein Feed oder fehlerhaft waren, betragen 483.



.. _plot:

.. figure:: ./figs/plot_formate.png
    :alt: Häufigkeit der verschiedenen Feedformate.
    :width: 80%
    :align: center
    
    Die Häufigkeit verschiedener Feedformate, untersucht anhand einer
    Stichprobe von 6.203 Feeds.  


    
.. figtable::
    :label: format-statistics
    :caption: Testergebnisse der Prüfung auf Feedformat für 5.092
              heruntergeladene Dateien.
    :alt: Testergebnisse der Prüfung auf Feedformat.
    :spec: l l r

    ============================================ ============  ==========
      **Feedformat/Vorkommen**                    **absolut**   **in %** 
    ============================================ ============  ==========
     **RSS 2.0**                                    3.559         69,89    
     **RSS 1.0**                                       63           1,24    
     **RSS 0.91**                                       7           0,14    
     **RSS 0.92**                                       5         0,10    
     **RSS 0.90**                                       1         0,02    
     **Atom 1.0**                                     971           19,07    
     **Atom 0.3**                                       3           0,06    
     **ohne Format/fehlerhafte**                      483           9,48    
     |hline| **gesamte Dateien**                   5.092         100,00
    ============================================ ============  ==========

- Evtl. darauf eingehen, warum es problematisch ist, dass es viele
  unterschiedliche Formate gibt...Deshalb nutzt gylfeed den Universal
  Feedparser...deckt Großteil der Formate ab...war keine Anforderung an gylfeed,
  dass sämtliche Formate gelesen werden können, UFP reicht vorerst aus.


XML-Elemente
------------

Nicht alle in den jeweiligen Spezifikationen der Feed-Formate definierten Elemente
sind zwingend erforderlich. Das ist verständlich, weil nicht jeder Anbieter
eines Feeds alle möglichen Elemente nutzen möchte. Für die Verarbeitung der Daten
durch den Feedreader ist jedoch kritisch zu betrachten, dass die Anzahl der
flicht-Elemente gering ist. Es muss damit gerechnet werden, dass erwartete
Elemente fehlen können. 

Als Beispiel soll das Format RSS 2.0 betrachtet werden.
Für das in der Stichprobe am häufigsten vorkommende Format RSS 2.0 sind lediglich die
Elemente *title*, *link* und *description* bezogen auf den Feed selbst(channel) zwingend
erforderlich. Die Elemente der einzelnen Einträge (items) sind alle optional.
In der Spezifikation wird darauf hingewiesen, dass für einen Eintrag 
mindestens eines der Elemente *title* oder *description* vorhanden sein
muss (vgl. :cite:`rssrequests` -- Spezifikation von RSS 2.0).


.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <rss version="2.0">
        <channel>
            <title>Titel des Feeds</title>
            <link>URL der Webpräsenz</link>
            <description>Kurze Beschreibung des Feeds</description>
            <language>Sprache des Feeds</language>
            <copyright>Autor des Feeds</copyright>
            <pubDate>Erstellungsdatum</pubDate>
            <image>
                <url>URL einer einzubindenden Grafik</url>
                <title>Bildtitel</title>
                <link>URL, mit der das Bild verknüpft ist</link>
            </image>
            <item>
                <title>Titel des Eintrags</title>
                <description>Kurze Zusammenfassung des Eintrags</description>
                <link>Link zum vollständigen Eintrag</link>
                <author>Autor des Artikels, E-Mail-Adresse</author>
                <guid>Eindeutige Identifikation des Eintrages</guid>
                <pubDate>Datum des Items</pubDate>
            </item>
       </channel>
    </rss>


- nur ein Ausschnitt aller Elemente, vollständige Liste im Anhang?


- Nicht alle Elemente sind Pflicht
- Selbst die Pflicht-Attribute können fehlen.


-- Für die Verarbeitung dieser Daten durch den Feedreader bedeutet dies, dass
  mit fehlenden Attributen gerechnet werden muss.


Inwiefern fehlende Elemente bei der Umsetzung eines Feedreaders von Bedeutung sind,
soll anhand einer Stichprobe untersucht werden. Dabei wird davon ausgegangen,
dass der *Titel*, der *Plot*, das *Datum* und der *Autor* eines Eintrags (items) vom
Feedreader benötigt werden. Die Stichprobe soll auf diese vier Elemente
getestet werden.


'id': 4345, 
'title': 4478,
'icon': 40, 
'image': 1129, 
'author': 3632, 
'logo': 70, 
'link': 4500, 
'counter': 5092, 
'summary': 4442,
'updated_parsed': 4409

.. figtable::
    :label: elemente-statistics
    :caption: Testergebnisse der Prüfung auf XML-Elemente für 5.092
              heruntergeladene Dateien.
    :alt: Testergebnisse der Prüfung auf vorhandede XML-Elemente.
    :spec: l l r

    =============================================== ============  ==========
      **XML-Element/Vorkommen**                      **absolut**   **in %** 
    =============================================== ============  ==========
     **title**                                      4.478         97,16   
     **link**                                       4.500         97,64    
     **description**                                4.442         96,38    
     **date**                                       4.409         95,66    
     **author**                                     3.632         78,80    
     |hline| **gesamte Dateien abzgl. fehlerhafte** 4.609         100,00
    =============================================== ============  ==========

Das Testergebnis in Tabelle :num:`elemente-statistics` zeigt, dass die Elemente
*title*, *link*, *description* und *date* bei einem Großteil der getesteten Feeds
vorhanden sind. Das Element *author* ist hingegen seltener vorhanden.

Auch wenn das Ergebnis zeigt, dass diese Elemente für einen großen Teil der 
getesteten Feeds vorhanden sind, müssen die wenigen Feeds mit fehlenden Elementen
entsprechend behandelt werden.

Interessant zu betrachten wäre an dieser Stelle die Forderung aus der
Spezifikation von RSS 2.0, dass es bei Items keine Pflicht-Elemente gibt, aber
entweder *title* oder *description* vorhanden sein sollte.

.. _feedparser:

Der Universal Feedparser
========================


Umsetzung innerhalb von *gylfeed*
=================================


