from copy import deepcopy

user_name = "Bob"

x = 10 # initialize x with 10
y = x  #  y refers to same object as x
print(x, y)
x = "football"
print(x, y)

values = ['a', 'b', 'c', [1, 2, 3]]
v1 = values  # alias
v1.append('wombat')
print(values, v1)

def add_something(array, value):
    array.append(value)

add_something(values, "koala")
add_something(v1, "wallaby")
print(values, v1)

v2 = list(values) # v2 = values[::]  # shallow copy
v2.append("kangaroo")
print(values, v2)
v2[3].append(42)
print(values, v2)

v3 = deepcopy(values)
v3[3].append(1000)
print(values, v3)

del v2  #

x = None

values.append(None)

flags = [None] * 10  # multiply sequence by integer
print(flags)

print('-' * 60)

# True False









