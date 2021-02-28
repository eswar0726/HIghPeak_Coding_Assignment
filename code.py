# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:08:21 2021

@author: eswar sai
"""

f = open('input_sa.txt','r')

with open('input_sa.txt') as f:
    read_data = f.readline()
        
    a = read_data.split(':')
    n = (int(a[1]))
    r2 = f.readline()
    r2 = f.readline()
    r2 = f.readline()
    di = dict()
    for _ in range(9):
        c = f.readline()
        a = c.split(':')
        di[a[0]] = int(a[1])
    
    di2 = dict(sorted(di.items(), key=lambda item: item[1]))
    a = list(di2.keys())
    an = []
    for i in range(0,len(a)):
        if(i+n-1<len(a)):
            an.append(di2[a[i+n-1]]-di2[a[i]])
    l1 = (an.index(min(an)))
    d = dict(list(di2.items())[l1:l1+n])
    print(d)

f1 = open("output.txt",'w')
f1.write("The goodies selected for distribution are: ")
f1.write("\n")
f1.write("\n")
for key,value in d.items():
    a = str(key + ":" + str(value))
    b = "gan"
    f1.write(a)
    f1.write("\n")
x="And the difference between the chosen goodie with highest price and the lowest price is " + str(min(an))
f1.write("\n")
f1.write(x)
f1.close()