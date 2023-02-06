# Function for describing a city
def describe_city(city_name, country='England'):
    """Print out basic info on a city, including name and country"""
    print(f"The city of {city_name} is in {country}.")

# Call the function 3 times
describe_city('Caracas', 'Venezuela')
describe_city('Coventry')
describe_city('Wichita', 'the USA')