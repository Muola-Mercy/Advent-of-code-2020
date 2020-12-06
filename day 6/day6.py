# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:14:15 2020

@author: MERCY
"""
from collections import Counter
t = open('input.txt').read().split('\n\n')
#print(t)
test =['abc','a b c\n','ab ac','aaaa','a']

lens = []
k = 0
#part 1
for inp in t:
    inp_one = inp.split('\n')
    inp = inp.replace('\n','')
    inp = inp.replace(" ","")
    lens.append(len(set(inp)))
#part 2
    counter = (Counter(inp))
    for key in counter:
        if counter[key] == len(inp_one):
            k+= 1
    

        
print(sum(lens))
print(k)