import cards
import user_input

def is_valid_play(card, top_card):
    if card["color"] == top_card["color"]:
        return True
    elif card["value"] == top_card["value"]:
        return True
    elif card["color"] == cards.colors[-1]:  # Wild card
        return True
    else:
        return False

def play_card(card_top_play, top_card):
    if is_valid_play(card_top_play, top_card):
        print(f"Playing card: {card_top_play['name']}")
        if card_top_play["color"] == cards.colors[-1]:  # Wild card
            print("Playing a wild card! You can choose any color.")
            chosen_color = user_input.choose_color()
            card_top_play["color"] = chosen_color
        return card_top_play  # Return the played card to update the top card
    else:
        print("Invalid play!")
