#!/usr/bin/env python3
with open('input.txt') as file:
  f = file.read()

f = f.split('\n')
n = []
for k in f:
    first, last = None, None
    i, j = 0, -1
    while first == None or last == None:
        if k[i].isnumeric():
            first = k[i]
        if k[j].isnumeric():
            last = k[j] 
        if first is None: i+=1
        if last is None: j-=1 
    n.append(int(f'{first}{last}'))
print(sum(n))

