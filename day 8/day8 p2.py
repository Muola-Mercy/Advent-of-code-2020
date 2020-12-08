# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:41:39 2020

@author: MERCY
"""

t = open('input.txt').read().split('\n')

def runprog(change):
  ip = 0
  acc = 0
  ran = set([])
  while ip >= 0 and ip < len(t):
    [i, p] = t[ip].split()
    if ip == change and i == 'nop':
      i = 'jmp'
    if ip == change and i == 'jmp':
      i = 'nop'
    if ip in ran:
      return False
    ran.add(ip)
    if i == 'acc':
      acc += int(p)
      ip += 1
    elif i == 'jmp':
      ip += int(p)
    elif i == 'nop':
      ip += 1
  return acc

for i in range(len(t)):
  ret = runprog(i)
  if ret is not False:
    print(ret)