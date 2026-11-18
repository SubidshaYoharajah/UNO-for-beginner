import deck

def show_hand(game):
    for card in game["player_hand"]:
        print(card["name"])


def show_computer(game):
    count = len(game["computer_hand"])
    print(f"Computer has {count} cards") 



def show_top_card(game):
    top_card = game["discard_pile"][-1]
    print(f"Top card: {top_card['name']}")
    print (f"Active color: {top_card['color']}")

if __name__ == "__main__":
    game = deck.new_game()
    show_hand(game)
    show_computer(game)
    show_top_card(game) 

