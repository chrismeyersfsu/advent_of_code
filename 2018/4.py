#!/usr/bin/env python

from enum import Enum
from parse import parse
from dateutil import parser
from collections import OrderedDict
import collections



Entry = collections.namedtuple('Entry', 'timestamp id action sleeps sleep')

class Action(Enum):
    WAKEUP = 1
    SLEEP = 2
    SHIFT_START = 3

class Entry():
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

class Guard():
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

total = 0
ts = OrderedDict()
guards = dict()
with open('4.input', 'r') as f:
    for line in f:
        (timestamp, extra) = parse("[{}] {}", line)
        action = None
        guard_id = None

        timestamp = parser.parse(timestamp)

        if extra == "wakes up":
            action = Action.WAKEUP
        elif extra == "falls asleep":
            action = Action.SLEEP
        else:
            action = Action.SHIFT_START
            (guard_id,) = parse("Guard #{} begins shift", extra)

        entry = Entry(timestamp=timestamp, action=action, id=guard_id, sleeps=[], sleep=0)
        ts[timestamp] = entry

ts = OrderedDict(sorted(ts.iteritems(), key=lambda x: x))

id = None
sleep_start = None

'''
Parse in the data and sum up the total sleep for each guard
'''
for ts, e in ts.iteritems():
    print("timestamp {} action {} id {}".format(e.timestamp, e.action, e.id))

    if e.action == Action.SHIFT_START:
        id = e.id
    elif e.action == Action.SLEEP:
        sleep_start = e.timestamp
    elif e.action == Action.WAKEUP:
        print("Guard id is {}".format(id))
        guards.setdefault(id, Guard(sleep=0, id=id, sleeps=[]))

        diff = (e.timestamp - sleep_start).total_seconds() / 60
        guards[id].sleep += int(diff)
        guards[id].sleeps.append((sleep_start, e.timestamp))


minute_sleeps = dict()

'''
Find sleepiest guard
'''
largest_id = 0
largest_sleep_time = 0
for id, e in guards.iteritems():
    print("Guard {} Sleep {}".format(e.id, e.sleep))
    if e.sleep >= largest_sleep_time:
        largest_sleep_time = e.sleep
        largest_id = e.id

'''
Find minute of the day he/she was sleepiest
'''
e = guards[largest_id]
for s in e.sleeps:
    for m in range(s[0].minute, s[1].minute):
        v = minute_sleeps.get(m, 0)
        minute_sleeps[m] = v + 1

largest_minute_count = 0
largest_minute = 0
for minute, minute_sleep_count in minute_sleeps.iteritems():
    if minute_sleep_count > largest_minute_count:
        largest_minute = minute
        largest_minute_count = minute_sleep_count

print("Guard id {} minute most asleep {}".format(largest_id, largest_minute))

