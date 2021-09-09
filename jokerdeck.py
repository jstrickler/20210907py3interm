from carddeck import CardDeck, Card

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        for joker_number in "1", "2":
            joker = Card(joker_number, "JOKER")
            self._cards.append(joker)
