# Define weights
weights = {
    "clean pick": 5,
    "good throw": 4,
    "catch": 6,
    "drop catch": -5,
    "stumping": 5,
    "run out": 7,
    "missed run out": -6,
    "direct hit": 8,
}

def get_data():
    data = []
    print("Enter fielding events for 3 players. Type 'done' to stop.")
    while True:
        match_no = input("Match No. (or 'done'): ")
        if match_no.lower() == 'done':
            break
        player = input("Player Name: ")
        pick = input("Pick (clean pick/good throw/fumble/bad throw/catch/drop catch): ").lower()
        throw = input("Throw (run out/missed stumping/missed run out/stumping/none): ").lower()
        runs = input("Runs saved (+) or conceded (-): ")

        # Store minimal info needed for analysis
        data.append({
            "Player": player,
            "Pick": pick,
            "Throw": throw,
            "Runs": int(runs),
            "Description": ""
        })
        print("---")

    return data

def calculate_performance(data):
    performance = {}

    for entry in data:
        p = entry["Player"]
        if p not in performance:
            performance[p] = {
                "clean pick": 0, "good throw": 0, "catch": 0, "drop catch": 0,
                "stumping": 0, "run out": 0, "missed run out": 0, "direct hit": 0,
                "runs": 0
            }
        performance[p][entry["Pick"]] = performance[p].get(entry["Pick"], 0) + 1 if entry["Pick"] in weights else performance[p].get(entry["Pick"], 0)
        performance[p][entry["Throw"]] = performance[p].get(entry["Throw"], 0) + 1 if entry["Throw"] in weights else performance[p].get(entry["Throw"], 0)
        performance[p]["runs"] += entry["Runs"]

    # Calculate score
    scores = {}
    for player, stats in performance.items():
        score = 0
        for key, count in stats.items():
            if key in weights:
                score += weights[key] * count
        score += stats["runs"]
        scores[player] = score

    return scores

def main():
    data = get_data()
    if not data:
        print("No data entered.")
        return

    scores = calculate_performance(data)

    print("\nPerformance Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

if __name__ == "__main__":
    main()
