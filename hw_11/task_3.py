import random
import csv

'''Write a program that will simulate user scores in a game.
Create a list with 5 players’ names after that simulate 100
rounds for each player. As a result of the game create a list
with the player's name and score (0-1000 range). And save it
to a CSV file.

The file should look like this:

Player name, Score
Josh, 56
Luke, 784
Kate, 90
Mark, 125
Mary, 877
Josh, 345
'''

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

results = []

for _ in range(100):
    for player in players:
        score = random.randint(0, 1000)
        results.append((player, score))

csv_file_name = 'game_scores.csv'
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Player name", "Score"])  # Запис заголовка
    csv_writer.writerows(results)  # Запис результатів

print(f"Results saved to '{csv_file_name}'")
