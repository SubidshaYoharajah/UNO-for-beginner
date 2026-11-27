
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


def main():
    welcome()
    choice = main_menu()

        # Exit the game
    if choice == "4":
        print("\nThank you for playing UNO.")
        print("Goodbye!")
        return

    print("Players:", player_name, "and", computer_name)

    game = deck.new_game()

    while True:
        # repeat the turns again until the game ends
        if game["current_player"] == "human":
            human_turn.human_turn(game)
            game["current_player"] = "computer"
        else:
            print("Computers turn(coming soon)")
            game["current_player"] = "human"


if __name__ == "__main__":
    main()

