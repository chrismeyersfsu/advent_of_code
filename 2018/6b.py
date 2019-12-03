#!/usr/bin/env python

from collections import namedtuple
import uuid
import math, sys

total = 0
w, h = 0, 0;

class Entry():
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

points = []
count = 1
with open('6.input', 'r') as f:
    for line in f:
        (x, y) = line.split(', ')
        x = int(x) + 400
        y = int(y) + 400
        points.append(Entry(x=x, y=y, id=uuid.uuid4(), sid=count, total=0))

        count += 1

        w = x if x > w else w
        h = y if y > h else h

w = w+1
h = h+1
matrix = [[Entry(distance=None, points=[]) for x in range(h)] for y in range(w)]
print("Matrix {} x {}".format(w, h))
# Fill in the matrix with points
for p in points:
    m = matrix[p.x][p.y]
    m.points = [p]
    m.distance = 0

# Calc Euclidean distance for each point (Pythagorean theorem since 2d)
total_area = 0
for x in range(w):
    for y in range(h):
        total = 0
        for p in points:
            if x == p.x and y == p.y:
                continue

            m = matrix[x][y]

            #dist = math.sqrt(pow((x - p.x), 2) + pow((y - p.y), 2))
            dist = abs(x - p.x) + abs(y - p.y)
            total += dist

        if total < 10000:
            total_area += 1

print("Total area {}".format(total_area))
