#!/usr/bin/env python
import pickle

infile = pickle.load(open("banner.p"))
for item in infile:
    for thing in item:
        print thing[0]*thing[1],
    print ""