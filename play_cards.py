from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Andy")
print(d1)

print(d1.dealer)

print(type(CardDeck.dealer))

print(d1.animal)

d1.dealer = "Alicia"

print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards, '\n')

for i in range(7):
    print(d1.draw())

print(d1.get_suits())
print(CardDeck.get_suits())

d2 = CardDeck("Andy")

print('-' * 60)

j1 = JokerDeck('Bonnie')
print(j1.dealer)
j1.shuffle()
print(j1.cards, '\n')

print(len(d1), len(j1))
# CardDeck.__len__(d1)
print(d1) # print(str(d1))
print(j1)
print(repr(d1))
print(repr(j1))

x = d1 + j1
print(x)
print(len(x))
print(x.dealer)

