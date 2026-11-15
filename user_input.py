import cards

def input_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def choose_color():
    print("Choose a color:")
    for i, color in enumerate(cards.colors[:-1]):  # Exclude black (wild)
        print(f"{i + 1}. {color.capitalize()}")
    
    choice = input_int("Your choice: ", 1, len(cards.colors) - 1) - 1
    if 0 <= choice < len(cards.colors) - 1:
        return cards.colors[choice]
    else:
        print("Invalid choice. Defaulting to red.")