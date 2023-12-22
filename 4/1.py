#!/usr/bin/env python3 
with open('input.txt') as file:
  f = file.read()
f = [e[e.find(':')+2:] for e in f.splitlines()]
winning_numbers = []
my_numbers = []

for card in f:
  r = card.split(' | ')
  winning_numbers.append(r[0].split(' '))
  my_numbers.append(r[1].split(' '))


card_scores = []
for k in range(len(my_numbers)):
  count = 1
  product = 0
  for j in range(len(my_numbers[k])):
    this_number = my_numbers[k][j]
    if len(this_number) > 0 and this_number in winning_numbers[k]:  #(some are one digits so split included empty strings)
      if count==1:
        product = 1
      else:
        product*=2
      count+=1
  card_scores.append(product)
  
print(sum(card_scores))