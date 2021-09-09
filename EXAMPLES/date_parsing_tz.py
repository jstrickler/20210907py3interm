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

time_ist = parser.parse(date_strings[0], tzinfos=tzinfos)
time_est = parser.parse(date_strings[2], tzinfos=tzinfos)
print(time_ist - time_est)
print(time_est - time_ist)

