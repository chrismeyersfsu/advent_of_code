#!/usr/bin/env python

inputs = []

c2p = {}

def get_path(start):
    path = []
    parent = c2p[start]
    path.append(parent)
    while parent in c2p:
        parent = c2p[parent]
        path.append(parent)
    return path


with open('6.input', 'r') as f:
    inputs = [line.rstrip().split(')') for line in f]

for parent, child in inputs:
    c2p[child] = parent

you_path = get_path('YOU')
san_path = get_path('SAN')
san_set = set(san_path)

count = 0
for p in you_path:
    if p in san_set:
        index = san_path.index(p)
        count += index
        break
    count += 1

print("total is {}".format(count))


