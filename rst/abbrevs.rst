.. One big hack.

.. only:: html or singlehtml or singletext

    **Abkürzungsverzeichnis**

.. raw:: latex

    \thispagestyle{plain}
    \renewcommand{\thepage}{\roman{page}}
    \setcounter{page}{7} % cough.
    \addcontentsline{toc}{section}{Abk"urzungsverzeichnis}
    {%
        \vspace*{2em}
        \Huge\textbf{Abk"urzungsverzeichnis}
        \vspace{1em}
    }%

.. figtable::
    :spec: >{\raggedleft\arraybackslash}p{0,25\linewidth} p{0,65\linewidth}

    =======================  ==================================
    Abkürzung                Bedeutung
    =======================  ==================================
    API                      *Application Programming Interface*
    CSS                      *Cascading Style Sheets*
    GTK                      *GIMP Toolkit*
    GUI                      *Graphical User Interface*
    HTML                     *Hypertext Markup Language*
    HTTP                     *Hypertext Transfer Protocol*
    PEP                      *Python Enhancement Proposals*
    RSS                      *Really Simple Syndication*
    URL                      *Uniform Resource Locator*
    XML                      *Extensible Markup Language*   
    =======================  ==================================

.. raw:: latex

    \newpage
    \renewcommand{\thepage}{\arabic{page}}
    \pagestyle{fancy}
    \setcounter{page}{1}
