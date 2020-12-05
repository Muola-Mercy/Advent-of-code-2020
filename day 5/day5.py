# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:11:30 2020

@author: MERCY
"""
import numpy as np
i = 0
seats = []
t = open('input.txt').read().split('\n')


for inp in t:
    row_range = 64
    row = 0
    col = 0
    col_range = 4
    for c in inp:
        if c == 'F':
            row_range /= 2
        elif c == 'B':
            row += row_range
            row_range //= 2
        elif c == 'R':
            col += col_range
            col_range //= 2
        elif c == 'L':
            col_range //= 2
    seat_no = (row*8)+col
    seats.append(seat_no)
    
#part 1        
print(max(seats))

# part 2
seat = sorted(seats)

while i+1 < len(seat):
    if seat[i+1] - seat[i] == 2:
        print(seat[i]+1)
    i += 1

