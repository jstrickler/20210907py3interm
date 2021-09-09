#!/usr/bin/env python

def next_prime(limit):
    flags = set()  # <1>

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2 * i, limit + 1, i):
            flags.add(j)  # <2>
        yield i  # <3>   # "add" to virtual list


np = next_prime(200)  # <4>
for prime in np:  # <5>
    # next(np)
    print(prime, end=' ')
print()

def goofy_gen():
    yield "wombat"
    yield "possum"
    yield "koala"
    for letter in 'a', 'b', 'c':
        yield letter


gg = goofy_gen()
for thing in gg:
    print(thing)
print()
