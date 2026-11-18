import cards
import random

deck = cards.all_cards[:]
random.shuffle(deck)
print(deck[0]["name"])

player_hand = []
computer_hand = []
for i in range(7):
    player_hand.append(deck.pop())
    computer_hand.append(deck.pop())


discard_pile =  [deck.pop()]
current_player = "human"


print(len(player_hand))
print(len(computer_hand))
print(len(deck))


print(len(discard_pile))
print(current_player)