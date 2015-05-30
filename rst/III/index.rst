**************************
Kommunikation über Signale
**************************

Signale werden innerhalb von *gylfeed* einerseits verwendet, um Interaktionen vom Benutzer
zu erkennen und weiterzuleiten. Andererseits werden Signale für interne Abläufe
verwendet. An dieser Stelle sollen die Hintergründe und theoretischen Grundlagen zu
Signalen näher betrachtet und die Anwendung innerhalb von *gylfeed* erläutert
werden. --Hier, weil später immer wieder Konstrukte auftauchen, in denen Signale
involviert sind. --


GTK+ als Grundlage
==================

GTK+, das GIMP Toolkit, ist eine Bibliothek zur Erstellung grafischer
Benutzeroberflächen. Es bietet die Grundlage für die Verwendung von Signalen.
GTK+
wurde ursprünglich für das GNU Image Manipulation Programm (GIMP) entwickelt
(vgl. :cite:`gimp` -- offizielle Webseite von GIMP).
Dieser Ursprung blieb im Namen von GTK+ enthalten. Zwischenzeitlich wurde die
dritte Version von GTK+ entwickelt. GTK+ ist plattformübergreifend und unter der 
LGPL (GNU Lesser General Public License) lizenziert (vgl. :cite:`lgpl`).

Entwickelt wurde GTK+ in der Programmiersprache C. Language Bindings ermöglichen
es jedoch auch in anderen Programmiersprachen mit GTK+ zu entwickeln. Dazu zählen bespielsweise
Python, Perl, JavaScript oder C++ (vgl.
:cite:`language` -- Language Bindings für GTK+).

GTK+ basiert zu einem großen Teil auf der Bibliothek *GLib*. *GLib* stellt
beispielsweise Datenstrukturen zur Verfügung oder bietet einen Eventloop an.
Die Bibliothek *GObject* ist wiederum Teil von *GLib* und erleichtert innerhalb
C die objektorientierte Programmierung. Außerdem ermöglicht *GLib* eine eventbasierte Programmierung,
die beispielsweise für grafische Benutzeroberflächen eingesetzt wird.

Grafische Benutzeroberflächen, die mit GTK+ erstellt werden, bestehen aus
sogenannten Widgets. Ein Widget ist ein Element der grafischen
Benutzeroberfläche, das die Interaktion zwischen Benutzer und Software ermöglicht. Widgets sind
beispielsweise Buttons, Eingabefelder, Fortschrittsbalken oder ein einfaches
Label. Eine Übersicht dieser Widgets ist in der Online-Dokumentation von GTK+ zu
finden (vgl. :cite:`widgets` -- Widget-Gallerie von GTK+). Diese Widgets sind in
einer Hierarchie organisiert. In Abbildung :num:`widgethierarchie` ist
beispielhaft die Hierarchie bis zum Widget *Button* dargestellt. Die Hierarchie
aller Widgets ist unter :cite:`widgetsall` abrufbar. --> vl. in den Anhang?!!!???


.. _widgethierarchie:

.. figure:: ./figs/widgethierarchie.png
    :alt: Die Hierarchie der Widgets innerhalb GTK+ am Beispiel von Gtk.Button.
    :width: 50%
    :align: center
    
    Die Hierarchie der Widgets innerhalb GTK+ am Beispiel von Gtk.Button.



Der Main-Event-Loop
===================

Wenn es darum geht, verschiedene Events abzufangen, die jederzeit auftreten können und nicht
im Voraus geplant sind, ist der Main-Event-Loop im Zusammenspiel mit Signalen
interessant.
Um das Zusammenspiel von Main-Event-Loop und Signalen besser nachvollziehen zu können,
wurde der Ablauf in Abbildung :num:`mainloop` grafisch dargestellt.

.. _mainloop:

.. figure:: ./figs/mainloop.png
    :alt: Main-Event-Loop im Zusammenspiel mit Signalen.
    :width: 80%
    :align: center
    
    Main-Event-Loop im Zusammenspiel mit Signalen.

    
GTK+ verwendet ein eventbasiertes Konzept. Mit Hilfe der Abbildung
:num:`mainloop` soll dieses Konzept erläutert werden. Der *Main-Event-Loop* ist
in wartender Stellung und prüft zyklisch, ob ein Event aufgetreten ist. In
Zusammenspiel mit Signalen sieht ein typischer Ablauf eines Klicks auf einen
Button wie folgt aus. Unabhängig vom Abfangen und Weitergeben des
Events muss der Button zuvor mit einem Signal verbunden werden. Signale werden durch Strings
repräsentiert. Für das Klicken eines Buttons ist *clicked* der zugehörige
Signalname,
mit dem sich verbunden werden muss. Gleichzeitig muss beim Verbinden auf ein
Signal eine Funktion angegeben werden, die beim Auslösen des Signals ausgeführt
wird -- eine sogenannte Callback-Funktion. Zu einem beliebigen Zeitpunkt wird
nun der Button angeklickt. Dies löst ein Event aus, dass von dem
*Main-Event-Loop* abgefangen wird und an das jeweilige Widget, hier der Button,
weitergegeben wird. Empfängt der Button das Event, wird das Signal *clicked*
ausgelöst (emittiert) und die hinterlegte Callback-Funktion ausgeführt. Ist die
Callback-Funktion ausgeführt, kehrt GTK+ wieder zum *Main-Event-Loop* zurück und
es wird gewartet, bis das nächste Event auftritt.




Signale verwenden
=================

Im Folgenden wird die Verwendung von Signalen anhand von Beispielen näher
betrachet. Einerseits ist es möglich, Widgets mit deren bereits vorhandener
Signale zu verbinden, oder eigene Signale zu definieren.

Built-In Signale
----------------

Eigene Signale
--------------

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




Vorteile von Signalen
---------------------


Vergleich mit Observer-Pattern
------------------------------


Signale innerhalb *gylfeed*
===========================

In Abbildung ... ist die Verwendung von Signalen innerhalb *glyfeed*
dargestellt.





