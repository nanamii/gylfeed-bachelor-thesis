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


.. figtable::
    :spec: >{\raggedleft\arraybackslash}p{0,25\linewidth} p{0,65\linewidth}

    =======================  ==================================
    Begriff                  Bedeutung
    =======================  ==================================
    Feed                      *Application Programming Interface*
    Entry                     *Graphical User Interface*
    Header Bar                *Really Simple Syndication*
    TRALALA                   *Uniform Resource Locator*
    GTK                       *Gnome Toolkit*
    =======================  ==================================

.. raw:: latex

    \newpage
    \renewcommand{\thepage}{\arabic{page}}
    \pagestyle{fancy}
    \setcounter{page}{1}
