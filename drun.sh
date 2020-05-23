#!/bin/sh

docker run -it --rm -v $(pwd):/usr/src/app -w /usr/src/app python:3.8.1 python3 $@
