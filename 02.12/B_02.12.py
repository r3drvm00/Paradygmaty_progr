class Street:
    def __init__(self, name):
        self.name = name

city = {
    "3Maja": Street("3Maja"),
    "Sobieskiego": Street("Sobieskiego"),
    "Piastowska": Street("Piastowska"),
    "Warszawska": Street("Warszawska"),
    "Legionów": Street("Legionów"),
}

for street_name, street_object in city.items():
    print(f"{street_name}: {street_object.name}")
