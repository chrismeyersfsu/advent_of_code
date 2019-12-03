#!/usr/bin/env python3

def doit():
    with open('2.input', 'r') as f:
        d = list(map(int, f.readline().rstrip().split(',')))

    d_init = d.copy()
    for a in range(0, 99):
        for b in range(0, 99):
            d = d_init.copy()

            d[1] = a
            d[2] = b
            print("a={} b={}".format(a, b))


            i = 0
            while i < len(d):
                if d[i] == 1:
                    d[d[i+3]] = d[d[i+1]] + d[d[i+2]]
                elif d[i] == 2:
                    d[d[i+3]] = d[d[i+1]] * d[d[i+2]]
                elif d[i] == 99:
                    if d[0] == 19690720:
                        print("end a={} b={}".format(a, b))
                        return d
                    else:
                        print("Clean break")
                    break
                else:
                    #print("Blarg! [{}] = {}".format(i, d[i]))
                    break
                i += 4
    print("WTF? we got to the end of the ticker tape")

d = doit()
print("Pos 0 value is {}".format(d[0]))
