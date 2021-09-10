#!/usr/bin/env python

import requests

response = requests.get("https://www.python.org")  # <1>

for header, value in sorted(response.headers.items()): # <2>
    print(header, value)
print()

# response.text str
# response.content bytes  (raw)
print(response.text[:200])   # <3>
print('...')
print(response.text[-200:])   # <4>
