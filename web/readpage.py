# for more information, check this website:
# http://www.boddie.org.uk/python/HTML.html
# -*- coding: utf-8 -*-
# python

from HTMLParser import HTMLParser
from urllib import urlopen
f =  urlopen("http://obamaspeeches.com/").read()

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
    return s.get_data()

print strip_tags(f)
