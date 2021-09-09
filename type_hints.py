import inspect

class Dog:
    pass

d = Dog()

class Cat:
    pass

c = Cat()

def spam(a: int, b: str, c: Dog) -> float:
    print(b)
    return a / 2

x = spam(5, "abc", d)
print(x)

x = spam(9.7, 123, c)
print(x)

print(inspect.getfullargspec(spam))
