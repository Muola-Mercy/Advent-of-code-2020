# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 09:03:43 2020

@author: MERCY
"""
t = open('input.txt').read().split('\n')
test = ['F10','N3','F7','R90','F11']

def distance():
    d = [[1,0],[0,1],[-1,0],[0,-1]]
    di = 0
    y = 0
    x = 0
    i = 0
    while i < len(t):
        direction =t[i][0]
        step = int(t[i][1:])
        if direction == 'N':
            y -= step
        if direction == 'S':
            y += step
        if direction == 'E':
            x += step
        if direction == 'W':
            x -= step
        if direction == 'F':
            x += step * d[int(di)][0]
            y += step * d[int(di)][1]
        if direction == 'R':
            h = step/90
            di += h
            di %= 4
        if direction == 'L':
            h = step/90
            di += 4-h
            di %= 4
        i += 1
    return x+y
print('Part 1:',distance())

