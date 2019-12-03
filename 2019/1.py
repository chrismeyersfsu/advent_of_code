#!/usr/bin/env python

total = 0
with open('1.input', 'r') as f:
    for line in f:
        total += int(int(line.rstrip()) / 3) - 2

print("Total is {}".format(total))


