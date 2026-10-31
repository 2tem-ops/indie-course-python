countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()

res = [(country, city) for country, cities in countries.items() if city in cities]
print(f"INFO: {res[0][1]} is a city in {res[0][0]}" if res else f"ERROR: Country for {city} not found")