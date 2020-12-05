# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:21:38 2020

@author: MERCY
"""
from itertools import combinations

target_sum = 2020
my_file=open("input.txt","r")
values = my_file.read()

input = values.splitlines()
input = list(map(int, input))
#print(input)
 

def findPairs(lst, k): 
    y =  [pair for pair in combinations(lst, 3) if sum(pair) == k]
    x = y[0] #unpack the list
    a,b,c = x #unpack the tuple with the numbers
    print(y)
    print(b)
    print(c)
    print(a*b*c)# find the product of this numbers

    
    
print(findPairs(input, target_sum)) 
my_file.close()