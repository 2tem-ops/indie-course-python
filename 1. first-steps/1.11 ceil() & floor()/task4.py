# Ремонт

from math import ceil

L, W, H = map(int, input().split())
P = (L + W) * 2
S = P * H

print(ceil(S / 16))

