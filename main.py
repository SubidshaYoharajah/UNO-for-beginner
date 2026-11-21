import cards
import logic
import save_load
import computer
import user_input
import deck
import game_statistics
import display 
import human_turn 


# Start the game
print("Welcome to UNO!")

# Player names
player_name = "Human"
computer_name = "Computer"

print("Players:", player_name, "and", computer_name)

def main():
    top_card = cards.one_green
    print(f"Top card is: {top_card['name']}")
    
    # Example card to play
    card_to_play = {
        "name": "Wild",
        "color": cards.colors[-1],
        "value": cards.wild_value
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