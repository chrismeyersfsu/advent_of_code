#!/usr/bin/env python

from parse import parse
import sys

nodes = dict()
with open('7.inpu2', 'r') as f:
    for line in f:
        (parent, child) = parse("Step {} must be finished before step {} can begin.", line)

        nodes.setdefault(parent, set())
        nodes.setdefault(child, set()).add(parent)

left = set(nodes.keys())
while len(left) != 0:
    for n in sorted(list(left)):
        if all(p not in left for p in nodes[n]):
            left.remove(n)
            sys.stdout.write(n)
            break
print("")
