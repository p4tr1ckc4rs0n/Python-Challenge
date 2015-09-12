#!/usr/bin/env python

from urllib import *

# open webpage and read page source
page = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php")
contents = page.readlines()
page.close()

# line in page source we are concerned with
sline = contents[9].split()

# this is what we want to access the next page
numbers = ""

# loop to get initial digits from page source
for element in sline[1]:
    if element.isdigit():
        numbers += (str(element))

# function to automate going to next page and retrieving numbers        
def next_page(numbers):
    
    # define webaddress
    webaddress = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    
    # go to next page and retrieve numbers
    next_page = urlopen(webaddress+numbers)
    contents = next_page.readlines()
    for line in contents:
        numbers = line.split()[-1]
    return numbers

# divide by two and keep going
numbers = 16044/2
numbers = str(numbers)

# loop through 400 times as the challenege says
for i in xrange(401):
    numbers = next_page(numbers)
    print numbers
    
    # test and break loop if numbers variable does not contain numbers anymore
    if numbers.isdigit() == False:
        break