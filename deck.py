import cards
import random

deck = cards.all_cards[:]
random.shuffle(deck)
print(deck[0]["name"])
