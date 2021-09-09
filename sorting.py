
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0: {}\n".format(f0))

def to_lower(f):
    return f.lower()

#  str.lower(f)

f1 = sorted(fruits, key=str.lower)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=len)
print("f2: {}\n".format(f2))

def custom_sort(f):
    return len(f), f.lower()

f3 = sorted(fruits, key=custom_sort)
print("f3: {}\n".format(f3))






