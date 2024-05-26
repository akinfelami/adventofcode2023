#!/usr/bin/env python3
f = open('input.txt').read()
f = [e for e in f.splitlines() if e]

data = {'seed-to-soil map:': [], 'soil-to-fertilizer map:': [],
        'fertilizer-to-water map:': [], 'water-to-light map:': [],
        'light-to-temperature map:': [], 'temperature-to-humidity map:': [],
        'humidity-to-location map:': []}

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

locations = []
for seed in seeds:
    curr = seed
    for k, v in data.items():
        seg_len = 0
        while seg_len != len(v):
            dest, source, rang = [int(e) for e in v[seg_len].split(' ')]
            if curr in range(source, source+rang+1):
                curr = (int(curr) - source) + dest
                break
            seg_len += 1
    locations.append(curr)

print(min(locations))
