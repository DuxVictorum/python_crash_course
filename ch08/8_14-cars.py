# Functions
def describe_car(make, model, **car_info):
    """Describes make, model, and other features of a car"""
    car_info['make'] = make
    car_info['model'] = model
    return car_info

def compare_car_age(car_a, car_b):
    """BONVS function -- Prints out which car is older"""
    if int(car_a['year']) < int(car_b['year']):
        print(f"The {car_a['year']} {car_a['make']} {car_a['model']} is older " 
        f"than the {car_b['year']} {car_b['make']} {car_b['model']}.")
    else:
        print(f"The {car_b['year']} {car_b['make']} {car_b['model']} is older " 
        f"than the {car_a['year']} {car_a['make']} {car_a['model']}.")

# Call the function three times
car1 = describe_car('Chevy', 'Caprice Classic', year='1979', color='silver')
car2 = describe_car('Honda', 'Accord', year='2017', color='sunset orange', 
        for_sale=True)
car3 = describe_car('Tyrulean', 'Jupiter 9000', year='2459', warp_speed='25', 
        passengers='16')
print(car1)
print(car2)
print(car3)

compare_car_age(car1, car2)
compare_car_age(car3, car2)


