.. only:: latex

   .. raw:: latex

       \appendix

Abkürzungsverzeichniss
======================

.. figtable::
    :spec: >{\raggedleft\arraybackslash}p{0.25\linewidth} p{0.65\linewidth}

    =======================  ==================================
    Abkürzung                Bedeutung
    =======================  ==================================
    **API**                  Application Programming Interface
    **LoC**                  Lines of Code
    =======================  ==================================

.. only:: latex

   .. raw:: latex

       \newpage

Glossar
=======

.. glossary:: 

    Song

        Im Kontext von libmunin ist ein Song eine Menge von Attributen.
        Jedem Attribut ist, wie in einer Hashmap, ein Wert zugeordnet. 

        Beispielsweise haben alle Songs eine Attribut ``artist``, aber jeder
        einzelner Song kennt dafür einen bestimmten Wert.

        Desweiteren wird für jeden Song die Distanz zu einer Menge ähnlicher
        Songs gespeichert, sowie eine Integer der als Identifier dient.

    Distance

        Eine Distanz beschreibt die Ähnlichkeit zweier Songs oder Attribute. 
        Eine Distanz von 0 bedeutet dabei eine maximale Ähnlichkeit (oder
        minimale *Entfernung* zueiander), eine Distanz von 1.0 maximale
        Unähnlichkeit (oder maximale *Entfernung*).

        Die Distanz wird durch eine :term:`Distanzfunktion` berechnet.

    Distanzfunktion

        Eine Distanzfunktion ist im Kontext von libmunin eine Funktion die 
        zwei Songs als Eingabe nimmt und die :term:`Distance` zwischen
        diesen berechnet.

        Dabei schaut sie sich alle :term:`Attribut` an die beide Songs
        gemeinsam haben und nutzt für jedes gemeinsame Attribut eine
        spezialisierte Distanzfunktion die weiß wie diese zwei bestimmten Werte
        sinnvoll verglichen werden können. Die so errechneten Werte werden,
        gemäß der Gewichtung in der :term:`Maske`, zu einem Wert verschmolzen.

        Fehlen Attribute in einen der beiedn Songs wird für diese jeweils eine
        Distanz von 1.0 angenommen und ebenfalls in die gewichtete Oberdistanz
        eingerechnet.

        Die folgenden Bedingungen müssen sowohl für die allgemeine
        Distanzfuntkion, als auch für die speziellen Distanzfunktionen gelten:
 
        *Uniformität:*
        
        .. math::

            0 \leq D(i, j) \leq 1 \forall i,j \in D

        *Symmetrie:*

        .. math::

            D(i, j) = D(j, i) \forall i,j \in D

        *Identität:*

        .. math::

            D(i, i) = 0.0 \forall i \in D

        *Dreiecksungleichung:*

        .. math::

            D(i, j) \leq D(i, x) + (x, j)

    Session

        Eine *Session* ist eine Nutzung von libmunin über einem bestimmten
        Zeitraum. Zum Erstellen einer Session werden die Daten importiert,
        analysiert und ein :term:`Graph` wird daraus aufgebaut.
    
        Zudem kann eine *Session* persistent für späteren Gebrauch gespeichert
        werden. 

        Wer die Bibliothek benutzt wird die *Session* zudem als Eintrittspunkt
        für die API benutzen.

    Maske

        Die :term:`Session` benötigt eine Beschreibung der Daten die importiert
        werden. So muss ich darauf geeinigt werden was beispielsweise unter dem
        Schlüssel ``genre`` abgespeichert wird.
    
        In der *Maske* werden daher die einzelnen Attribute festgelegt die ein
        einzelner Song haben kann und wie diese anzusprechen sind. Zudem wird
        pro Attribut ein :term:`Provider` und eine :term:`Distanzfunktion`
        festgelegt die bei der Verarbeitung dieses Wertes genutzt wird. Zudem
        wird die Gewichtung des Attributes festgelegtes - manche Attribute sind
        für die Ähnlichkeit zweier Songs entscheidender als andere.

    Attribut

        Ein Attribut ist ein *Schlüssel* in der :term:`Maske`. Er repräsentiert
        eine Vereinbarung mit dem Nutzer unter welchem Namen das Attribut in
        Zukunft angesprochen wird. Zu jedem gesetzten Attribut gehort ein Wert,
        andernfalls ein spezieller leerer Wert. Ein Song besteht aus einer 
        Menge dieser Paare.

    Provider

        Ein *Provider* normalisiert einen Wert anhand verschiedener
        Charakteristiken. Sie dienen als vorgelagerte Verarbeitung von den Daten
        die in das System geladen werden. Jeder *Provider* ist dabei einem 
        :term:`Attribut` zugeordnet.

        Ihr Ziel ist für die :term:`Distanzfunktion` einfache und effizient 
        vergleichbare Werte zu liefern - da die :term:`Distanzfunktion` sehr
        viel öfters aufgerufen wird als der *Provider*.

    Assoziationsregel
        
        Eine Assoziationsregel verbindet zwei Mengen *A* und *B* von Songs
        miteinander. Wird eine der beiden Mengen miteinander gehört ist es
        wahrscheinlich dass auch die andere Menge daraufhin angehört wird.

        Sie werden aus dem Verhalten des Nutzers abgeleitet.

        Die Güte der Regel wird durch ein *Rating* beschrieben:

        .. math::

            Rating(A, B) = (1.0 - Kulczynski(A, B)) \cdot ImbalanceRatio(A, B)

        wobei:

        .. math::

            Kulczynski(A, B) =  \frac{P(A \vert B) + P(B \vert A)}{2}

        .. math::

            ImbalanceRatio(A, B) = \frac{\vert support(A) - support(B) \vert}{support(A) + support(B) - support(A \cup B)}


        .. admonition:: Vergleiche dazu:

            :cite:`datamining-concepts-and-techniques`
            Datamining Concepts and Techniques, Seiten 268-271.


    Recommendation

        Eine Recommendation (dt. Empfehlung) ist ein :term:`Song` der vom System
        auf Geheiß des Users hin vorgeschlagen wird. 

        Die Empfehlunge sollte eine geringe Distanz zum :term:`Seedsong` haben.

    Seedsong

        Ein Song der als Basis für Empfehlungen ausgewählt wurde. 

    Graph 

        Im Kontext von libmunin ist der Graph eine Abbildung aller Songs (als
        Knoten) und deren Distanz (als Kanten) untereinander. Im idealen Graphen
        kennt jeder :term`Song` *N* zu ihm selbst ähnlichsten Songs als
        Nachbarn.

        Da die Erstellung eines idealen Graphen sehr aufwendig ist wird auf
        eine schneller zu berechnende Approximation zurückgegriffen.

.. only:: latex

   .. raw:: latex

       \newpage


Online Ressourcen
=================

Zusätzlich zu dieser Arbeit findet sich komplementär weitere Ressourcen im Netz:

    * Github: Source code von libmunin

        https://github.com/sahib/libmunin

    * PyPi: Hosted ein fertig installierbares Paket von libmunin

        https://pypi.python.org/pypi/libmunin/

        Unter Unix installierbar via ``sudo pip install libmunin``.

        .. admonition:: Achtung:

            Dies funktioniert nur für Python Versionen ab ``3.2``!

    * TravisCI: Zeigt den Buildstatus der Tests von libmunin

        https://travis-ci.org/sahib/libmunin

    * HTML Dokumentation zur API:

        http://libmunin.readthedocs.org/en/latest/

    * Dieses PDF als HTML Version:

        http://sahib.github.io/libmunin-thesis/singlehtml/rst/index.html

.. only:: latex

   .. raw:: latex

       \newpage

