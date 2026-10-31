# Сражение игроков

players = [("Alice", 10), ("Bob", 12), ("Charlie", 15)]
max_difference = 10

battles = []

for i in range(len(players) - 1):
    for j in range(i + 1, len(players)):
        name1, power1 = players[i]
        name2, power2 = players[j]

        if abs(power1 - power2) <= max_difference:
            battles.append((name1, power1, name2, power2))

if battles:
    for battle in battles:
        print(f"{battle[0]} vs {battle[2]}")