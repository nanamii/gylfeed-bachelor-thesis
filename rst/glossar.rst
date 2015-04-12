.. One big hack.

.. only:: html or singlehtml or singletext

    **Glossar**

.. raw:: latex

    \thispagestyle{plain}
    \renewcommand{\thepage}{\roman{page}}
    \setcounter{page}{9} % cough.
    \addcontentsline{toc}{section}{Glossar}
    {%
        \vspace*{2em}
        \Huge\textbf{Glossar}
        \vspace{1em}
    }%

. 

.. glossary::

    
    Feed

     Ein Feed Tralalala.
    
    Entry

     Ein auf PC--Komponenten basierendes Gerät zur Wiedergabe multimedialer
     Inhalte. Dieser wird oft mit sogenannter Media--Center--Software wie dem
     XBMC betrieben.

    Listbox



    XML

     Extensible Markup Language, eine Auszeichnungssprache zur baumartig
     strukturierten Darstellung von Daten in Form von Textdateien.

    JSON

     JavaScript--Object--Notation, eine Auszeichnungssprache ähnlich wie *XML*
     mit dem Ziel, von Mensch und Maschine einfacher lesbar zu sein als *XML*.


.. raw:: latex

    \newpage
    \renewcommand{\thepage}{\arabic{page}}
    \pagestyle{fancy}
    \setcounter{page}{1}
