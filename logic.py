import cards
import user_input
import game_statistics

def is_valid_play(card, top_card):
    if card["color"] == top_card["color"]:
        return True
    elif card["value"] == top_card["value"]:
        return True
    elif card["color"] == cards.colors[-1]:  # Wild card
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

    if card["value"] == "+2":
        draw_cards = 2
        skip_turn = True

    elif card["value"] == "Skip":
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

            # Copy the Wild card to keep the original card unchanged
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


# US 07: Detect Winner
# Check if the player has no cards left
def check_winner(player_cards):
    if len(player_cards) == 0:
        return True
    else:
        return False
    
# Check if the player has the card and if it is valid
def player_turn(player_cards, card_to_play, top_card, player_name="Human"):
    if card_to_play not in player_cards: # Check if the card is in the player's hand
        print("Card is not in your hand!")
        return top_card, False
 # Check if the card can be played
    if not is_valid_play(card_to_play, top_card):
        print("Invalid play!")
        return top_card, False
 # Play the card and update the top card
    top_card = play_card(card_to_play, top_card)
# Remove the played card from the player's hand
    player_cards.remove(card_to_play)
    print("Cards left:", len(player_cards))

    # Check if the player has won
    if check_winner(player_cards):
        print(f"{player_name} wins!")
        game_statistics.update_statistics(player_name)
        return top_card, True

    print("Game continues")
    return top_card, False

