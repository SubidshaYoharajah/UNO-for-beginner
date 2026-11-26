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
    if game.get("winner") or game ["current_player"] != "computer":
        return

    computer_hand = game["computer_hand"]
    top_card = game["discard_pile"][-1]

    playable_cards = []

    for card in computer_hand:
        if logic.is_valid_play(card, top_card):
            playable_cards.append(card)

    if len(playable_cards) == 0:
        if len(game["deck"]) == 0:
            print("Draw pile is empty")
            game["current_player"] = "human"
            return None

        drawn_card = game["deck"].pop()
        computer_hand.append(drawn_card)

        print("Computer draws a card")

        if logic.is_valid_play(drawn_card, top_card):
            playable_cards.append(drawn_card)
        else:
            print("Computer cannot play")
            game["current_player"] = "human"
            return None

    chosen_card = random.choice(playable_cards)

    played_card = chosen_card.copy()

    if skip_turn:
        game["current_player"] = "computer"
        print("Human skips their turn")
    else:
        game["current_player"] = "human"

    return played_card




