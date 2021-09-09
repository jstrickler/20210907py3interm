
"""
struct person {
    char *first_name;
    char *last_name;
    int age;
}

"""

person = 'Bill', 'Gates', 'Microsoft', '1954-10-28'

print(len(person), person[0], 'Bill' in person, 'Larry' in person)

print(person[0], person[1])

first_name = person[0]
last_name = person[1]
# ...

first_name, last_name, product, dob = person   # iterable unpacking
print(first_name, last_name)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
    ('John', 'Strickler', '1956-10-31'),
]

for first_name, last_name, *product, dob in people:
    print(first_name, last_name)
print()

for first_name, last_name, *_ in people:
    print(first_name, last_name)
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()

e = enumerate(fruits)
print(e)
print(list(e), '\n')

values = ['a', 'b', 'c', 'd', 'e', 'f']

i, *j, k = values
print(i, j, k)

*i, j, k = values
print(i, j, k)

i, j, *k = values
print(i, j, k)

i, *j, k, l = values
print(i, j, k, l)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, name in airports.items():
    print(code, name)
print()

for _, last_name, *_, dob in people:
    print(last_name, dob)
print()

for *_, dob in people:
    print(dob)
print()

# awk '{ print $NF }'



