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

w = w*2
h = h*2
matrix = [[Entry(distance=None, points=[]) for x in range(h)] for y in range(w)]
print("Matrix {} x {}".format(w, h))
# Fill in the matrix with points
for p in points:
    m = matrix[p.x][p.y]
    m.points = [p]
    m.distance = 0

# Calc Euclidean distance for each point (Pythagorean theorem since 2d)
for x in range(w):
    for y in range(h):
        for p in points:
            if x == p.x and y == p.y:
                continue

            m = matrix[x][y]

            #dist = math.sqrt(pow((x - p.x), 2) + pow((y - p.y), 2))
            dist = abs(x - p.x) + abs(y - p.y)
            if len(m.points) == 0 or dist < m.distance:
                m.distance = dist
                m.points = [p]
            elif len(m.points) > 0 and dist == m.distance:
                m.points.append(p)

print("Done calculating distances")

candidate_points = set(points)
# Go around the edge and remove points as candidates
# left and down
# right and down
for y in range(h):
    if len(matrix[0][y].points) == 1:
        candidate_points.discard(matrix[0][y].points[0])
    if len(matrix[w-1][y].points) == 1:
        candidate_points.discard(matrix[w-1][y].points[0])

# top and to the right
# bottom and to the right
for x in range(w):
    if len(matrix[x][0].points) == 1:
        candidate_points.discard(matrix[x][0].points[0])
    if len(matrix[x][h-1].points) == 1:
        candidate_points.discard(matrix[x][h-1].points[0])

# of the candidate, find how much area it occupies
for x in range(w):
    for y in range(h):
        m = matrix[x][y]

        if len(m.points) > 1:
            continue
        if m.points[0] in candidate_points:
            m.points[0].total += 1

for p in candidate_points:
    print("Candidate point {} total {}".format(p.sid, p.total))

# Find the largest area
largest_area = 0
largest_point = None
for p in candidate_points:
    if p.total > largest_area:
        largest_area = p.total
        largest_point = p

print("Total is {}".format(largest_area))


'''
for x in range(w):
    for y in range(h):
        m = matrix[x][y]

        if len(m.points) == 1:
            if m.points[0].sid < 10:
                sys.stdout.write(' ')
            sys.stdout.write("{}".format(m.points[0].sid))
            sys.stdout.write(' ')
        else:
            sys.stdout.write('.. ')
    print("")
print("")
'''
