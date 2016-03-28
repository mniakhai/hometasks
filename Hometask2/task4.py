#!/usr/bin/python

from collections import Counter
with open('access.log') as file:
    count = Counter(line.split('- -', 1)[0].rstrip() for line in file)
for ip in count.most_common(10):
   print (ip[0]+": "+str(ip[1]) +"times")