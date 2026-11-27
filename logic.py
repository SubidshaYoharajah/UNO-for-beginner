
import cards
import user_input


# US-04: Check if a card can be played
def is_valid_play(card, top_card):

    # Check if the played card is a Wild card
    if card["value"] == "Wild":
        return True

    # Check if the top card is a Wild card
    if top_card["value"] == "Wild":
        return card["color"] == top_card["color"]

    # Check if the colors match
    if card["color"] == top_card["color"]:
        return True

    # Check if the numbers or symbols match
    elif card["value"] == top_card["value"]:
        return True

    else:
        return False


# US-04: Check if Skip card was played
def is_skip_card(card):
    return card["value"] == "Skip"


# US-04: Check if +2 card was played
def is_draw_two_card(card):
    return card["value"] == "+2"


# US-04: Check what happens when an Action card is played
def get_action_effect(card):
    draw_cards = 0
    skip_turn = False

    if is_draw_two_card(card):
        draw_cards = 2
        skip_turn = True

    elif is_skip_card(card):
        skip_turn = True

    return draw_cards, skip_turn


# US-04: Play a card
def play_card(card_top_play, top_card):

    # Check if the card is valid
    if is_valid_play(card_top_play, top_card):
        print(f"Playing card: {card_top_play['name']}")

        # Check if the card is a Wild card
        if card_top_play["color"] == cards.colors[-1]:
            print("Playing a wild card! You can choose any color.")
            chosen_color = user_input.choose_color()

            # Copy the Wild card
            played_card = card_top_play.copy()

            # Set the chosen color
            played_card["color"] = chosen_color
            return played_card

        # Return the played card
        return card_top_play

    else:
        # Keep the old top card if the play is invalid
        print("Invalid play!")
        return top_card


# US-07: Detect Winner
def check_winner(player_cards):
    if len(player_cards) == 0:
        return True
    else:
        return False
