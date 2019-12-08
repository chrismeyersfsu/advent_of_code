#!/usr/bin/env python

total = 0
with open('8.input', 'r') as f:
    input = f.readline().rstrip()

layers = []
count = 0
layer = []
for e in input:
    layer.append(int(e))
    if count != 0 and count % (25*6) == 0:
        layers.append(layer)
        layer = []
    count += 1

fewest = None
fewest_layer = None
fewest_layer_index = None
for layer_index, layer in enumerate(layers):
    total = 0
    for i in layer:
        if i == 0:
            total += 1

    print("Layer {} total 0's {}".format(layer_index, total))
    if fewest_layer_index is None or total < fewest:
        fewest = total
        fewest_layer = layer
        fewest_layer_index = layer_index


print("Fewest layer is {}".format(fewest_layer_index))

total = 0
ones = 0
twos = 0
for i in layers[fewest_layer_index]:
    if i == 1:
        ones += 1
    elif i == 2:
        twos += 1

total = ones * twos


print("Total {}".format(total))
