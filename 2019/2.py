#!/usr/bin/env python

def doit():
    with open('2.input', 'r') as f:
        d = list(map(int, f.readline().rstrip().split(',')))

    d[1] = 12
    d[2] = 2

    i = 0
    while i < len(d):
        if d[i] == 1:
            print("add")
            d[d[i+3]] = d[d[i+1]] + d[d[i+2]]
        elif d[i] == 2:
            print("multiply")
            d[d[i+3]] = d[d[i+1]] * d[d[i+2]]
        elif d[i] == 99:
            print("end {}".format(d[0]))
            return d
        else:
            print("Blarg! [{}] = {}".format(i, d[i]))
            return d
        i += 4
    print("WTF? we got to the end of the ticker tape")

d = doit()
print("Pos 0 value is {}".format(d[0]))
