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

     Ein Feed bezeichnet im Kontext der Projektarbeit allgemein den Anbieter
     von Änderungen auf Webseiten in standardisierten Formaten. Als Beispiel
     soll die Sueddeutsche Zeitung als Anbieter genannt werden, der
     Änderungen im RSS-Format mitteilt. Hier spricht man vom *Feed* der
     Sueddeutschen Zeitung.

     Zusätzlich ist innerhalb *gylfeed* ein Feed eine Repräsentation des
     ursprünglichen Feeds.
    
    Entry

     Ein Entry ist innerhalb *gylfeed* ein Teil eines Feeds. Ein Feed kann
     mehrere Entries enthalten. Es handelt sich um die einzelne
     Nachricht, die ein Feed veröffentlicht. Ein Entry enthält beispielsweise
     einen Titel, ein Bild, einen Zeitstempel und einen Plot.
   
    
    Listbox

     Eine Listbox ist innerhalb *gylfeed* eine Instanz von Gtk.Listbox.
     Es handelt sich um einen Container, der mehrere Listbox Rows enthalten 
     kann.

    Listbox Row

     Eine Listbox Row ist Bestandteil einer Listbox und enthält selbst Daten,
     die auf der grafischen Benutzeroberfläche angezeigt werden. Innerhalb
     *gylfeed* werden Listbox Rows für die Anzeige von Feeds und die Anzeige
     von Entries in Listenform eingesetzt.

     
    XML

     Extensible Markup Language ist eine Auszeichnungssprache zur baumartig
     strukturierten Darstellung von Daten in Form von Textdateien.


.. raw:: latex

    \newpage
    \renewcommand{\thepage}{\arabic{page}}
    \pagestyle{fancy}
    \setcounter{page}{1}
