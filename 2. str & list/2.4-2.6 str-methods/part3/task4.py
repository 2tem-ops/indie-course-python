# Модель кодирования RGB

r, g, b = hex(int(input()))[2:].upper(), hex(int(input()))[2:].upper(), hex(int(input()))[2:].upper()

print(f"#{r.zfill(2)}{g.zfill(2)}{b.zfill(2)}")