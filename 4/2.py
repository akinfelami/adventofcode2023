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

cards_and_counts = []
original_matches = [0 for k in range(len(f))]
for k in range(len(my_numbers)):
  count = 0
  for j in range(len(my_numbers[k])):
    this_number = my_numbers[k][j]
    if len(this_number) > 0 and this_number in winning_numbers[k]:  #(some are one digits so split included empty strings)
      count+=1
  cards_and_counts.append(count)

for k in range(len(original_matches)):
  stat = 1
  while stat < cards_and_counts[k]+1:
    original_matches[k+stat]+=1
    stat+=1
  stat = 1
  while stat < cards_and_counts[k]+1:
    original_matches[k+stat]+=original_matches[k]
    stat+=1


original_matches = [k+1 for k in original_matches]
print(sum(original_matches))