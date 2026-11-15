import cards
import logic

def main():
    top_card = cards.one_green
    print(f"Top card is: {top_card['name']}")
    
    # Example card to play
    card_to_play = {
        "name": "Switch Color",
        "color": cards.colors[-1],
        "value": 0
    }
    
    top_card = logic.play_card(card_to_play, top_card)

    card_to_play = {
            "name": "3 Red",
            "color": cards.colors[0],
            "value": 3
    }
    top_card = logic.play_card(card_to_play, top_card)  # Valid play

if __name__ == "__main__":
    main()