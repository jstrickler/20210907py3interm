from collections import namedtuple

Card = namedtuple('Card', 'rank suit')

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = 'Clubs Diamonds Hearts Spades'.split()

deck = []

for suit in SUITS:
    for rank in RANKS:
        card = Card(rank, suit)
        deck.append(card)

print(deck)

c = deck[0]
print(c)
print(c.rank, c.suit, c[0], c[1])
