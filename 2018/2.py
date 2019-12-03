#!/usr/bin/env python

total_2 = 0
total_3 = 0
with open('2.input', 'r') as f:
    for line in f:
        unique = dict()
        for x in line:
            unique[x] = unique.get(x, 0) + 1

        found_2 = False
        found_3 = False

        for k, v in unique.iteritems():
            if v == 2:
                found_2 = True
            elif v == 3:
                found_3 = True

        if found_2:
            total_2 += 1
        if found_3:
            total_3 += 1

print("Total is {}".format(total_2*total_3))


