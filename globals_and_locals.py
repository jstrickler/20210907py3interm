
x = 5
y = 10

def spam():
    m = 88
    n = 99
    print(locals())
    return "fatty pork fantasy"


g = globals()
print(g, '\n')

print(x, g['x'])

g['animal'] = 'wombat'

print(animal)

g['laugh'] = lambda : print("HA HA HA")

laugh()

spam()

name = "Liam"

print(dir(name))




