# Functions
def city_country(city, country):
    """Returns city and country in formatted state"""
    return f"{city.title()}, {country.title()}"

# Call function
destination = city_country('Sao Paulo', 'Brazil')
print(f"I would love to visit {destination} some day.")