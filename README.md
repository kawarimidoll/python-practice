# python-practice

[Python実践入門 ──言語の力を引き出し、開発効率を高める：書籍案内｜技術評論社](https://gihyo.jp/book/2020/978-4-297-11111-3)

## Python Commands feat. Docker

REPL

```sh
docker run -it --rm python:3.8.1 python3
```

run single-line code

```sh
docker run -it --rm python:3.8.1 python3 -V
```

run script file

```sh
docker run -it --rm -v $(pwd):/usr/src/app -w /usr/src/app python:3.8.1 python3 hello.py
```

check annotation

```sh
docker run -it --rm -v $(pwd):/usr/src/app -w /usr/src/app python:3.8.1 bash -c "pip install mypy==0.740; mypy $@"
```

make environment:

[ref](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)

use variables in `.sh`

[ref](https://www.atmarkit.co.jp/ait/articles/1810/07/news001.html)
