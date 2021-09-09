from datetime import datetime
from functools import wraps

def spam():
    print("Hello from spam()")

def ham(func):
    func()

def toast(func):
    return func

def bacon(func):
    def temp():
        print("hello from some inner function")
        func()
    return temp

ham(spam)

f = toast(spam)
f()

spam = toast(spam)
spam()
print('-' * 60)

spam = bacon(spam)
spam()

@bacon
def marmalade():
    print("Hi from marmalade")

# marmalade = bacon(marmalade)
marmalade()

def weird(func):
    return 1

@weird
def victim():
    pass

print(victim)

def timestamp(func):  # decorator AND wrapper

    @wraps(func)
    def _new(*args, **kwargs):
        print(datetime.now())
        return func(*args, **kwargs)
    return _new

@timestamp
def foo(x):
    print("hello from foo(): value is", x)
# foo = timestamp(foo)

@timestamp
def bar(a, b):
    print("hello from bar(): values are", a, b)


foo(42)
bar("spam", "ham")
print(foo, bar, foo.__name__, bar.__name__)






