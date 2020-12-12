# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:01:05 2020

@author: MERCY
"""

lines = open('input.txt').read().split('\n')

def step(grid):
    newgrid = []
    search_min = -1
    search_max = 2
    for row in range(len(grid)):
        newrow = ''
        for col in range(len(grid[0])):
            adj = []
            for x in range(search_min,search_max):
                for y in range(search_min,search_max):
                    if x == y == 0:
                        continue
                    i = 1
                    while 0 <= row+i*x < len(grid) and 0 <= col+i*y < len(grid[0]):
                        ch = grid[row+i*x][col+i*y]
                        if ch != '.':
                            adj.append(ch)
                            break
                        i += 1
            if grid[row][col] == 'L' and '#' not in adj:
                newrow += '#'
            elif grid[row][col] == '#' and adj.count('#') >= 5:
                newrow += 'L'
            else:
                newrow += grid[row][col]
        newgrid.append(newrow)
    return newgrid


grid = lines
while True:
    after = step(grid)
    if after == grid:
        print('Part 2:',''.join(grid).count('#'))
        break
    grid = after
   