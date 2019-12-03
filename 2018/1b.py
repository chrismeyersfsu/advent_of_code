#!/usr/bin/env python

total = 0
past = set()
while True:
    with open('1.input', 'r') as f:
        for line in f:
            if line[0] == '+':
                total += int(line[1:])
            else:
                total -= int(line[1:])

            if total in past:
                print("Found {}".format(total))
                raise RuntimeError()
            else:
                print("Not found {}".format(total))
            past.add(total)

print("Total is {}".format(total))


