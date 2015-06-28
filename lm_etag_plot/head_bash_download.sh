#!/bin/sh

for f in $(cat urlliste)
do
    curl -I -L $f  | grep "HTTP/1.1 200 OK" -A 1000  > file$(ls -l | wc -l)  
done
