#!/usr/bin/env python 

from urllib import *
from re import *

def main():
    page1 = urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
    contents1 = page1.read()
    page1.close()
    
    pattern = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"
    
    matched = findall(pattern,contents1[22:-1])
    
    for char in matched:
        print char,
    
if __name__ == "__main__":
    main()