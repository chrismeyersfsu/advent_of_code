#!/usr/bin/env python

import sys

def doit():
    with open('5.input', 'r') as f:
    #with open('5b.input.sample', 'r') as f:
        d = list(map(f.readline().rstrip().split(','))


    i = 0
    step = 0
    while i < len(d):
        inst = d[i]
        insts = str(inst)
        op = int(inst) if len(inst) == 1 else (10*int(insts[-2])) + int(insts[-1])
        poi1 = 0 if len(insts) <= 2 else insts[-3]
        poi2 = 0 if len(insts) <= 3 else insts[-4]
        poi3 = 0 if len(insts) <= 4 else insts[-5]

        print("{} {} {} {}".format(poi3, poi2, poi1, op))

        step = 4
        if op == 1:
            param1 = d[i+1] if poi1 else d[d[i+1]]
            param2 = d[i+2] if poi1 else d[d[i+2]]
            d[d[i+3]] = param1 + param2
        elif op == 2:
            param1 = d[i+1] if poi1 else d[d[i+1]]
            param2 = d[i+2] if poi1 else d[d[i+2]]
            d[d[i+3]] = param1 * param2
        elif op == 3:
            step = 2
            print("Give me input: ")
            input = sys.stdin.readline().rstrip()
            d[d[i+1]] = input
        elif op == 4:
            step = 2
            print("Output: {}".format(d[d[i+1]]))
        elif op == 99:
            return d
        else:
            print("Blarg! [{}] = {}".format(i, d[i]))
            return d
        i += step
    print("WTF? we got to the end of the ticker tape")

d = doit()
print("Pos 0 value is {}".format(d[0]))
