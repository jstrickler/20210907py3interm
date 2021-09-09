

def doit(a, b):
    print(a * b)


doit(5, 10)
doit('a', 5)
doit(0, 103093)

values = [8, 5]
doit(*values)
print()

data = [
    (5, 10),
    (8, 6),
    (9, 4),
    (13, 11),
]

for d in data:
    doit(*d)


def config(**options):
    print(options)

config(file_name="foo.txt", user="jack")

data = {
    'file_name': "wombats.txt",
    'user': 'croc_dundee',
}

config(**data)  # config(file_name='wombats.txt', user='croc_dundee')




