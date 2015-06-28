.. _verarbeitung:

***************************
Verarbeitung der Feed-Daten
***************************

Nach der Beschaffung der Feed-Daten stellt sich die Frage, wie diese Daten
verarbeitet werden können. In diesem Zusammenhang treten verschiedene
Problemstellungen auf. 


Ausgangssituation und Problemstellungen
=======================================

Die heruntergeladenen Feed-Daten liegen meist als XML-Datei vor. Nun gilt es,
die Daten aus der XML-Datei zu verarbeiten...

Feedformate
-----------

Wie bereits in der Projektarbeit *Entwicklung und Implementierung eines
Feedreaders* erwähnt, gibt es eine Vielzahl an Feedformaten und diese in
verschiedenen Versionen. Allein das Format RSS (Really Simple Syndication) 
wurde in sechs verschiedenen Versionen veröffentlicht (vlg. :cite:`HU` - Historie der RSS-Versionen).

Es soll nun anhand einer
Stichprobe untersucht werden, wie häufig die verschiedenen Feedformate in der
Praxis verwendet werden. Ziel ist es, eine Aussage treffen zu können, welche
Feedformate tendenziell häufiger als andere verwendet werden.

.. _plot:

.. figure:: ./figs/plot_formate.png
    :alt: Häufigkeit der verschiedenen Feedformate.
    :width: 80%
    :align: center
    
    Die Häufigkeit verschiedener Feedformate, untersucht anhand einer
    Stichprobe von 6.203 Feeds.  




Fehlende Attribute
------------------

Fehlende Attribute sind eine weitere Herausforderung, die sich bei der
Verarbeitung der Feed-Daten ergeben.

Inwiefern fehlende Attribute bei der Umsetzung eines Feedreaders von Bedeutung sind,
soll anhand einer Stichprobe untersucht werden. Dabei wird davon ausgegangen,
dass der *Titel*, der *Plot*, das *Datum* und der *Autor* der Feed-Nachricht vom
Feedreader benötigt werden. Die Stichprobe soll auf diese vier Attribute
getestet werden.



Speicherung der Daten
---------------------


Lösungsansätze
==============


Umsetzung innerhalb von *gylfeed*
=================================


