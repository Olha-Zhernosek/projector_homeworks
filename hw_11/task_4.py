'''Write a script that reads the data from the previous
CSV file and creates a new file called high_scores.csv where
each row contains the player name and their highest score.
The final score should be sorted by descending to the highest
score.

The output CSV file should look like this:
Player name, Highest score
Kate, 907
Mary, 897
Luke, 784
Mark, 725
Josh, 345'''

import random
import csv

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

results = []

for _ in range(100):
    for player in players:
        score = random.randint(0, 1000)
        results.append((player, score))

csv_file_name = 'high_scores.csv'
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Player name", "Highest score"])

    highest_scores = {}
    for name, score in results:
        if name not in highest_scores or score > highest_scores[name]:
            highest_scores[name] = score

    for name, score in highest_scores.items():
        csv_writer.writerow([name, score])

print(f"High scores saved to '{csv_file_name}'")
