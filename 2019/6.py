#!/usr/bin/env python

total = 0
inputs = []

c2p = {}

with open('6.input', 'r') as f:
    inputs = [line.rstrip().split(')') for line in f]

for parent, child in inputs:
    c2p[child] = parent

for child, parent in c2p.items():
    total +=1
    while parent in c2p:
        parent = c2p[parent]
        total += 1


print("total is {}".format(total))


