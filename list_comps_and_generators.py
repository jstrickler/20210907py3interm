fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    if f.startswith('p'):
        f0.append(f.upper())
print("f0: {}\n".format(f0))

#    [EXPR for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [len(f) for f in fruits]
print("f3: {}\n".format(f3))

f4 = [(f, len(f)) for f in fruits]
print("f4: {}\n".format(f4))

f5 = [f for f in fruits if f.startswith('p') if len(f) > 5]
print("f5: {}\n".format(f5))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names: {}\n".format(last_names))

with open('DATA/mary.txt') as mary_in:
    lines = [line.rstrip() for line in mary_in]
print("lines: {}\n".format(lines))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [float(n) * 10 for n in nums]
print("n1: {}\n".format(n1))

n2 = [round(n ** .5, 2) for n in nums]
print("n2: {}\n".format(n2))

e = enumerate(fruits)
print("e: {}\n".format(e))
for i, fruit in e:
    print(i, fruit)
print()

fg1 = (f.upper() for f in fruits if f.startswith('p'))
print(fg1)
for fruit in fg1:
    print(fruit)
print()

fg_upper = (f.upper() for f in fruits)
fg_p = (f for f in fg_upper if f.startswith('P'))
print(fg_p)
for fruit in fg_p:
    print(fruit, end=' ')
print('\n')














