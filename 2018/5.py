#!/usr/bin/env python

from time import sleep
import copy

total = 0
data = ""
with open('5.input', 'r') as f:
    for line in f:
        data += line.strip()


orig_data = copy.copy(data)

smallest = None
smallest_letter = None
for letter_lower in range(ord('a'), ord('z')+1):
    letter_upper = chr(letter_lower - 32)
    letter_lower = chr(letter_lower)

    data = filter(lambda x: x not in [letter_lower, letter_upper], orig_data)

    data_len = len(data)

    i = 0
    while i < (len(data)-1):
        d1 = data[i]
        d2 = data[i+1]
        if ord(d1) == (ord(d2) - 32) or ord(d1) == (ord(d2) + 32):
            data = data[:i] + data[i+2:]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1

    maybe_smallest = len(data)
    if smallest is None:
        smallest = maybe_smallest
        smallest_letter = letter_upper
    elif maybe_smallest < smallest:
        smallest = maybe_smallest
        smallest_letter = letter_upper
    print("Data lens: {}, {}, {} filtered {} and {}".format(len(orig_data), data_len, len(data), letter_lower, letter_upper))

#print("{} {}".format(data, len(data)))
print("smallest {} {}".format(smallest_letter, smallest))



