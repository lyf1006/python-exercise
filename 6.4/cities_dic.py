cities = {
    'Paris': {
        'country': 'France',
        'population': '1100万',
        'fact': 'romance',
    },

    'beijing': {
        'country': 'China',
        'population': '2173万',
        'fact': 'history',
    },

    'London': {
        'country': 'England',
        'population': '828万',
        'fact': 'Big Ben',
    },
}

for city in cities.keys():
    print("\n")
    print(city)
    print(cities[city])