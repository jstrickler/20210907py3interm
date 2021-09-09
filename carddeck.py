import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'



class CardDeck:   # object
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()


    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer): # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property
    def animal(self):
        return 'wombat'


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}: {self.dealer}, {len(self)}"

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f'{my_name}("{self.dealer}")'

# str(obj) -- human friendly info about obj
# repr(obj) -- how to create obj

    def __add__(self, other):
        my_type = type(self)
        new = my_type(self.dealer)
        new._cards = self.cards + other.cards
        return new




