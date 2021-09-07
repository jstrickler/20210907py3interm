#!/usr/bin/env python
#
from dateutil import parser
from dateutil.tz import gettz

tzinfos = {
    'IST': gettz('Asia/Kolkata'),
    'AEST': gettz('Australia/Sydney'),
    'EST': gettz('US/Eastern'),
    'PST': gettz('US/Los_Angeles'),
}

print(tzinfos)

date_strings = [  # <1>
    '5 AM April 2, 2021 IST',
    '5 AM April 2, 2021 AEST',
    '5 AM April 2, 2021 EST',
]

for date_string in date_strings:
    print("{:25s}".format(date_string), end=' ')
    try:
        dt = parser.parse(date_string, tzinfos=tzinfos)  # <2>
        print(dt)
    except ValueError as err:
        print("Cannot parse")

t_ist = parser.parse(date_strings[0], tzinfos=tzinfos)
t_est = parser.parse(date_strings[2], tzinfos=tzinfos)
print(t_ist - t_est)
print(t_est - t_ist)

