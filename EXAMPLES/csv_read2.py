#!/usr/bin/env python
import csv

with open('../DATA/knights.csv') as knights_in:
    rdr = csv.reader(knights_in, dialect='excel')  # <1>
    for row in rdr:  # <2>
        print(row)
