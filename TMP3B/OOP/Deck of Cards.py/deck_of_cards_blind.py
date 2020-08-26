from random import shuffle


class Card:
    # Each instance of Card  should have a suit # noqa
    # Each instance of Card  should have a value  # noqa
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Card 's __repr__  method should return the card's value and suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    # Each instance of Deck  should have a cards attribute with all 52 possible instances of Card . # noqa
    def __init__(self):
        self.cards = []
        for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
            for value in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):  # noqa
                self.cards.append(Card(suit, value))

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    # Deck  should have an instance method called count  which returns a count of how many cards remain in the deck. # noqa
    def count(self):
        return len(self.cards)

    # Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck # noqa
    def deal(self, number):
        if self.card:
            pass
        else:
            return ValueError('All cards have been dealt.')

    # Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. # noqa
        if self.card:
            self.cards = shuffle(self.cards)
            return self.cards
        else:
            return ValueError('Only full decks can be shuffled"')

    # Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal # noqa


# Tests
# my_deck = Deck()
# print(my_deck)  # Deck of 52 cards.

# my_deck.shuffle()
# card = my_deck.deal_card()
# print(card)  # A of Hearts

# hand = my_deck.deal_hand(5)
# # [8 of Spades, 10 of Clubs, 6 of Spades, 10 of Diamonds, Q of Spades]
# print(hand)
# print(my_deck)  # Deck of 46 cards.
