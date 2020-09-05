from random import shuffle


class Card:
    # Each instance of Card  should have a suit # noqa
    # Each instance of Card  should have a value  # noqa
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Card 's __repr__  method should return the card's value and suit
    def __repr__(self):
        # return f"{self.value} of {self.suit}" # online test doesn't accept f-strings # noqa
        return "{} of {}".format(self.value, self.suit)


class Deck:
    # Each instance of Deck  should have a cards attribute with all 52 possible instances of Card . # noqa
    def __init__(self):
        self.cards = []
        for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
            for value in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):  # noqa
                self.cards.append(Card(suit, value))

    # Deck's __repr__ method should return information on how many cards are in the deck # noqa
    def __repr__(self):
        # return f"Deck of {self.count()} cards." # online test doesn't accept f-strings  # noqa
        return "Deck of {} cards".format(self.count())

    # Deck should have an instance method called _deal which accepts a number and removes at most that many cards from the end of the deck. If there are no cards left, this method should raise a ValueError with the message 'All cards have been dealth". # noqa
    def _deal(self, number):
        available_cards = self.count() if self.count() < number else number
        if self.count() > 0:
            cards = self.cards[-available_cards:]
            self.cards = self.cards[:-available_cards]
            return cards[0] if len(cards) == 1 else cards
        raise ValueError("All cards have been dealt")

    # Deck should have an instance method called count which returns a count of how many cards remain in the deck. # noqa
    def count(self):
        return len(self.cards)

    # Deck should have an instance method called shuffle  which will shuffle a full deck of cards. # noqa
    def shuffle(self):
        if self.count() == 52:
            shuffle(self.cards)
            return self
        raise ValueError("Only full decks can be shuffled")

    # Deck should have an instance method called deal_card which uses the _deal method to deal a single card from the deck and return that single card. # noqa

    def deal_card(self, number=1):
        return self._deal(number)

    # Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal # noqa
    def deal_hand(self, number):
        return self._deal(number)


# Tests
my_deck = Deck()
print(my_deck)  # Deck of 52 cards.

# my_deck.shuffle()
card = my_deck.deal_card()
print(card)  # King of Spades rather than A of Hearts

hand = my_deck.deal_hand(5)

print(hand)  # [8 of Spades, 9 of Spades, 10 of Spades, J of Spades, Q of Spades] rather than [8 of Spades, 10 of Clubs, 6 of Spades, 10 of Diamonds, Q of Spades] # noqa
print(my_deck)  # Deck of 46 cards.
