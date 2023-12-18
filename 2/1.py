#!/usr/bin/env python3
with open('input.txt') as file:
  f = file.read()

f = f.split('\n')
target = {'red': 12, 'blue':14, 'green':13}
game_sets = []
games_res = []
checks = []

for game in f:
  r = game.find(':')
  color_sep_sem_col = game[r+2:].split(';')
  game_check = []
  for k in range(len(color_sep_sem_col)):
    color_sep_commas = color_sep_sem_col[k].split(',')
    for j in range(len(color_sep_commas)):
      txt = color_sep_commas[j].strip()
      num_index = txt.find(' ')
      num = txt[:num_index]
      color = txt[num_index+1:]
      if target[color] >= int(num):
        game_check.append(True)
      else:
        game_check.append(False)
  checks.append(game_check)

for k in range(len(checks)):
  if False not in checks[k]:
    games_res.append(k+1)   
print(sum(games_res))
    
  
  


