#!/usr/bin/env python3
with open('input.txt') as file:
  f = file.read()

f = f.split('\n')
n = []
vocab = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5, 'six': 6, 'seven':7, 'eight': 8, 'nine':9}

for k in f:
  first, last = None, None
  i, j = 0, len(k)-1
  while first == None or last == None:
  # so the longest character of the vocab is five letters long
  # smallest is three
    start, end = 5, 3
    while start >= end:
      sub = k[i:i+start]
      if sub in vocab.keys():
        for word in vocab.keys():
          if word in sub:
            first = vocab[word]
            break
      sub_last = k[j+1-start:] if j==len(k)-1 else k[j-start+1:j+1]
      if sub_last in vocab.keys():
        for word in vocab.keys():
          if word in sub_last:
            last = vocab[word]
            break
      start -=1
    if first is None and k[i].isnumeric():
      first = k[i]
    if last is None and k[j].isnumeric():
      last = k[j] 
    if first is None: i+=1
    if last is None: j-=1 
  n.append(int(f'{first}{last}'))

print(sum(n))