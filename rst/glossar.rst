.. One big hack.

.. only:: html or singlehtml or singletext

    **Glossar**

.. raw:: latex

    \thispagestyle{plain}
    \renewcommand{\thepage}{\roman{page}}
    \setcounter{page}{8} % cough.
    \addcontentsline{toc}{section}{Glossar}
    {%
        \vspace*{2em}
        \Huge\textbf{Glossar}
        \vspace{1em}
    }%

. 

.. glossary::

    
    Feed

     Ein Feed ist ein strukturiertes Datenformat welches von Webseiten verwendet
     wird, um Änderungen mitzuteilen. Als Beispiel soll die Sueddeutsche Zeitung
     als Anbieter eines Feeds genannt werden, der Änderungen im RSS-Format
     mitteilt. Hier spricht man vom *Feed* der Sueddeutschen Zeitung.

     Bezogen auf die Bachelorarbeit repräsentiert innerhalb der Software *gylfeed* ein Feed
     die Daten des ursprünglichen Feeds eines Anbieters.
   

    Feed-Daten

     Der Begriff *Feed-Daten* beschreibt innerhalb der Bachelorarbeit den Inhalt
     des Feeds, d.h. die Daten, die aus dem Web heruntergeladen und verarbeitet
     werden müssen. Das sind sämtliche Daten, die den Feed beschreiben (Titel des
     Feeds, Beschreibung, Datum der Veröffentlichung etc.) und die einzelnen
     Nachrichten, die durch den Feed veröffentlicht werden.
    
    Entry, auch Eintrag oder Nachricht 

     Ein Entry bezeichnet einen Eintrag eines Feeds. Ein Feed kann mehrere
     Entries besitzen. Es handelt sich jeweils um die einzelne Nachricht, die
     ein Feed veröffentlicht. Ein Entry enthält beispielsweise einen Titel, ein
     Bild, einen Zeitstempel und einen Plot. Ein Entry ist auch innerhalb
     *gylfeed* ein Teil eines Feeds. 
   

    GTK+

     Das GIMP Toolkit ist eine Bibliothek zur Erstellung grafischer Benutzeroberflächen.
     GTK+ findet vorwiegend im unixoiden Bereich Anwendung.
     
     
    Future Objekt

     Ein Future Objekt wird in der Softwareentwicklung als ,,Platzhalter" für
     ein ausstehendes Resultat verwendet. Über dieses Objekt kann das
     Ergebnis eines asynchronen Aufrufs abgefragt werden.

    XML

     Extensible Markup Language, ist eine Auszeichnungssprache zur baumartig
     strukturierten Darstellung von Daten in Form von Textdateien.


.. raw:: latex

    \newpage
    \renewcommand{\thepage}{\arabic{page}}
    \pagestyle{fancy}
    \setcounter{page}{1}
