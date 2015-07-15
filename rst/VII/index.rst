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
ist möglich nach einem Feed oder einer Nachricht zu suchen. Abbildung
:cite:`suchleiste` zeigt die implementierte Suchfunktion. Der Suchbegriff
*deutschland* ist in drei der durchsuchten Nachrichten enthalten. Wie die
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
unvollständig oder die Suche komplett erfolglos bleibt.
















Einbindung von Datamining-Algorithmik
=====================================


