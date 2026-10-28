# Очередь на взлёт

clients = input().split()

while clients:
    print(f"Клиент {clients.pop()} пройдите к стойке!")
    if clients: print(f"{",".join(clients[::-1])} ожидайте!", sep="\n")