import json

def save_game(main):
    with open("saved_game.json", "w") as file:
        json.dump(main, file, indent=4)

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

