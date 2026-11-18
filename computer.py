import random
import logic
import cards
import deck

def choose_computer_color(computer_hand):
    hand_colors = []
    for card in computer_hand:
        hand_colors.append(card["color"])

    best_color = "red"
    for color in cards.color[:4]:
        if hand_colors.count(color) > hand_colors.count(best_color):
            best_color = color
    
    return best_color




