__author__ = 'bgenc'

import urllib

class HTTPTreeNode:
    def __init__(self):
        self.type = None
        self.value = None

class HTTPTree:
    def __init__(self):
        headNode = None

s = urllib.urlopen("http://www.google.com")
