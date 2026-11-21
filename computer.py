import random
import logic
import cards

def choose_computer_color(computer_hand):
    hand_colors = []
    for card in computer_hand:
        hand_colors.append(card["color"])

    best_color = "red"
    for color in cards.colors[:4]:
        if hand_colors.count(color) > hand_colors.count(best_color):
            best_color = color
    
    return best_color


def computer_turn(game):
    if game.get("Winner") or game ["current_player"] != "computer":
        return

    computer_hand = game["computer_hand"]
    top_card = game["discard_pile"][-1]

    playable_cards = []

    for card in computer_hand:
        if logic.is_valid_play(card, top_card):
            playable_cards.append(card)

