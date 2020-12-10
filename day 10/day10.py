# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 08:13:06 2020

@author: MERCY
"""
#part 1
t = open('input.txt').read().split('\n')
t = list(map(int, t))
to = sorted(t)

def joltDiff():
    diff = []
    i = 0
    diff.append(to[0]-0)
    while i >= 0 and i < len(to):
        dif = 0
        if i == len(to)-1:
            dif = 3
            diff.append(dif)
            return diff.count(1)*diff.count(3)
        dif = to[i+1] - to[i]
        diff.append(dif)
        i += 1
      
print('Part 1:',joltDiff())
# part 2
t.append(0)
t.sort()
n = len(t)
dp = [0] * n
dp[0] = 1

for i in range(1, n):
  for j in range(i):
    if (t[i] - t[j] <= 3):
      dp[i] += dp[j]
     # print(t[i], t[j], dp[i], dp[j])

print('Part 2:',dp[n - 1])
    