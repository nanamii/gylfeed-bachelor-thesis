Bachelor Thesis for libhugin
============================

Based on a (quite heavily) modified version of *sphinxtr*:

    https://github.com/jterrace/sphinxtr

More details there.


Installation
============

.. code-block:: bash

   $ pip install -r requirements.txt

In contrast to original *sphinxtr*, this works with Python3 and does not
necessarily need a virtualenv, although you may want to consider it:

.. code-block:: bash

   # *before* the pip command above:
   $ virtualenv venv
   $ source ./venv/bin/activate

Configuration
=============

For configuring name, title and stuff, look into these files:

- ``tex/sphinx.sty`` (Titlepage)
- ``conf.py`` (Projectname, Author, Language (currently ``ngerman``))
- ``rst/index.rst`` (HTML Entydocument)
- ``rst/index_tex.rst`` (LaTeX Entrydocument)

Autobuild
=========

To do a autobuild on every save just run the convenience script:

.. code-block:: bash

   $ ./autobuild.sh
