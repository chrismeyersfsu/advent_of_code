#!/usr/bin/env python

total = 0
data = []
class Entry():
    def __init__(self, *args, **kwargs):
        for k,v in kwargs.iteritems():
            setattr(self, k, v)

with open('8.input2', 'r') as f:
    for line in f:
        res = line.split(' ')
        data.extend(res)


def get_entry(index, count=[]):
    if index >= len(data):
        return index
    print("Index is {}".format(index))

    child_count = int(data[index])
    meta_count = int(data[index+1])

    for i in range(child_count):
        index = get_entry(index+2, count)

    if index >= len(data):
        return index

    count[0] += sum(int(data[index+i]) for i in range(meta_count))
    print("Count[0] is now {}".format(count[0]))

    return index


count = [0]
res = get_entry(0, count)

print("Last index is {}".format(count[0]))


