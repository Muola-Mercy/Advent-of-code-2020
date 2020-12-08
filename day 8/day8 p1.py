# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:59:59 2020

@author: MERCY
"""

t = open('input.txt').read().split('\n')
def bootCode(lines):
    acc = 0
    ip = 0
    read_lines = []
    while ip >= 0 and ip < len(lines):
         
        [opa, arg] = lines[ip].split()
        if ip in read_lines:
            return acc
        read_lines.append(ip)
        if opa == 'acc':
            acc += int(arg)
            ip += 1
            
        elif opa == 'jmp':
            ip += int(arg)
              
        elif opa == 'nop':
            ip += 1

        #print(read_lines,len(read_lines))
acc= bootCode(t)
print(acc)

