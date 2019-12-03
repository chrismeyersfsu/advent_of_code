#!/usr/bin/env python

from parse import parse
import sys

nodes = dict()
with open('7.input', 'r') as f:
    for line in f:
        (parent, child) = parse("Step {} must be finished before step {} can begin.", line)

        nodes.setdefault(parent, set())
        nodes.setdefault(child, set()).add(parent)

count = 0
workers = [0 for i in range(5)]
left = set(nodes.keys())
done = set()
pending = [None for i in range(5)]
while len(nodes.keys()) != len(done):
    found_worker = False
    for n in sorted(list(left)):
        if all(p in done for p in nodes[n]):
            found_worker = False
            for i in range(5):
                if workers[i] == 0:
                    workers[i] = 60 + ord(n) - ord('A') + 1
                    print("Worker got {} {}".format(n, workers[i]))
                    pending[i] = n
                    found_worker = True
                    left.remove(n)
                    break
            if found_worker:
                break

    if not found_worker:
        increase_count = False
        for i in range(5):
            if workers[i] > 0:
                workers[i] -= 1
                increase_count = True
                if workers[i] == 0:
                    done.add(pending[i])
                    pending[i] = None
        if increase_count:
            count += 1





print("count {}".format(count))
