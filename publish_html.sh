#!/bin/sh
# This is probably very prone to fail.

make html singlehtml && cp _build/*html /tmp -r;
git checkout gh-pages
rm *html -rf && cp /tmp/*html . -r
git add *html
git commit -am 'Automated update.'
git checkout master
