#!/usr/bin/env python

total = 0
with open('1.input', 'r') as f:
    for line in f:
        if line[0] == '+':
            total += int(line[1:])
        else:
            total -= int(line[1:])

print("Total is {}".format(total))


