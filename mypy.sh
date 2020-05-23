#!/bin/sh

docker run -it --rm -v $(pwd):/usr/src/app -w /usr/src/app python:3.8.1 bash -c "pip install mypy==0.740; mypy $@"
