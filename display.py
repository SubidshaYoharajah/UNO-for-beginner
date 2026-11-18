import deck

def show_hand(game):
    for card in game["player_hand"]:
        print(card["name"])


if __name__ == "__main__":
    game = deck.new_game()
    show_hand(game)


