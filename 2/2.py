#!/usr/bin/env python3
with open('input.txt') as file:
  f = file.read()

f = f.split('\n')
game_sets = []
games_res = []
checks = []

for game in f:
  r = game.find(':')
  color_sep_sem_col = game[r+2:].split(';')
  game_set_check = {}
  for k in range(len(color_sep_sem_col)):
    color_sep_commas = color_sep_sem_col[k].split(',')
    for j in range(len(color_sep_commas)):
      txt = color_sep_commas[j].strip()
      num_index = txt.find(' ')
      num = txt[:num_index]
      color = txt[num_index+1:]
      if color in game_set_check:
        game_set_check[color] = max(game_set_check[color], int(num))
      else:
        game_set_check[color] = int(num)
  checks.append(game_set_check)
  
  
powers = []
for k in range(len(checks)):
  product = 1
  for key, value in checks[k].items():
    product *=value
  powers.append(product)
  
print(sum(powers))
    
  
  


