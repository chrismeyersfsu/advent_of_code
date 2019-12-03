#!/usr/bin/env python

matrix = dict()

# #123 @ 3,2: 5x4

total = 0
ids = set()
with open('3.input', 'r') as f:
    for line in f:
        (id, rem) = line.split('@')
        (cord, rem) = rem.split(':')
        (w, h) = rem.split('x')

        (x, y) = cord.split(',')

        id = id.strip()[1:]
        x = int(x.strip())
        y = int(y.strip())

        w = int(w.strip())
        h = int(h.strip())

        #print("ID '{}' x,y '{},{}' w,h '{},{}'".format(id, x, y, w, h))
        if id in ids:
            print("Duplicate id found {}".format(id))
        ids.add(id)

        for i in range(x, x+w):
            for j in range(y, y+h):
                k = '{}x{}'.format(i, j)
                matrix[k] = matrix.get(k, 0) + 1

                if matrix[k] == 2:
                    total += 1


print("Total is {}".format(total))


