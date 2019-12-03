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



'''
Find minute of the day he/she was sleepiest
'''
for id, e in guards.iteritems():
    minute_sleeps = dict()
    for s in e.sleeps:
        for m in range(s[0].minute, s[1].minute):
            v = minute_sleeps.get(m, 0)
            minute_sleeps[m] = v + 1
    setattr(e, 'minute_sleeps', minute_sleeps)

largest_minute_count = 0
largest_minute = 0
largest_guard_id = None
for id, e in guards.iteritems():
    for minute, count in e.minute_sleeps.iteritems():
        print("Sleeps {} {}".format(minute, count))
        if count > largest_minute_count:
            largest_minute = minute
            largest_minute_count = count
            largest_guard_id = e.id

print("Guard id {} largest minute {}".format(largest_guard_id, largest_minute))
