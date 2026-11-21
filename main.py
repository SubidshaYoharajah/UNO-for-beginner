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
    game = deck.new_game()
    human_turn.human_turn(game)

if __name__ == "__main__":
    main()
    