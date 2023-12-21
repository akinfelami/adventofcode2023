#!/usr/bin/env python3  
def walk_left(start, txt):
  res = ''
  done = False
  while not done:
    if start>=0: 
      if txt[start].isdigit():
        res+=txt[start]
      else:
        done=True
      start-=1
    else:
      done=True
  return None if len(res)==0 else res
      

def walk_right(start, txt):
  done = False
  res=''
  while not done:
    if start <len(txt):
      if txt[start].isdigit():
        res+=txt[start]
      else:
        done=True
      start+=1
    else:
      done=True
  return None if len(res)==0 else res
    
with open('input.txt') as file:
  f = file.read()
f = [e.split(',') for e in f.splitlines()]
adjascents = []
for k in range(len(f)):
  txt = f[k][0]
  asterik_index = 0
  while asterik_index < len(txt):
    found = False
    for char in txt[asterik_index:]:
      if char=='*':
        found=True
        break
      asterik_index+=1
    top = bottom = right = left = bottom_right = bottom_left = top_right = top_left = None
    if found:
      if k!=0:
        right_inter = walk_right(asterik_index, f[k-1][0])
        left_inter = walk_left(asterik_index, f[k-1][0])
        if (right_inter!=None and left_inter!=None):
          top = left_inter.strip()[::-1][:-1]+right_inter.strip()
        elif left_inter!=None and right_inter==None:
          top = left_inter[::-1]
        else:
          top = right_inter
      
      if k!=len(f)-1: 
        right_inter = walk_right(asterik_index, f[k+1][0])
        left_inter = walk_left(asterik_index, f[k+1][0])
        if (right_inter!=None and left_inter!=None):
          bottom = left_inter.strip()[::-1][:-1]+right_inter.strip()
        elif left_inter!=None and right_inter==None:
          bottom=left_inter[::-1]
        else:
          bottom = right_inter
      
      if asterik_index!= len(f[k][0])-1 :
        right = walk_right(asterik_index+1, f[k][0])
      
      if asterik_index!=0:
        left = walk_left(asterik_index-1, f[k][0])
        if left!=None: left=left[::-1]
      
      if top==None:
        if k!=0 and asterik_index!=len(f[k-1][0])-1: 
          top_right = walk_right(asterik_index+1, f[k-1][0])
              
        if k!=0 and asterik_index!=0 : 
          top_left = walk_left(asterik_index-1, f[k-1][0])
          if top_left!=None: top_left=top_left[::-1]
      
      if bottom==None:
        if k!=len(f)-1 and asterik_index!=len(f[k-1][0])-1:
          bottom_right = walk_right(asterik_index+1, f[k+1][0])
      
        if k!=len(f)-1 and asterik_index!=0 :
          bottom_left = walk_left(asterik_index-1, f[k+1][0])
          if bottom_left!=None: bottom_left=bottom_left[::-1]
      
      adjascents.append({'top': top , 'bottom': bottom, 'right': right, 'left':left, 'bottom_right': bottom_right,
          'bottom_left':bottom_left, 'top_right':top_right, 'top_left':top_left}
      ) 
    asterik_index+=1     
result = 0
for k in range(len(adjascents)):
  digis = []
  for key, value in adjascents[k].items():
    if value!=None:
      digis.append(int(value))
  if(len(digis))==2:
    product=1
    for d in digis:
      product*=d
    result+=product
  
print(result)
    
    
    