# -*- coding: utf-8 -*-
from __future__ import print_function
from optparse import OptionParser
from snownlp import SnowNLP
from HTMLParser import HTMLParser
import re

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    pattern = re.compile(r'\s')
    return re.sub(pattern, '', s.get_data())

def main(options):
    print("text")
    text = strip_tags(get_text(options))
    print(text)

    s = SnowNLP(text)
    print("Summary:")
    for summary in s.summary(3):
        print(summary)
    print("Keywords:")
    for keyword in s.keywords():
        print(keyword)

def get_text(options):
    if options.filename:
        with open(options.filename) as f:
            return f.read().decode('UTF-8')

    if options.text:
        return options.text.decode('UTF-8')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read report from FILE", metavar="FILE")
    parser.add_option("-t", "--text", dest="text",
                      help="pass text instead of a file", metavar="TEXT")

    (options, args) = parser.parse_args()
    main(options)
