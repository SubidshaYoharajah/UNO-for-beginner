import json

def save_game():
    with open("save.json", "w") as file:
        json.dump(game, file, indent=4)

    print("Game saved successfully!")