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