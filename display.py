import deck

def show_hand(game):
    hand = game["player_hand"]
    print("Your cards:")
    for i in range(len(hand)):
        print(f"{i + 1}: {hand[i]['name']}")



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

