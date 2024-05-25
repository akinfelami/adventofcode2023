#!/usr/bin/env python3
f = open('input.txt').read()
f = [e for e in f.splitlines() if e]

data = {'seed-to-soil map:': [], 'soil-to-fertilizer map:': [],
        'fertilizer-to-water map:': [], 'water-to-light map:': [], 'light-to-temperature map:': [], 'temperature-to-humidity map:': [], 'humidity-to-location map:': []}

# destination range start, source range start, range length
seeds = [int(e) for e in f[0][f[0].find(':')+1:].split()]

for k in range(len(f)):
    if f[k] in data:
        j = k+1
        try:
            while f[j] not in data:
                data[f[k]].append(f[j])
                j += 1
        except IndexError:
            pass

s_2_s = data['seed-to-soil map:']
s_2_f = data['soil-to-fertilizer map:']
f_2_w = data['fertilizer-to-water map:']
w_2_l = data['water-to-light map:']
l_2_t = data['light-to-temperature map:']
t_2_h = data['temperature-to-humidity map:']
h_2_l = data['humidity-to-location map:']


locations = []
for seed in seeds:
    s = f = w = lt = t = h = l = None
    for entry in s_2_s:
        dest, source, rang = [int(e) for e in entry.split(' ')]
        if seed in range(source, source+rang+1):
            s = (int(seed) - source) + dest
            break
    if s is None:
        s = int(seed)

    for entry in s_2_f:
        dest, source, rang = [int(e) for e in entry.split(' ')]
        if s in range(source, source+rang+1):
            f = (int(s) - source) + dest
            break
    if f is None:
        f = int(s)

    for entry in f_2_w:
        dest, source, rang = [int(e) for e in entry.split(' ')]
        if f in range(source, source+rang+1):
            w = (int(f) - source) + dest
            break
    if w is None:
        w = int(f)

    for entry in w_2_l:
        dest, source, rang = [int(e) for e in entry.split(' ')]
        if w in range(source, source+rang+1):
            lt = (int(w) - source) + dest
            break
    if lt is None:
        lt = int(w)

    for entry in l_2_t:
        dest, source, rang = [int(e) for e in entry.split(' ')]
        if lt in range(source, source+rang+1):
            t = (int(lt) - source) + dest
            break
    if t is None:
        t = int(lt)

    for entry in t_2_h:
        dest, source, rang = [int(e) for e in entry.split(' ')]
        if t in range(source, source+rang+1):
            h = (int(t) - source) + dest
            break
    if h is None:
        h = int(t)

    for entry in h_2_l:
        dest, source, rang = [int(e) for e in entry.split(' ')]
        if h in range(source, source+rang+1):
            l = (int(h) - source) + dest
            break
    if l is None:
        l = int(h)

    locations.append(l)

print(min(locations))
