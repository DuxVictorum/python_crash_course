# Ask user for a number
num = input("Give me a number between 1 and 1,000  ")

# Use modulo operator to check whether the response is a multiple of 10
if int(num) % 10 == 0:
    print(f"Huzzah, {num} is indeed a multiple of 10.")
else:
    print(f"It turns out that {num} is not a multiple of 10.")