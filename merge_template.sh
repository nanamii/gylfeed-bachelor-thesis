#!/bin/sh
git commit -am "Template change: $1"

git checkout pa
git merge master

git checkout ba
git merge master

git checkout master
