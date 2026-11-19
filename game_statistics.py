import json

# File to save the statistics
STATS_FILE = "statistics.json"

# Load the statistics
def load_statistics():
    try:
        with open(STATS_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {"Human": 0, "Computer": 0}


# Save the statistics
def save_statistics(stats):
    with open(STATS_FILE, "w") as file:
        json.dump(stats, file, indent=4)

# Add one win to the winner
def update_statistics(winner):
    # Load the current statistics
    stats = load_statistics()

    # Check if the winner is valid
    if winner == "Human" or winner == "Computer":
        # Add one win
        stats[winner] += 1

        # Save the upadated statistics
        save_statistics(stats)
