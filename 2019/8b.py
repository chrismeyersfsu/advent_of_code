#!/usr/bin/env python
import sys

total = 0
with open('8.input', 'r') as f:
    input = f.readline().rstrip()

layers = []
count = 0
layer = []
for e in input:
    if count != 0 and count % (25*6) == 0:
        print(len(layer))
        assert len(layer) == (25*6)
        layers.append(layer)
        layer = []
    layer.append(int(e))
    count += 1

layers.append(layer)
print("Total layers {}".format(len(layers)))

for layer in layers:
    sys.stdout.write("{} ".format(layer[0]))
print("")

flayer = [" "]*25*6
for i in range(len(flayer)):
    for layer_index, layer in enumerate(layers):
        if layer[i] == 0:
            flayer[i] = ' '
            break
        if layer[i] == 1:
            flayer[i] = '#'
            break

for count, i in enumerate(flayer):
    sys.stdout.write(i)
    if count % 25 == 0:
        sys.stdout.write("\n")

sys.stdout.write("\n")

print(flayer)
