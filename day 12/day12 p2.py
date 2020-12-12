# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:09:13 2020

@author: MERCY
"""
lines = open('input.txt').read().split('\n')

x, y = 0, 0
wx, wy = 10, 1
for line in lines:
    action = line[:1]
    arg = int(line[1:])
    if action == 'F':
        x += wx * arg
        y += wy * arg
    if action == 'N':
        wy += arg
    if action == 'E':
        wx += arg
    if action == 'S':
        wy -= arg
    if action == 'W':
        wx -= arg
    if action == 'L':
        while arg:
            wx, wy = -wy, wx
            arg -= 90
    if action == 'R':
        while arg:
            wx, wy = wy, -wx
            arg -= 90

print('Part 2:',x+y) 