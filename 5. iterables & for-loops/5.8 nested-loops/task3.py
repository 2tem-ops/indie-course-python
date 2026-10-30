# Схема рассадки в кинотеатре

booked = [(int(i[2]), int(i[-1])) if len(i) == 8 else (int(i[2]), int(i[7:])) for i in booked]

matrix = [["O" for j in range(10)] for i in range(5)]

for row, seat in booked:
    matrix[row - 1][seat - 1] = "X"

for row in matrix:
    print(" ".join(row))