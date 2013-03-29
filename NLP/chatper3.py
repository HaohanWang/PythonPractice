from __future__ import division
from HTMLParser import HTMLParser
import nltk, re, pprint
from urllib import urlopen
#class MLStripper(HTMLParser):
#    def __init__(self):
#        self.reset()
#        self.fed = []
#    def handle_data(self, d):
#        self.fed.append(d)
#    def get_data(self):
#        return ''.join(self.fed)
#
#def strip_tags(html):
#    s = MLStripper()
#    s.feed(html)
#    return s.get_data()

url = "http://fiction.eserver.org/novels/alexanders_bridge.html"
raw = urlopen(url).read()
t = nltk.clean_html(raw) 
tokens = nltk.word_tokenize(t)

text = nltk.Text(tokens)
print text.collocations()

