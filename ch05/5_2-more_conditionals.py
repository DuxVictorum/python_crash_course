# More practice with conditionals

# Strings
son_name = "William"
print(son_name == "Frederitzi")
print(son_name == "William")

# Strings with .lower method
candy = "skittles"
print()
print(candy == "Skittles".lower())
print(candy == "Snickers".lower())

# Numerical tests
age = 45
print()
print(age == 42)
print(age > 25)
print(age < 25)
print(age >= 25)
print(age <= 45)

# Using and / or
age = 45
financial_health = True
can_retire = 55
print(age >= can_retire and financial_health)
print(age >= can_retire or financial_health)

# Whether an item is in or not in a list
games = ["Axis & Allies", "Monopoly", "Robin Hood", "Sushi Go"]
print("Robin Hood" in games)
print("Robotech" not in games)
print("Axis & Allies" not in games)
