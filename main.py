
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


# Player names
player_name = "Human"
computer_name = "Computer"


def main():
    welcome()
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

