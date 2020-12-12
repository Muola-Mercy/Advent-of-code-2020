# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:42:32 2020

@author: MERCY
"""

t = open('input.txt').read().split('\n')

def check_neighbour(grid,check_row , check_column):

    search_min = -1
    search_max = 2

    neighbour_list = []
    for x in range(search_min,search_max):
        for y in range(search_min,search_max):
            neighbour_row = check_row + x
            neighbour_column = check_column + y 

            valid_neighbour = True

            if (neighbour_row) == check_row and (neighbour_column) == check_column:
                valid_neighbour = False

            if (neighbour_row) < 0 or (neighbour_row) >= len(grid):
                valid_neighbour = False

            if (neighbour_column) < 0 or (neighbour_column) >= len(grid[0]):
                valid_neighbour = False

            if valid_neighbour:
                neighbour_list.append(grid[neighbour_row][neighbour_column])

    return neighbour_list  

def update_seats(grid):

    new_grid = []
    for i in range(len(grid)):
        new_row = ''
        for j in range(len(grid[0])):
            neighbours = check_neighbour(grid,i,j)
       
            if( grid[i][j]=='#' and neighbours.count('#') >= 4):
                new_row += 'L'
            elif(grid[i][j]=='L' and neighbours.count('#') == 0):
                new_row += '#'
            else:
                new_row += grid[i][j]
        new_grid.append(new_row)

    return new_grid
grid = t

while True:
    after = update_seats(grid)

    if after == grid:
        occupied = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '#':
                    occupied+= 1
        print('Part 1:',occupied)

        break
    grid = after

    

    

        
    
