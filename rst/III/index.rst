**************************
Kommunikation über Signale
**************************

Signale werden innerhalb von *gylfeed* verwendet, um ...
An dieser Stelle sollen die Hintergründe und theoretischen Grundlagen zu
Signalen näher betrachtet werden.


Hintergründe zu Signalen
========================

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





