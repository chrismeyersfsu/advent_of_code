#!/usr/bin/env python3

range_start = 359282
range_end = 820401
diff = range_end-range_start

def has_adjacent_digits(num):
    s = str(num)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def increases_or_same(num):
    s = str(num)
    for i in range(len(s)-1):
        if s[i+1] < s[i]:
            return False
    return True

total = 0
for i in range(range_start, range_end):
    if has_adjacent_digits(i) and increases_or_same(i):
        total += 1

assert total < diff

print("Total is {}".format(total))


