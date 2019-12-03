#!/usr/bin/env python

total_2 = 0
total_3 = 0
boxes = []
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

        boxes.append(line.strip())


def diff1(x, y):
    if len(x) != len(y):
        return []

    found_diff = False
    diff_index = -1
    for i in range(0, len(x)):
        if x[i] != y[i]:
            if found_diff == True:
                return []
            found_diff = True
            diff_index = i

    if not found_diff:
        return []

    return x[:diff_index] + x[(diff_index+1):]


for i in range(0, len(boxes)):
    box1 = boxes[i]
    for j in range(i+1, len(boxes)):
        box2 = boxes[j]
        res = diff1(box1, box2)
        if len(res) > 0:
            print("Found entry {}".format(res))



