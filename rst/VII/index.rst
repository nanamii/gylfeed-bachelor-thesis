***********************
Weiterführende Konzepte
***********************

Innerhalb der Projektarbeit *Entwurf und Implementierung eines Feedreaders*
wurden bereits mögliche Verbesserungen und Erweiterungen für den Feedreader
*gylfeed* vorgeschlagen. Im Folgenden wird die Suchfunktion, mögliche Einbidung
von Datamining-Algorithmik und der automatische Namensvorschlag beim Hinzufügen
eines neuen Feeds näher betrachtet.



Ausbau der Suchfunktion
=======================

In der aktuellen Version von *gylfeed* wird eine lineare Suche angewendet. Es
ist möglich nach einem Feed oder dem Titel einer Nachricht zu suchen. Abbildung
:cite:`suchleiste` zeigt die implementierte Suchfunktion. Der Suchbegriff
*software* ist in drei der durchsuchten Nachrichten-Titeln enthalten. Wie die
Suchergebnisse zeigen, wird der Suchbegriff sowohl in Groß- als auch in
Kleinschreibung gefunden. Bevor zwischen Suchanfrage und Datenbestand aus
Nachrichten ein einfacher String-Vergleich stattfindet, werden beide
Zeichenketten mit der Funktion *lower()* in Kleinschreibung vereinheitlicht.


.. _suchleiste:

.. figure:: ./figs/suche.png
    :alt: Die Suchfunktion von gylfeed.
    :width: 80%
    :align: center
    
    Die Suchfunktion von gylfeed, Suche innerhalb der Nachrichten des Feeds
    *Golem*.


Code der implementierten Suchfunktion:
    
.. code-block:: python

   def _filter_function(self, row):
        query = self.search_term.lower()
        if not query:
            return True
        return query in row.get_title().lower()


Das Problem dieser Implementierung ist, dass bereits bei einem abweichenden
Zeichen keine Übereinstimmung gegeben ist und das Suchergebnis deshalb
unvollständig oder die Suche komplett erfolglos bleibt. Aus diesem Grund ist es
erstrebenswert, eine fehlertolerante Implementierung zu finden. Um trotz
Tippfehler, Buchstabendreher, falscher Rechtschreibung und ähnlichem zum
gewünschten Suchergebnis zu kommen, gibt es entsprechende Algorithmen.

Eine mögliche Lösung bietet das Modul *difflib* der Python Standardbibliothek
(vgl. :cite:`difflib` -- Dokumentation von difflib). Dem liegt der
Ratcliff-Obershelp Algorithmus zu Grunde. Der von John W. Ratcliff und D. E.
Metzener entwickelte Algorithmus sucht die größte übereinstimmende Sequenz
zweier Zeichenketten. Das wird für alle übrigen Zeichen rechts und links der
übereinstimmenden Sequenz durchgeführt, solange bis keine Zeichen mehr übrig
sind. Das Ergebnis des Vergleichs wird aus dem Zweifachen der Summe aller
gefundenen Sequenzen, dividiert durch die Summe der Zeichen beider
Zeichenketten, berechnet (vgl. :cite:`ratcliff`). Folgendes einfache Beispiel zeigt die Andwendung des
Algorithmus für die Zeichenketten *grafik* und *graphik*.

.. math::

    \frac {2*(3+2)}{(6+7)} = 0,77    (Übereinstimmende Sequenzen: *gra* und *ik*)

Der Ratcliff-Obershelp Algorithmus hat eine Komplexität von :math:`O(n^{3})` im
schlechtesten Fall und eine zu erwartende Komplexität von :math:`O(n^{2})`.


Alternativ soll der Damerau-Levenshtein Algorithmus betrachtet werden. Hierbei
handelt es sich um ein Distanzmaß. Es werden die notwendigen Editiervorgänge
gezählt, die es benötigt, um zwei übereinstimmende Zeichenketten zu erhalten.
Editiervorgänge sind das Löschen, Ersetzen oder Einfügen von Zeichen.
Zusätzlich erkennt der Algorithmus vertauschte Zeichen. Das unterscheidet den
Damerau-Levenshtein Algorithmus vom reinen Levenshtein Algorithmus. Der
Vergleich der Zeichenketten *grafik* und *graphik* ergibt eine Editierdistanz
von 2. Im ersten Schritt wird ,,f`` durch ,,p`` ersetzt und anschließend ,,h``
entfernt. Um diese Editierdistanz besser mit dem Ergebnis anderer Algorithmen
vergleichen zu können, gibt es die normalisierte Damerau-Levenshtein-Distanz.


Der Damerau-Levenshtein Algorithmus hat eine Komplexität von :math:`O(nm)`, mit m und n
als jeweilige Länge der Zeichenketten.

Für beide Algorithmen gibt es eine Implementierung in python. Die folgende
*bpython*-Sitzung zeigt die Ausfürhung der Algorithmen.

.. code-block:: python

   >>> import difflib
   >>> from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance 
   >>> from pyxdameraulevenshtein import damerau_levenshtein_distance
   
   >>> difflib.SequenceMatcher(None, "grafik", "graphik").ratio()
   0.7692307692307693
   >>> damerau_levenshtein_distance("grafik", "graphik")
   2
   >>> normalized_damerau_levenshtein_distance("grafik", "graphik")
   0.2857142857142857
   >>> 1 - normalized_damerau_levenshtein_distance("grafik", "graphik")
   0.7142857142857143


Der vom Python-Modul *difflib* errechnete Wert stimmt mit dem eben manuell berechneten
Ratcliff-Obershelp Wert von 0.77 überein. Auch die Ausführung des
Damerau-Levenshtein Algorithmus ergibt die manuell errechnete Editierdistanz von
2. Im Anschluss wurde die normalisierte Damerau-Levenshtein-Distanz berechnet.
Da ein Wert von 0.0 völlige Übereinstimmung und 1.0 keinerlei Übereinstimmung
entspricht, wird der errechnete Wert im nächsten Schritt von 1 subtrahiert. Das
ermöglicht den Vergleich mit dem Ergebnis des Ratcliff-Obershelp Algorithmus. Es
ist zu erkennen, dass beide Werte nahe beieinander liegen. Ratcliff-Obershelp
errechnet eine minimale höhere Übereinstimmung der Zeichenketten *grafik* und
*graphik*.

Wie können diese Algorithmen die Suchergebnisse innerhalb von *gylfeed*
verbessern. Ausgehend von der Annahme, es werden Übereinstimmungen bis zu einem
Wert von 0.60 als Suchtreffer angezeigt, würden innerhalb von *gylfeed* nicht
nur Schlagzeilen, die genau *grafik* enthalten angezeigt, sondern auch
diejenigen, die die Schreibweise *graphik* verwenden. Das ist auf sämtliche
andere Fälle übertragbar und die Fehlertoleranz beliebig anpassbar. Die
Erweiterung der Suche mit Hilfe der vorgestellten Algorithmen bietet dem
Benutzer demnach einen größeren Komfort.

Welcher der beiden Algorithmen zu bevorzugen ist, darüber lässt sich nur
schwierig eine allgemeine Aussage treffen. Damerau-Levenshtein hat zumindest
aufgrund der geringeren Laufzeit-Komplexität einen Performance-Vorteil.

Bei relativ großen Datenmengen ist die Laufzeit-Komplexität des
Damerau-Levenshtein Algorithmus von  :math:`O(nm)`, dennoch als problematisch
anzusehen. Hier wären alternative Suchstrategien, wie beispielsweise die binäre
Suche anzuraten.



Einbindung von Datamining-Algorithmik
=====================================


