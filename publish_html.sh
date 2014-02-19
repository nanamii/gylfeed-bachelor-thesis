#!/bin/sh
# This is probably very prone to fail.

function build {
    git checkout ${1} &&
    BUILD_PATH=/tmp/.build-${1} &&
    mkdir -p ${BUILD_PATH} && 
    make clean html && cp _build/*html ${BUILD_PATH} -r &&
    git checkout master
}

function copy {
    git checkout gh-pages &&
    BUILD_PATH=/tmp/.build-${1} &&
    rm ${1} -rf && 
    mkdir -p ${1} 
    cp ${BUILD_PATH}/*html $1 -r &&
    git add $1 && 
    git commit -am 'Automated update.' &&
    git checkout master
}

build project
build bachelor

copy project
copy bachelor
