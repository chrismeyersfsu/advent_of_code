#!/usr/bin/env python

def fake_recursion(mass):
    total = 0
    fuel = mass
    while True:
        remainder = int(int(fuel) / 3) - 2
        if remainder < 0:
            return total
        total += remainder

        fuel = remainder

total = 0
with open('1.input', 'r') as f:
    for line in f:
        total += fake_recursion(line.rstrip())

print("Total is {}".format(total))


