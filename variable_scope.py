
x = 100  # global var

value = 42

# def print(*_):
#     pass

if value > 10:
    name = "Bob"   # global


print(x, name)

def spam():
    m = "Monkey King"  # local (function)
    return m

y = spam()

print(y)



#  local -> nonlocal -> global -> builtin


def foo(color):

    def bar(n):
        print(color * n)

    return bar

r = foo('red')
r(5)
r(20)

b = foo('blue')
b(10)


animal = 'wombat'

def toast():
    animal = 'platypus'  # creates LOCAL variable

toast()

print(animal)







