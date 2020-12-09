# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:51:04 2020

@author: MERCY
"""

lines = open('input.txt').read().split('\n')
total = 0
bags = {}

#prt 1
def fb(xg,x):
    colours = []
    all_colours = []
    for k in xg:
        for y in xg[k]:
            if y[1] == x:
                colours.append(k)       
    for colour in colours:
        all_colours.append(colour)
        bags = fb(xg,colour)
        all_colours += bags  
    return set(all_colours)

for line in lines:
  line = line.replace('.', '')
  a, b = line.split(' bags contain ')
  toks = b.split(',')
  for tok in toks:
    tok = tok.strip()
    if tok == 'no other bags':
      continue
    c, d = tok.split(' ', 1)
    c = int(c)
    d = d.replace('bags', '').replace('bag', '').strip()
    #print('Edge from', a, 'to', d)
    if a not in bags:
      bags[a] = []
    bags[a].append((c, d))

print(len(fb(bags,'shiny gold')))
# part 2
def counts(xg,x):
    s = 1
    if x not in xg:
        xg[x] = []
    for n, y in xg[x]:
        s += n * counts(xg, y)
    return s
            
print((counts(bags,'shiny gold'))-1)
