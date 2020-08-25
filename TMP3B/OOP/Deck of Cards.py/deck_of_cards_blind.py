class Card:
    pass
    # each instance of card should have a suit # noqa
    # each instance of card should have a value  # noqa
    # cards repr method should display the card's value and suit # noqa


class Deck:
    pass
    # each instance of deck should have cards attributed with all 52 possible instances of card # noqa
    # deck should have instance method called count which returns a count of how many cards remain in deck # noqa
    # deck's repr method should display information on how many cards are in the deck # noqa
    # deck should have instance method called _deal which accepts a number and removes at most that many cards from the deck # noqa
    # deck should have an instance method called shuffle
    # deck should have an instance method called deal_card
    # deck should have an instance method called deal_hand


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
