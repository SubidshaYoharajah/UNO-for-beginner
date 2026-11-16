import json
import main

def save_game(main):
    with open("save.json", "w") as file:
        json.dump(main, file, indent=4)

    print("Game saved successfully!")

