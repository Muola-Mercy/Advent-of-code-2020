# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:05:26 2020

@author: MERCY
"""
count = 0
count_two = 0
my_file=open("input.txt","r")
values = my_file.read()

input = values.splitlines()
print(len(input))

#my_file_two=open("trial.txt","r")
#value = my_file_two.read()
#trial = value.splitlines()

for inp in input:
    initial_split = inp.split(':')
    paswd = initial_split[1]
    split_two = initial_split[0].split()
    letter = split_two[1]
    nos = split_two[0].split('-')
    min_no = int(nos[0])
    max_no = int(nos[1])
    
    if (min_no <= paswd.count(letter) <= max_no):
        count +=1
    if ((paswd[min_no]==letter) ^ (paswd[max_no]==letter)):
        count_two +=1

print(count)
print(count_two)    