#!/usr/bin/env python
#

from functools import wraps  # <1>


def multiply(multiplier): # <2>  # decorator

    def deco(old_func): # <3>  # wrapper function

        @wraps(old_func)  # <4>
        def new_func(*args, **kwargs): # <5>
            result = old_func(*args, **kwargs) # <6>
            return result * multiplier # <7>

        return new_func # <8>

    return deco # <9>

# @foo
# def bar():
#     pass
#
# bar = foo(bar)


@multiply(4)
def spam():
    return 5

# spam = multiply(4)(spam)


@multiply(10)
def ham():
    return 8

a = spam()
b = ham()
print(a, b)
