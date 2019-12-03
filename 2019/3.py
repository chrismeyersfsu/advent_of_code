#!/usr/bin/env python

runs = []

with open('3.input', 'r') as f:
    for line in f:
        run = set()
        runs.append(run)

        input = line.rstrip().split(',')

        paths = [(i[0], int(i[1:])) for i in input]

        x = 0
        y = 0
        for dir, dist in paths:
            assert dir in ['L', 'R', 'U', 'D']

            step = 1
            if dir in ['L', 'D']:
                step = -1

            if dir in ['L', 'R']:
                for i in range(dist):
                    x += step
                    run.add((x, y))
            if dir in ['U', 'D']:
                for i in range(dist):
                    y += step
                    run.add((x, y))

cords = runs[0] & runs[1]

distance = None
for cord in cords:
    dist = abs(cord[0]) + abs(cord[1])
    if distance is None or dist < distance:
        distance = dist

print(distance)






