# Декартово произведение

from itertools import product

colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']

print(list(product(colors, sizes)))

