# Mushroom

Mushroom try to resolve these problems:

1. pick the **KEYWORDS** from a given file or string.
2. pick the **KEYWORDS** from a large amount of indexed documents with filter.

I'm testing the [snownlp](https://github.com/isnowfy/snownlp) (which use TextRank) and [TermVectorComponent](http://wiki.apache.org/solr/TermVectorComponent) of SOLR (which use TF-IDF)

## Install

    $ python setup.py develop

## Usage

pick the **KEYWORDS** from a given file or string.

    $ python mushroom/cli.py -h
    Usage: cli.py [options]

    Options:
      -h, --help            show this help message and exit
      -f FILE, --file=FILE  read report from FILE
      -t TEXT, --text=TEXT  pass text instead of a file
