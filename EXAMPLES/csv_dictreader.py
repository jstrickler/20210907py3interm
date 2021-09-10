#!/usr/bin/env python
import csv

field_names = ['term', 'firstname', 'lastname', 'birthplace', 'state', 'party'] # <1>

with open('../DATA/presidents.csv') as presidents_in:
    # header_row = next(presidents_in)
    # fieldnames = header_row.split(',')
    rdr = csv.DictReader(presidents_in, fieldnames=field_names)  # <2>
    for row in rdr:  # <3>
        print('{:25s} {:12s} {}'.format(row['firstname'], row['lastname'], row['party']))  # <4>
        # string .format can use keywords from an unpacked dict as well:
        # print('{firstname:25s} {lastname:12s} {party}'.format(**row))
