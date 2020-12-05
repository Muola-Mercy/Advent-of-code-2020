# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:47:41 2020

@author: MERCY
"""

my_file=open("input.txt","r")
values = my_file.read()

input = values.splitlines()
print(len(input))
print(len(input[0]))
z = 1
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for (dy,dx) in slopes:
    x = 0
    y = 0
    ans = 0
    while x+1 < len(input):
        x += dx
        y += dy
        if input[x][y%len(input[x])] == '#':
            ans += 1
    z *= ans
print(z)
