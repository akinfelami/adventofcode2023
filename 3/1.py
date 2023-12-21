#!/usr/bin/env python3  
import json
with open('test.txt') as file:
  f = file.read()
f = [e.split(',') for e in f.splitlines()]
res = []
for k in range(len(f)):
  txt = f[k][0]
  track_index = 0
  next_start = 0
  track_iter = txt[:]
  while track_index < len(txt):
    numeric_digits=''
    for char in track_iter:
      track_index+=1
      if char.isdigit():
          numeric_digits += char
      else:
          break  
    track_iter = txt[track_index:]
    if(len(numeric_digits)>0):
      top = bottom = right = left = bottom_right = bottom_left = top_right = top_left = None
      adjascents = []
      for l in range(next_start, len(numeric_digits)+next_start):
        if k!=0: top = f[k-1][0][l]
        if k!=len(f)-1: bottom = f[k+1][0][l]
        if l!= len(f[k][0])-1 : right = f[k][0][l+1]
        if l!=0: left = f[k][0][l-1]
        if k!=0 and l!=len(f[k-1][0])-1 : top_right = f[k-1][0][l+1]
        if k!=0 and l!=0 : top_left = f[k-1][0][l-1]
        if k!=len(f)-1 and l!=len(f[k-1][0])-1 : bottom_right = f[k+1][0][l+1]
        if k!=len(f)-1 and l!=0 : bottom_left = f[k+1][0][l-1]
        adjascents.append({'top': top , 'bottom': bottom, 'right': right, 'left':left, 'bottom_right': bottom_right,
            'bottom_left':bottom_left, 'top_right':top_right, 'top_left':top_left}
        )
        
      found = False
      for u in range(len(adjascents)):
        for key, value in adjascents[u].items():
          if value!=None and value!='.' and value.isdigit()==False and found==False: # then it is a special character
            found=True
            res.append(int(numeric_digits))
        
    next_start = track_index

print(sum(res))
        