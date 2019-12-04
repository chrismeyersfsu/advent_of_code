#!/usr/bin/env python

runs = []
lengths = []

with open('3.input', 'r') as f:
    for line in f:
        run = set()
        length = dict()
        runs.append(run)
        lengths.append(length)

        input = line.rstrip().split(',')

        paths = [(i[0], int(i[1:])) for i in input]

        x = 0
        y = 0
        len = 0
        for dir, dist in paths:
            assert dir in ['L', 'R', 'U', 'D']

            step = 1
            if dir in ['L', 'D']:
                step = -1

            if dir in ['L', 'R']:
                for i in range(dist):
                    x += step
                    run.add((x, y))
                    len += 1
                    if (x, y) not in length:
                        length[(x,y)] = len
            if dir in ['U', 'D']:
                for i in range(dist):
                    y += step
                    run.add((x, y))
                    len += 1
                    if (x, y) not in length:
                        length[(x,y)] = len

cords = runs[0] & runs[1]

distance = None
for cord in cords:
    dist = lengths[0][cord] + lengths[1][cord]
    if distance is None or dist < distance:
        distance = dist

print(distance)

