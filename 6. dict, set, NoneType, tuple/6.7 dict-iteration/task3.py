# Зеркальный словарь

data = {'apple': 5, 'banana': 3, 'cherry': 5, 'date': 2}

res = {}

for k, v in data.items(): res.setdefault(v, []).append(k)

print({k: sorted(v) for k, v in res.items()})
