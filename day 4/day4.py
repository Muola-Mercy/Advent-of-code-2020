# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 07:47:47 2020

@author: MERCY
"""

valid = 0

my_file=open("input.txt","r")
values = my_file.read()

input = values.strip().split("\n\n")

features = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

for inp in input:
    if all(x in inp for x in features):
        valid += 1
        
print(valid)
    