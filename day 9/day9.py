# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 07:50:29 2020

@author: MERCY
"""
from itertools import combinations
t = open('input.txt').read().split('\n')
t = list(map(int, t))
test = open('test.txt').read().split('\n')
i = 0

def findPairs(lst): 
    #list,k
    i = 0
    while i >= 0 and i < len(lst):
        #line = lst[i]
        y = []

        check = lst[i:(i+25)]
        total = lst[i+25]
        #total = int(lst[i+25])

        #check = list(map(int, check))
        x =  [pair for pair in combinations(check, 2) if sum(pair) == total]
        y.append(x)
        if len(y[0]) == 0:
            return total

        i += 1
tar = findPairs(t)
print(tar)
def p2():
  l = 0
  r = 1
  s = t[l]

  while True:
    if s == tar:
      return min(t[l:r]) + max(t[l:r])
    if s < tar:
      s += t[r]
      r += 1
    if s > tar:
      s -= t[l]
      l += 1

print(p2())