import cards
import random


def new_game():
    deck = cards.all_cards[:]
    random.shuffle(deck)

    player_hand = []
    computer_hand = []
    for i in range(7):
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())

    
    first_card = deck.pop()
    while first_card["value"] == "Wild":
        deck.insert(0, first_card)
        first_card = deck.pop()
    discard_pile = [first_card]


    current_player = "human"

    return {
        "deck": deck,
        "player_hand": player_hand,
        "computer_hand": computer_hand,
        "discard_pile": discard_pile,
        "current_player": current_player,
    }



def refill_deck(game):
    if len(game["deck"]) == 0:
        top_card = game["discard_pile"][-1]
        old_cards = game["discard_pile"][:-1]
        for card in old_cards:
            if card["value"] == "Wild":
                card["color"] = "black"
        random.shuffle(old_cards)
        game["deck"] = old_cards
        game["discard_pile"] = [top_card]
        print("The deck was empty. The old cards were shuffled into a new deck.")

if __name__ == "__main__":
    game = new_game()
    print(len(game["player_hand"]))
    print(len(game["computer_hand"])) 
    print(len(game["deck"]))
    print(len(game["discard_pile"]))
    print(game["current_player"])