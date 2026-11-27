
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

            # Check if the human wins
            if logic.check_winner(game["player_hand"]):
                game["winner"] = "Human"
                game_statistics.update_statistics("Human")
                break

            # Default action effects
            draw_count = 0
            skip_turn = False

            # Get the effect of the played card
            if played_card is not None:
                draw_count, skip_turn = logic.get_action_effect(played_card)

            # Apply the draw effect
            for i in range(draw_count):
                deck.refill_deck(game)
                if len(game["deck"]) == 0:
                    break
                drawn_card = game["deck"].pop()
                game["computer_hand"].append(drawn_card)
                print("Computer draws a card")

            # Check if the computer skips its turn
            if skip_turn:
                print("Computer skips their turn")
            else:
                game["current_player"] = "computer"

        # Computer turn
        else:
            computer.computer_turn(game)

    # Show the winner
    print(game["winner"], "wins!")




def main():
    welcome()

    # Repeat the main menu
    while True:
        choice = main_menu()

        if choice == "1":
            start_game()

        elif choice == "2":
            print("Load game is not available yet.")

        elif choice == "3":
            game_statistics.show_statistics()

        elif choice == "4":
            print("\nThank you for playing UNO.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()



