from pprint import pprint

AIRPORT_DATA = {
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

def main():
    airport_examples(AIRPORT_DATA)
    set_examples(set1, set2)
    frozenset_examples()


def airport_examples(airports):
    print(airports['RDU'], '\n')
    for code in 'RDU', 'IAD', 'ELM', 'LAX', 'EWR':
        print(code, airports.get(code, "NOT FOUND"))
    print()

    print(airports.get('XXX'), '\n')

    for code, name in airports.items():
        print(code, name)
    print()

    print(len(airports), '\n')

    for code, name in sorted(airports.items()):
        print(code, name)
    print()


    more_airports = {
        'MID': 'Midway',
        'BUR': 'Burbank',
        'RIC': 'Richmond',
        'MCI': 'Kansas City, MO',
    }

    airports.update(more_airports)
    pprint(airports)
    print('\n')



def set_examples(c1, c2):
    print(c1)
    print(c2, '\n')
    print(colors1)
    print(colors2, '\n')

    c1.add('chartreuse')
    c2.add('red')
    c2.add('red')
    c2.add('scarlet')
    print(c1)
    print(c2, '\n')

    print("Common:", c1 & c2)
    print("Not common:", c1 ^ c2)
    print("All:", c1 | c2)
    print("Just c1:", c1 - c2)
    print("Just c2:", c2 - c1)

def frozenset_examples():
    locations = frozenset(['US', 'Canada', 'Other'])

    for loc in 'Canada', 'US', 'USSR', 'Chile':
        print(loc, loc in locations)
    print()

def say_hello():
    print("Hello, Python world")


if __name__ == '__main__':  # if running as script...
    colors1 = 'red blue red red green purple red orange'.split()
    colors2 = 'pink orange green black white red red red red red red'.split()
    set1 = set(colors1)
    set2 = set(colors2)

    say_hello()
    main()

# else (if imported do nothing)









