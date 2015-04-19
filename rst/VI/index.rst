.. _entwurfGUI:

******************************
Entwurf der Benutzeroberfläche
******************************

Überlegungen und Grundkonzept
=============================

Ziel ist es, die gestellten Anforderungen an die Benutzeroberfläche zu erfüllen.
Primäre Anforderungen sind:

 * Minimalistisches Design
 * Kompaktheit
 * Einfachheit der Bedienung
 * Innovatives Navigationskonzept
 * Ausreichend Feedback geben
 * Grundsätzliche Orientierung an den GNOME Human Interface Guidelines

Ein minimalistisches Design soll dadurch erreicht werden, dass lediglich die
wichtigen Bestandteile dargestellt werden. Auf unnötige Spielereien wird
verzichtet. Es wird eine klare, übersichlich strukturierte Oberfläche entworfen.

Die GUI wird immer exakt ein Thema darstellen und dadurch die
geforderte Kompaktheit erfüllen.
Es wird keine Verschachtelung verschiedener Fenster geben. Das bietet einerseits den Vorteil, 
leicht die Übersicht zu behalten und andererseits kann diese GUI leicht in einen
Tiling-Window-Manager integriert werden (vgl. :cite:`i3` -- i3 als Beispiel eines
Tiling-Window-Managers).

Die Einfachheit der Bedienung wird beispielsweise dadurch erreicht, dass dem
Benutzer bekannte Shortcuts zur Verfügung gestellt werden. Grundsätzlich wird
die Einfachheit umgesetzt, indem eine intuitive Bedienung angeboten wird. So
ist der Wechsel zwischen den Ansichten mit den Pfeiltasten möglich. 

Die Navigation mit der Tastatur stellt ebenso die einfache sowie effiziente
Bedienung sicher und ist Bestandteil des innovativen Navigationskonzepts. Das
Navigationskonzept wird in diesem Kapitel noch separat behandelt.

Um die Forderung nach ausreichendem Feedback zu erfüllen, werden dem Benutzer
Hinweise angezeigt und für ausgeführte Aktionen Resultate dargestellt. 
Treten beispielsweise beim Hinzufügen eines Feeds Fehler auf, wird der Benutzer 
mit einem Hinweis darauf aufmerksam gemacht. Außerdem ist das komplette
Verhalten der Benutzeroberfläche darauf abgestimmt, dem Benutzer bei jeglicher
Aktion Rückmeldung zu geben.

.. _mainwindow:

.. figure:: ./figs/scratchMainWindow.png
    :alt: Mockup des MainWindows.
    :width: 70%
    :align: center
    
    Mockup des *MainWindows*.


Das Grundkonzept der Benutzeroberfläche beruht auf dem in Abbildung
:num:`mainwindow` dargestellten *MainWindow*. Das *MainWindow* verwaltet den
Stack, der die verschiedenen Ansichten darstellt. Die Ausmaße des Fensters
betragen beim Start von *gylfeed* standardmäßig 800x600 Pixel. Eine
individuelle Anpassung der Fenstergröße ist möglich.


Die Ansichten
=============

Um einen ersten Eindruck von der geplanten Benutzeroberfläche zu erhalten, wurden
Mockups der einzelnen Ansichten erstellt. Jede der Ansichten wird kurz
erläutert.


Anzeige der Feeds - *FeedView*
------------------------------

.. _feedview:

.. figure:: ./figs/scratchFeedview.png
    :alt: Mockup der Ansicht FeedView.
    :width: 90%
    :align: center
    
    Mockup der Ansicht *FeedView*.

Abbildung :num:`feedview` zeigt den Entwurf der Ansicht *FeedView*.
Mit der *FeedView* soll nicht nur die erste Ansicht, sondern der Grundaufbau
der kompletten GUI näher betrachtet werden. In der Header Bar sind global
zugängliche Funktionaliäten enthalten. Der View Switcher, Such-Button,
Menü-Button und Exit-Button. Mit dem View Switcher ist das Navigieren
zwischen den Ansichten mit Maus möglich. Der Search-Button öffnet einen
Revealer innerhalb der jeweiligen Ansicht und ermöglicht die Suche innerhalb
dieser Ansicht. Der Menü-Button öffnet ein Menü mit weiteren
Auswahlmöglichkeiten, die in Abbildung :num:`menue` näher betrachtet werden. Der
Exit-Button schließt das Programm. In der Mitte der Header Bar kann ein Titel
dargestellt werden. Dieser wird an die jeweilige Ansicht angepasst. Wird
aktuell die *FeedView* dargestellt, wird als Titel die Anzahl der Feeds angezeigt.

Innerhalb der *FeedView* selbst ist eine Listbox enthalten, die wiederum
Listbox Rows enthält. In einer Listbox Row wird der Titel des Feeds und 
Labels für die Anzahl der neuen, ungelesenen, gesamten Nachrichten angezeigt
. Jede Listbox Row enthält einen Settings-Button. Dieser öffnet die Ansicht
*FeedOptionsView*. Die Ansicht ist scrollbar.

Suche innerhalb einer Ansicht
-----------------------------

Abbildung :num:`search` zeigt den Entwurf der Feedansicht mit 
aktivierter Suchfunktion. In diesem Fall verschiebt ein Revealer die
angezeigten Feeds nach unten und schafft Platz für die Suchleiste.

.. _search:

.. figure:: ./figs/scratchSearch.png
    :alt: Mockup der Ansicht FeedView mit aktivierter Suchfunktion.
    :width: 70%
    :align: center
    
    Mockup der Ansicht *FeedView* mit aktivierter Suchfunktion.

   
Ansicht der Optionen - *FeedOptionsView*
----------------------------------------

Abbildung :num:`options` zeigt den Entwurf der Ansicht *FeedOptionsView*.
Diese Ansicht wird verwendet, um neue Feeds hinzuzufügen, oder die
Einstellungen eines bereits vorhandenen Feeds anzuzeigen und Änderungen
vorzunehmen. Für diese Ansicht wird in der Header Bar ein zustimmender und
ein ablehnender Button hinzugefügt. Je nach Funktion der Ansicht, führen
diese Buttons andere Aktionen aus. Dem Benutzer wird dies durch entsprechende
Beschriftungen deutlich gemacht. Die Ansicht enthält die Eingabefelder für
die URL des Feeds und den Namen des Feeds. Einstellungen sind: automatisches
Update (ja/nein), Update-Intervall (Regler in Minuten), Zeitraum nach dem 
Nachrichten gelöscht werden (Regler in Tagen) und Notifications (ja/nein).

.. _options:

.. figure:: ./figs/scratchOptions.png
    :alt: Mockup der Ansicht FeedOptionsView.
    :width: 70%
    :align: center
    
    Mockup der Ansicht *FeedOptionsView*.



Ansicht von Entries - *EntryListView*
-------------------------------------

Abbildung :num:`entries` zeigt den Entwurf der Ansicht von Entries.
Die Entries werden in Listbox Rows innerhalb einer Listbox dargestellt. Eine
Listbox Row enthält die Daten eines Entry, also einer Nachricht. Es wird der
Titel der Nachricht und der Zeitstempel angezeigt. In der Header Bar wird als
Titel der Name des Feeds angezeigt. Die Ansicht ist scrollbar.

.. _entries:

.. figure:: ./figs/scratchEntries.png
    :alt: Mockup der Ansicht EntryListView.
    :width: 70%
    :align: center
    
    Mockup der Ansicht *EntryListView*.


Detailansicht eines Entry - *EntryDetailsView*
----------------------------------------------

Abbildung :num:`details` zeigt den Entwurf der Detailansicht eines
Entry. Wird ein bestimmter Entry ausgewählt, wird er in dieser Ansicht
detailliert dargestellt. Es wird der Titel, der Plot und mögliches
Bildmaterial angezeigt. Diese Ansicht ermöglicht das Öffnen von Links direkt
innerhalb dieser Ansicht. So kann beispielsweise der eigentliche Artikel
innerhalb dieser Ansicht angezeigt werden.

.. _details:

.. figure:: ./figs/scratchDetails.png
    :alt: Mockup der Ansicht EntryDetailsView.
    :width: 70%
    :align: center
    
    Mockup der Ansicht *EntryDetailsView*.


Inhalt des Menüs
----------------

Abbildung :num:`menue` zeigt den Entwurf der Feedansicht mit 
geöffnetem Menü. Im Menü können die Aktionen *update*, *add Feed*, 
*about gylfeed* oder *Close Window* ausgeführt werden. Das sind Aktionen,
die von jeder Ansicht aus ausgeführt werden können sollen und deshalb
global zugänglich in der Header Bar angeboten werden. Sollten während
der Entwicklung von *gylfeed* weitere globale Aktionen hinzukommen, ist
die Erweiterung des Menüs problemlos möglich. Für diese Aktionen werden
Shortcuts angeboten, die in der Abbildung bereits beispielhaft dargestellt
sind.

.. _menue:

.. figure:: ./figs/scratchMenue.png
    :alt: Mockup der FeedView mit geöffnetem Menü.
    :width: 70%
    :align: center
    
    Mockup der *FeedView* mit geöffnetem Menü.

.. raw:: latex

   \newpage

Navigationskonzept
==================

Der Inhalt der einzelnen Ansichten wurde vorgestellt. Ergänzend soll nun in
Abbildung :num:`navikonzept` die
Navigation zwischen den einzelnen Ansichten dargestellt werden. Im Zuge
dessen wird das Konzept der Interaktion, d.h. auf welche Weise navigiert 
werden kann, verdeutlicht.

.. _navikonzept:

.. figure:: ./figs/navikonzept.png
    :alt: Navigationskonzept von gylfeed.
    :width: 100%
    :align: center
    
    Navigationskonzept von *gylfeed*.

Zwischen *FeedView*, *EntryListView* und *EntryDetailsView* ist die
Navigation mit Pfeiltasten oder alternativ über den ViewSwitcher in der 
Header Bar möglich (blau dargestellt). Zur *FeedOptionsView* kann zentral über den Menü-Button
in der Header Bar navigiert werden. Durch die Auswahl von *add Feed* wird
die *FeedOptionsView* aufgerufen (grüner Pfeil mit Beschriftung "Add Feed"). Der Aufruf der *FeedOptionsView* über
den Settings-Button innerhalb der *FeedView* zeigt die Daten und
Einstellungen eines Feeds an (grüner Pfeil mit Beschriftung "Settings"). 
Innerhalb von *FeedView* und *EntryListView* ist der Wechsel zwischen den
einzelnen Rows über die Pfeiltasten möglich (rot dargestellt).
