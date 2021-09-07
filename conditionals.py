
value = 56

if value > 75:
    print("kangaroo")
    print("kookaburra")
elif value > 50:
    print("wombat")
elif value > 25:
    print("koala")
    print("platypus")
else:
    print("wallaby")

DEBUG = True

#  color = DEBUG?'red':'green'
color = 'red' if DEBUG else 'green'


while True:
    user = input("User name? ")
    if user == 'q':
        break
    if user == '':
        print("Please enter a name")
        continue

    print(f"User {user} added")

i = 0
while i < 3:
    print(i)
    i += 1
print()

for i in range(3):
    print(i)
print()

for fruit in 'mango', 'peach', 'apricot', 'plum', 'persimmon':
    print(fruit.upper())
print()

actor = "Joe Pesci"
for letter in actor:
    print(letter.lower())
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

target = 'x'
for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print(target, "not found")









