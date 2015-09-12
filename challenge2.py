#!/usr/bin/env python

import string
from urllib import *

print "="*70

print "running challenge2..."

def main():
    page = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
    contents = page.readlines()
    page.close()

    alpha = "abcdefghijklmnopqrstuvwzy"
    sense = ""

    for line in contents[38:]:
        for element in line:
            if element in alpha:
                sense += element
    
    print "this is what i found amongst mess:", sense
    
    print "="*70
    
if __name__ == "__main__":
    main()