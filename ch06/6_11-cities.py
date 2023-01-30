# Initialize dictionary of cities
cities = {
    'Wichita': {
        'country': 'the USA',
        'population': '647,610',
        'fact': 'Air Capital of the World'
    },
    'Innsbruck': {
        'country': 'Austria',
        'population': '132,493',
        'fact': 'host of the 1964 Winter Olympics'
    },
    'Darwin': {
        'country': 'Australia',
        'population': '147,255',
        'fact': 'wettest territorial capital in Australia'
    }
}

# Print out the information neatly formatted
for k, v in cities.items():
    print(f"Here's some information about the city of {k} in {v['country']}:")
    
    def verb():
        if k == 'Innsbruck':
            return "was"
        else:
            return "is"

    print(f"\tIt's population is {v['population']} and it {verb()} known as "
    f"the {v['fact']}.")