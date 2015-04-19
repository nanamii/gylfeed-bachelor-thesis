.. _architekturentwurf:

******************
Architekturentwurf
******************

In diesem Kapitel wird die Architektur der Software *gylfeed* vorgestellt.
Hierzu werden die Anforderungen aus Kapitel :ref:`anforderungen` (Anforderungen
an die Software) herangezogen. Eine
detaillierte Beschreibungen der internen Abläufe, tiefergehende Erläuterungen
zur Algorithmik und Problemstellungen sind Bestandteil der
Bachelorarbeit.


Herausforderungen und Lösungsansätze
====================================

Nun gilt es, für die gestellten Anforderungen Lösungsansätze zu entwickeln.
Hierzu sollen vorerst grundlegende Bestandteile der Software geklärt werden.

**Beschaffung der Daten:** Die Daten der Feeds müssen beschafft, also
heruntergeladen und verarbeitet, also geparst werden. Hier liefern verschiedene
Bibliotheken mögliche Ansätze.

**Verwaltung der Daten:** Die Daten, die eindeutig einem Feed zugeordnet werden
können, werden innerhalb eines Feedobjekts gekapselt. Dem übergeordnet ist eine
Instanz, die jene Feedobjekte aufnimmt: der Feedhandler. Dieser ist auch dafür
zuständig, Daten konsistent zu speichern und zu laden.

**Updates:** Die Spezifiktion stellt die Anforderung, dass Updates andere
Abläufe nicht beeinträchtigen dürfen. Hier ist das asynchrone Aktualisieren der
Feeds ein Lösungsansatz.

**Benutzeroberfläche:** Für die Benutzerobefläche ist ein neues Konzept
gefordert. Hierzu werden Entwürfe erstellt.


.. _klassendiagramm:

.. figure:: ./figs/klassendiagramm.png
    :alt: Übersicht der Klassen von gylfeed.
    :width: 100%
    :align: center
    
    Übersicht der Klassen von *gylfeed*.


Übersicht der Klassen
=====================

Abbildung :num:`klassendiagramm` zeigt die Klassen, die von *gylfeed* verwendet
werden. Jede Klasse soll kurz vorgestellt werden.

**MainApplication:** Die Klasse *MainApplication* wird durch *gylfeed.py*
initialisiert. Hier erfolgt der Start des Programms.

**Feedhandler:** In der *MainApplication* wird eine Instanz der Klasse
*Feedhandler* erstellt. Der Feedhandler hält die Instanzen aller erstellten
Feeds. Außerdem benutzt der Feedhandler die Klasse *Downloader* zum
Herunterladen der Feed-Daten.

**Feed:** Die Klasse *Feed* repräsentiert ein Abonnement eines Feeds. Von dieser
Klasse wird die Klasse *SumFeed* abgeleitet. *Feed* benutzt selbst auch die
Klasse *Downloader*. Anders als bei der Klasse *Feedhandler* wird hier die
Aktualisierung in Intervallen durchgeführt, die für jeden Feed individuell sind.

**SumFeed:** SumFeed leitet von *Feed* ab und stellt die Gesamtheit der Feeds
dar. SumFeed kann aufgrund der Ableitung von *Feed* aber wie ein *Feed* agieren.
Eingesetzt wird diese Klasse für die Darstellung aller vorhandener Feeds.

**Downloader:** Die Klasse *Downloader* beschafft die von den Klassen *Feed* und
*Feedhandler* angefragten Daten. Sie verwendet die Klasse *Document*.

**Document:** Die Klasse *Document* liefert ein Future-Objekt zurück und wird
von der Klasse *Downloader* verwendet. 

**MainWindow:** Eine Instanz der Klasse *MainWindow* wird durch die Klasse *MainApplication*
erstellt. *MainWindow* beinhaltet die Unteransichten *FeedView*,
*EntryListView*, *EntryDetailsView* und *FeedOptionsView*. *MainWindow* arbeitet
mit einem Stack, für dessen Verwaltung die Klasse *ViewSwitcher* benutzt wird.
Bei einem Stack handelt es sich in diesem Zusammenhang um einen Container zur
Verwaltung der verschiedenen Ansichten -- ein Objekt der Klasse Gtk.Stack.

**ViewSwitcher:** Die Klasse *MainWindow* instanziiert einen *ViewSwitcher*.
Dieser ist für die Verwaltung der einzelnen Views zuständig.

**View:** *View* ist die abstrakte Oberklasse von *FeedView*, *EntryListView*,
*EntryDetailsView* und *FeedOptionsView*. *View* stellt für die Unterklassen
eine standardisierte Implementierung für eine Ansicht zur Verfügung. Innerhalb von *View* wird
die Suchleiste implementiert und verwaltet, die von den Unterklassen individuell
benutzt wird. *View* selbst erbt von Gtk.Grid und beinhaltet ein
Gtk.ScrolledWindow -- ein scrollbares Fenster -- das von den Unterklassen
benutzt wird, um Inhalte darzustellen.

**FeedView:** *FeedView* leitet von der Oberklasse *View* ab und beihnaltet
selbst n *FeedRows*. Diese spezialisierte View wird die vorhandenen Feeds
anzeigen.

**FeedRow:** Eine Instanz der Klasse *FeedRow* ist Bestandteil der Klasse
*FeedView*. *FeedView* selbst hat eine Listenansicht. Eine Zeile dieser Liste
entspricht einer *FeedRow*.

**IndicatorLabel:** Ermöglicht individualisierte Darstellung von Labels.
Innerhalb *gylfeed* werden die Labels für die Darstellung der Anzahl 
neuer, ungelesener und aller Nachrichten verwendet.
Die Klasse *IndicatorLabel* ist eine Spezialisierung von 
*Gtk.Label*.

**EntryListView:** *EntryListView* leitet von der Oberklasse *View* ab und
beinhaltet selbst n *EntryRows*. Diese spezialisierte View wird die vorhandenen
Entries anzeigen.

**EntryRow:** Eine Instanz der Klasse *EntryRow* ist Bestandteil der Klasse
*EntryListView*. *EntryListView* selbst hat eine Listenansicht. Eine Zeile dieser
Liste entspricht einer *EntryRow*.

**EntryDetailsView:** *EntryDetailsView* leitet von der Oberklasse *View* ab und
zeigt die Details eines einzelnen Entry an.

**FeedOptionsView:** *FeedOptionsView* leitet von der Oberklasse *View* ab und
beinhaltet sämtliche Optionen, die für einen Feed gesetzt werden können.


Erläuterung des Grundkonzepts von *gylfeed*
===========================================

Da die einzelnen Klassen nun bekannt sind, wird das in Abbildung 
:num:`funktionsprinzip` dargestellte Grundkonzept von *gylfeed* erläutert.
Die Darstellung zeigt die grundsätzliche Funktionsweise von *gylfeed*. Die
Akteure sind bereits aus dem Klassendiagramm bekannt.

Die Nummerierungen der Aktionen dienen zur Orientierung und werden an dieser
Stelle verwendet, um mit der Beschreibung des Diagramms zu beginnen.

Es wird angenommen, im Objekt Feed wird gefordert ein Update durchzuführen (1).
Dieser Auftrag wird an den Downloader weitergegeben. Dieser lädt die angefragten
Daten über das Web herunter (2). An dieser Stelle ist anzumerken, dass hier nicht
immer die kompletten Daten des Feeds heruntergeladen werden. Lässt es
die Struktur des betreffenden Feeds zu, wird nur dann ein kompletter Download
der Daten des Feeds durchgeführt, wenn sich dieser tatsächlich geändert hat.
Hier gibt es verschiedene Möglichkeiten festzustellen, ob eine Änderung vorliegt,
dies wird innerhalb der Bachelorarbeit näher betrachtet.

.. _funktionsprinzip:

.. figure:: ./figs/funktionsprinzip.png
    :alt: Das Grundkonzept von gylfeed.
    :width: 100%
    :align: center
    
    Das Grundkonzept von *gylfeed*.


Im nächsten Schritt empfängt der Downloader die Daten aus dem Web (3). 
Document wird vom Downloader als Future-Objekt verwendet (4).
Die Instanz des Documents wird an den Feed zur weiteren
Verarbeitung gegeben (5). Das Weiterverarbeiten im Feed wird dadurch ausgelöst,
indem sich der Feed auf ein Signal von der Instanz Document registriert. Sobald
das Document komplett heruntergeladen ist, wird das entsprechende Signal
ausgelöst und die im Document enthaltenen Daten werden im Feed geparst (6).
Signale werden im Anschluss an die Beschreibung der Abbildung näher erläutert.

Der Feed kommuniziert an den Feedhandler, dass er sich aktualisiert hat. Der
Feedhandler reicht das Signal an die Benutzeroberfläche weiter. Die Änderungen
werden grafisch dargestellt.

Im Feedhandler werden Updates ausgelöst, die manuell vom Benutzer angefordert
werden. Da dies für alle Feeds geschieht, ist es die Aufgabe des Feedhandlers, der
als Verwalter der Feeds funktioniert. Er lässt für jeden Feed eine
Aktualisierung durchführen. Die Aktualisierung im Feed selbst entspricht dem
Ablauf von den genannten Schritten (1) bis (6). Eine weitere Aufgabe des
Feedhandlers ist die persistente Speicherung der Daten, sowie das Laden dieser
Daten beim Start der Software.

Die Benutzeroberfläche kommuniziert Eingaben des Benutzers unter der Verwendung von
Signalen an die jeweilige logische Einheit. An dieser Stelle wird zum besseren
Verständnis das Konzept von Signalen innerhalb GTK kurz erläutert. Eine genaue
Betrachtung und Einzelheiten zu Signalen sind Bestandteil der Bachelorarbeit.

Als erstes sei erwähnt, dass GTK ereignisbasiert ist. GTK wartet solange, bis ein
Ereignis ausgelöst wird, beispielsweise durch einen Klick auf einen Button. GTK gibt dieses Ereignis an das
betreffende Widget weiter, hier der Button. Der Button löst in diesem Fall das
Signal *clicked* aus. Damit das Auslösen des Signals etwas bewirken kann, musste der Button 
bereits vorher mit diesem Signal verknüpft und eine entsprechende Callback-Funktion
zugewiesen werden. Die Callback-Funktion enthält den gewünschten Code, der ausgeführt
werden soll, wenn genau dieser Button angeklickt wird. 

.. raw:: latex

   \newpage

Folgendes kurze Codebeispiel soll das erläuterte Prinzip nochmals anschaulich
darstellen.


.. code-block:: python

    from gi.repository import Gtk

    #Callback-Funktion  
    def print_hello(button):
        print("Hello")

    button = Gtk.Button("Print Hello")          # Erstellen eines Buttons
    button.connect('clicked', print_hello)      # Verknüpfen mit Signal 'clicked'
                                                # und Angabe der Callback-Funktion

    window = Gtk.Window()                       # Erstellen eines Fensters
    window.add(button)                          # Hinzufügen von Button zu Fenster
    window.show_all()                           # Alle Bestandteile von window anzeigen

    Gtk.main()                                  # Gtk Main-Loop

Es können nicht nur bereits vorhandene Signale verwendet werden, sondern eigene
Signale definiert werden. Hierzu ist es notwendig, dass die Instanz, die ein
Signal anbieten möchte, von GObject.Object erbt. Innerhalb der Projektarbeit 
bietet beispielsweise die Klasse *Document* das Signal *finished* an. Die Klasse
Feed, die dieses Signal nutzen möchte verknüpft sich mit dem Signal. Feed ist
daran interessiert, benachrichtigt zu werden, sobald dieses Signal ausgelöst
wird. Beim Verknüpfen mit dem Signal ist ebenso wie in obigem Codeblock die
Angabe einer Callback-Funktion notwendig. Nun sind die Voraussetzungen
geschaffen, um im Quellcode bei Bedarf das Signal auszulösen. Beispielsweise
wird das Signal *finished* ausgelöst, wenn der asynchrone Download beendet ist.


Beschreibung der Schnittstellen
===============================

Das Grundkonzept von *gylfeed* ist vorgestellt und die Klassen sind bekannt. Nun
werden die öffentlich angebotenen Schnittstellen der Klassen vorgestellt.

**MainApplication:**

``__init__()``: Der Konstruktor der Klasse *MainApplication* ruft den
Konstruktor der Oberklasse Gtk.Application auf.

``do_activate()``: Zeigt laut Definition von Gtk.Application die erste
Standard-Ansicht der Anwendung an. In diesem Fall zeigt es das MainWindow,
das wiederum alle weiteren Ansichten beinhaltet, an.

``do_startup()``: Enthält die initialen Aktionen der Software. Es wird die
Klasse *Feedhandler* instanziiert, die Daten von der Festplatte geladen und eine
Instanz der Klasse *MainWindow* erstellt.

Die Funktionen ``do_activate()`` und ``do_startup()`` sind grundsätzlich
für eine Instanz, die von Gtk.Application ableitet, vorgegeben. Wird
Gtk.Application verwendet, ist es sinnvoll Gtk.ApplicationWindow als
Gegenstück zu verwenden. Dies setzt die Klasse *MainWindow* mit der Ableitung
von Gtk.ApplicationWindow um.


**Feedhandler**:

``__init__()``: Aufruf des Konstruktors der Oberklasse GObject.Object
ermöglicht in diesem Fall das Anbieten eigener Signale.

``create_feed(init_data)``: Erstellt ein Feedobjekt. Der Parameter ``init_data``
stellt ein Dictionary dar, das Schlüssel/Wert-Paare enthält. Diese sind URL,
Name des Feeds und alle weiteren Optionen, die für den Feed hinterlegt werden
können. Die Funktion verknüpft den Feed abschließend mit dem Signal *created*
und übergibt als Callback-Funktion die interne Funktion 
``_create_feed_deferred()``.

``update_all_feeds()``: Anhand der im Feedhandler geführten Liste *feeds*
wird ein Update für jeden Feed ausgelöst.

``delete_feed(feed)``: Löscht den im Funktionsaufruf übergebenen *Feed*.

``delete_old_entries()``: Ruft für jeden im Feedhandler geführten *Feed* 
deren Funktion delete_old_entries(max_days) auf.

``save_to_disk()``: Speichert die zu serialisierenden Daten auf Festplatte.
Hierzu wird die Hilfsfunktion ``get_serializable_data()`` herangezogen.

``load_from_disk()``: Lädt gespeicherte Daten von der Festplatte.


**Feed:**

``__init__(init_data, args)``: Der Konstruktor der Klasse *Feed* erwartet 
das Dictionary init_data. Darin enthalten sind alle Daten, die beim 
Hinzufügen des Feeds generiert wurden. Dazu gehören URL, Name des Feeds 
und alle weiteren Feed-Optionen. Neben init_data kann ein Flag für 
ein Icon, eine Referenz auf Feedhandler und der Typ des Feeds übergeben 
werden. Für diese Argumente - hier als args zusammengefasst - sind Default-Werte gesetzt, d.h. diese Argumente
müsssen nicht zwingend übergeben werden. 

``add_updater(update_interval=None)``: Fügt dem Feed unter Angabe des
Update-Intervalls in Minuten ein Timeout für das automatische Update hinzu. 

``update()``: Veranlasst für den aufgerufenen Feed ein Update. Hierzu wird die
Funktionalität der Klasse *Downloader* verwendet.

``delete_old_entries()``: Durchläuft die Entries eines Feeds 
und markiert diejenigen Entries als gelöscht, die dem Wert entsprechen, der in den
Einstellungen des Feeds gesetzt ist. Dieser Wert entspricht standardmäßig 30 Tagen
und kann durch den Benutzer geändert werden.

Die Klasse *Feed* bietet noch zahlreiche interne Funktionen. Ausgehend vom
Aufruf der Funktion ``update()`` wird beispielsweise intern die Funktion
``parse(document)`` aufgerufen. Hier werden die heruntergeladenen Daten
geparst.
Außerdem ist die Funktion ``compare_entries(new_raw_feed)`` enthalten. 
Diese Funktion vergleicht die neu heruntergeladenen Daten mit den bereits 
vorhandenen Daten im Feed und fügt die Differenz hinzu.

**SumFeed:**

``__init__(feedhandler)``: Der Konstruktor der Klasse *SumFeed* erwartet eine
Instanz der Klasse *Feedhandler*. Innerhalb des Konstruktors wird der
Konstruktor der Oberklasse *Feed* aufgerufen.

Ansonsten überschreibt *SumFeed* die Methoden von *Feed* in der Weise, dass
Daten aller Feeds in Summe abgefragt werden können. Dazu zählen die
Funktionen ``get_entries(), get_num_of_entries(), get_num_of_new_entries(),``
``get_num_of_unread(), get_num_of_counted() und get_name().``


**Downloader:**

``__init__()``: Der Konstruktor der Klasse *Downloader* erwartet keine
Parameter. Innerhalb des Konstruktors wird ein Standardwert für die
Paketgröße definiert, die zum Einlesen des Bytestreams verwendet wird.

``download(url, check_if_needed=True)``: Lädt Daten unter Verwendung der
angegebenen URL herunter. Das Flag *check_if_needed* wird dazu verwendet, um
entscheiden zu können, ob eine Vorprüfung stattfinden soll. Diese Vorprüfung
lädt vorerst den Header herunter und prüft, ob eine Änderung vorliegt. Dies
geschieht anhand der Parameter *etag* und *lastmodified* des HTTP-Headers. Wurde eine Änderung
festgestellt, oder ist weder *etag* noch *lastmodified* vorhanden, wird eine
interne Funktion von *Downloader* aufgerufen, die einen Download der 
kompletten Daten durchführt.


**Document:**

``__init__()``: Die Klasse *Document* ruft im Konstruktor den Konstruktor
von GObject auf. GObject ermöglicht in diesem Fall das Anbieten eigener
Signale.

Die Klasse *Document* ist ein Future-Objekt für den *Downloader*.
Die enthaltene Funktion ``_append(chunk)`` wird von der Klasse
*Downloader* solange aufgerufen, bis der eingehende Bytestream vollständig
gelesen ist. An dieser Stelle kommt die Funktion ``_finish()`` zum Einsatz.
Ist der Bytestream vollständig gelesen, löst die Funktion ``_finish()`` das
Signal *finish* aus. Anhand dieses Signals wird bespielsweise in den 
Instanzen von *Feed* die Funktion ``parse()`` aufgerufen.

.. raw:: latex

   \newpage

**MainWindow:**

``__init__(app, feedhandler)``: Der Konstruktor der Klasse *MainWindow*
erwartet eine Instanz der Klasse *MainApplication* -- hier app -- und eine Instanz
der Klasse *Feedhandler*. Innerhalb des Konstruktors wird der Konstruktor der
Oberklasse, Gtk.ApplicationWindow, aufgerufen. 

``add_widget_to_headerbar(widget, start_or_end)``: Fügt das übergebene
Widget der Header Bar hinzu. Mit start_or_end kann durch Übergabe eines 
Strings die Position des Widgets bestimmt werden.

``remove_widget_from_headerbar(widget)``: Entfernt das an die Funktion
übergebene Widget aus der Header Bar.

Neben diesen öffentlich angebotenen Schnittstellen hat *MainWindow*
zahlreiche interne Funktionen.


**ViewSwitcher:**

``__init__(stack)``: Der Konstruktor der Klasse *ViewSwitcher* bekommt den
Stack, der alle Views enthalten wird, zur Verwaltung übergeben. Da 
*ViewSwitcher* von Gtk.Box ableitet, erfolgt der Aufruf des Konstruktors 
von Gtk.Box.

``add_view(view, name)``: Fügt eine View in Verbindung mit dem übergebenen
Namen dem Stack hinzu.

``switch(name)``: Setzt anhand des übergebenen Namens die aktuell sichtbare
View. Hierbei werden alle notwendigen Aktionen ausgelöst, um die jeweilige View
und ihre Abhängikeiten korrekt darzustellen.


**View:**

``__init__(app, sub_title=None)``: Der Konstruktor der Klasse *View* bekommt
eine Instanz der Klasse *MainApplication* übergeben. Es ist möglich einen
Untertitel anzugeben. Hierfür ist der Standardwert *None* gesetzt. Innerhalb
des Konstruktors wird der Konstruktor der Oberklasse Gtk.Grid aufgerufen.

``add(widget)``: Nimmt ein *Widget* entgegen und fügt es der jeweiligen
Instanz von Gtk.ScrolledWindow
hinzu. Hier erfolgt eine Überschreibung der add-Funktion von Gtk.Grid.

``invalidate_filter(searchentry)``: Ruft die Funktion ``invalidate_filter()``
der Unterklasse auf.

``on_view_enter()``: Schnittstelle für alle Unterklassen, um Eigenschaften
beim Aufruf der jeweiligen Ansicht zu setzen. Ruft die Funktion 
``on_view_enter()`` der jeweiligen Unterklasse auf.

``on_view_leave()``: Schnittstelle für alle Unterklassen, um Eigenschaften 
beim Verlassen der jeweiligen Ansicht zu setzen. Ruft die Funktion 
``on_view_leave()`` der jeweiligen Unterklasse auf.

``manage_searchbar()``: Steuert das Verhalten der Suchleiste.


**FeedView:**

``__init__(app)``: Der Konstruktor der Klasse *FeedView* bekommt eine Instanz
der Klasse *MainApplication* übergeben. Innerhalb des Konstruktors wird der
Konstruktor der Oberklasse *View* aufgerufen.

``new_listbox_row(logo, feed)``: Erstellt eine Instanz der Klasse *FeedRow*
und fügt diese der Listbox innerhalb der *FeedView* hinzu. Als
Übergabeparameter sind das zu verwendende Logo und die Instanz des Feeds, der
hinzugefügt werden soll, erforderlich.

``on_view_enter()``: Führt alle Aktionen aus, die beim Aufruf von
*FeedView* notwendig sind. Beispielsweise die Aktualisierung der Labels, die
anzeigen, wieviele neue, ungelesene und gesamte Nachrichten ein Feed hat.

``on_view_leave()``: Führt alle Aktionen aus, die beim Verlassen von
*FeedView* notwendig sind.

``remove_feedrow(feed)``: Unter Angabe des Feeds, der gelöscht werden soll,
wird die *FeedRow* aus der Listbox von *FeedView* gelöscht.

``show_feedview(feedlist)``: Initiale Darstellung von *FeedView*
beim Start der Software. Erwartet wird eine Liste mit Feeds, die dargestellt
werden sollen.

**FeedRow:**

``__init__(logo, feed)``: Der Konstruktor der Klasse *FeedRow* erwartet ein
Logo und eine Instanz der Klasse *Feed*. Innerhalb des Konstruktors wird der
Konstruktor von Gtk.ListBoxRow aufgerufen, da *FeedRow* von Gtk.ListBoxRow
ableitet. 

``redraw_labels(sum_row)``: Aktualisiert die Labels, die anzeigen, wieviele
neue, ungelesene und gesamte Nachrichten ein Feed hat. Der Übergabeparameter
*sum_row* repräsentiert die *FeedRow*, in der die Zusammenfassung aller 
Feeds dargestellt wird.


**IndicatorLabel:**

``__init__(*args)``: Der Konstruktor der Klasse *IndicatorLabel* kann mehrere
Argumente übergeben bekommen, hierzu wird die Funktionalität ``*args`` der Python Sprachdefinition genutzt. 
Das erlaubt das Übergeben einer variablen Anzahl an Argumenten.
Innerhalb des
Konstruktors wird der Konstruktor der Oberklasse Gtk.Label aufgerufen.

``set_color(state)``: Setzt die Farbe des Labels anhand des Parameters *state*.
Dazu wird intern CSS verwendet. Möglich macht dies die Funktion ``set_markup()``
der Oberklasse Gtk.Label.


**EntryListView:**

``clear_listbox():`` Leert die Ansicht, um neu dargestellt werden zu 
können.

``on_view_enter()``: Führt alle Aktionen aus, die beim Aufruf von
*EntryListView* notwendig sind. Beispielsweise das Markieren von gelesenen
Entries.

``show_entries(listbox, row):`` Lässt die Entries eines Feeds darstellen. Als
Übergabeparameter wird die Listbox der *FeedView* erwartet und die darin
ausgewählte *Row*.

**EntryRow:**

``__init__(*args)``: Der Konstruktor der Klasse *EntryRow* erwartet mehrere
Argumente, hierzu wird ``*args`` verwendet. Beispielsweise sind dies Titel,
Zeitstempel und Plot des Feeds. Zusammenfassend alle Daten, die in einer
*EntryRow* dargestellt werden sollen. Innerhalb des Konstruktors wird der
Konstruktor der Oberklasse *Gtk.ListBowRow* aufgerufen.


**EntryDetailsView:**

``__init__(app)``: Der Konstruktor der Klasse *EntryDetailsView* bekommt
eine Instanz der Klasse *MainApplication* übergeben. Innerhalb des 
Konstruktors wird der Konstruktor der Oberklasse *View* aufgerufen.

``on_view_enter()``: Führt alle Aktionen aus, die beim Aufruf von
*EntryDetailsView* notwendig sind. Beispielsweise Einstellungen für den
View Switcher in der Header Bar.

``on_view_leave()``: Führt alle Aktionen aus, die beim Verlassen von
*EntryDetailsView* notwendig sind.

``show_entry_details(listbox, row)``: Lässt den ausgewählten Entry darstellen.
Als Übergabeparameter wird die Listbox der *EntryListView* erwartet und die
darin ausgwählte *Row*. Innerhalb der Funktion ``show_entry_details()`` werden
weitere interne Funktionen aufgerufen, die für die Darstellung des einzelnen
Entry notwendig sind.


**FeedOptionsView:**

``__init__(app)``: Der Konstruktor der Klasse *FeedOptionsView* bekommt 
eine Instanz der Klasse *MainApplication* übergeben. Innerhalb des 
Konstruktors wird der Konstruktor der Oberklasse *View* aufgerufen.

``on_view_enter()``: Führt alle Aktionen aus, die beim Aufruf von
*FeedOptionsView* notwendig sind. Beispielsweise werden in dieser Ansicht in
der Header Bar Buttons für zustimmende Aktionen und ablehnende Aktionen
angeboten. Dies wird je nach vorher gewählter Funktion passend dargestellt.
Das Hinzufügen eines Feeds erfordert andere Button-Beschriftungen, als der
Aufruf der Einstellungen eines bestehenden Feeds.

``on_view_leave()``: Führt alle Aktionen aus, die beim Verlassen von
*FeedOptionsView* notwendig sind. Beispielsweise das Entfernen von Buttons
aus der Header Bar.

``show_options_filled(feedview, feed)``: Zeigt die gespeicherten Einstellungen 
eines Feeds an. Als Übergabeparameter wird die *FeedView* und der gewählte *Feed* 
erwartet.


