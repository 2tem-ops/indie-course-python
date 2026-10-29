# Мишка и игра

# на кубике чисоа от 1 до 6
# игрок который выбросит наибольшее значение - победитель раунда
# значения равны - никому не засчитывается победа

# победитель игры - тот, кто выиграл в большем количестве раундов
# если победы равны - ничья

m_wins, c_wins = 0, 0

for _ in range(n:=int(input())):
    m, c = map(int, input().split())
    if m > c: m_wins += 1
    elif c > m: c_wins += 1

print("Mishka" if m_wins > c_wins else "Chris" if c_wins > m_wins else "Friendship is magic!^^")