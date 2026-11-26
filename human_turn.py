import deck
import logic
import user_input
import display


def has_playable_card(hand, top_card):
    for card in hand:
        if logic.is_valid_play(card, top_card):
            return True
    return False


def draw_card(game):
    deck.refill_deck(game)
    card = game["deck"].pop()
    game["player_hand"].append(card)
    print(f"You drew: {card['name']}")
    return card


def play(game, card):
    top_card = game["discard_pile"][-1]
    played_card = logic.play_card(card, top_card)
    game["player_hand"].remove(card)
    game["discard_pile"].append(played_card)


def human_turn(game):
    hand = game["player_hand"]
    top_card = game["discard_pile"][-1]

    display.show_top_card(game)
    display.show_hand(game)

    if not has_playable_card(hand, top_card):
        print("You have no playable card. You draw one.")
        deck.refill_deck(game)
        if len(game["deck"]) == 0:
            print("There are no cards left. Your turn is over.")
            return
        
        card = draw_card(game)
        if logic.is_valid_play(card, top_card):
            print("The drawn card can be played. It is played now.")
            play(game, card)
        else:
            print("The drawn card cannot be played. Your turn is over.")
        return

    while True:
        number = user_input.input_int("Choose a card number: ", 1, len(hand))
        card = hand[number - 1]
        if logic.is_valid_play(card, top_card):
            play(game, card)
            return
        print("You cannot play this card. Choose another one.")


if __name__ == "__main__":
    game = deck.new_game()
    human_turn(game)
    print()
    display.show_top_card(game)
    display.show_hand(game)