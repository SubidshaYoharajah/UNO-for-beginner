import json

def save_game(game):
    with open("saved_game.json", "w") as file:
        json.dump(game, file, indent=4)

    print("Game saved successfully!")

def load_game():
    try:
        with open("saved_game.json", "r") as file:
            game = json.load(file)

        print("Game loaded successfully")
        return game
    
    except FileNotFoundError:
        print("No saved game found!")
        return None  

