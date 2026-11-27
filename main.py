
import cards
import logic
import save_load
import computer
import user_input
import deck
import game_statistics
import display
import human_turn


# Welcome message
def welcome():
    print("================================")
    print("       WELCOME TO UNO!")
    print("================================")

# Main menu
def main_menu():
    print("\n1. Start new game")
    print("2. Load game")
    print("3. View statistics")
    print("4. Exit")

    choice = input("Your choice: ")
    return choice

# Player names
player_name = "Human"
computer_name = "Computer"




# Start a new game
def start_game():
    print("Players:", player_name, "and", computer_name)

    game = deck.new_game()

    while True:
        # Stop the game if a winner is detected
        if game.get("winner"):
            break

        # Human turn
        if game["current_player"] == "human":
            played_card = human_turn.human_turn(game)

            # Check if a Skip card was played
            if played_card is not None and logic.is_skip_card(played_card):
                print("Computer skips their turn")
            else:
                game["current_player"] = "computer"

        # Computer turn
        else:
            computer.computer_turn(game)


def main():
    welcome()
    choice = main_menu()

    if choice == "1":
        start_game()

    elif choice == "4":
        print("\nThank you for playing UNO.")
        print("Goodbye!")
        return

    else:
        print("Option not available yet.")


if __name__ == "__main__":
    main()


