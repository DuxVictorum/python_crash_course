# Initialize list of numbers 1-9
first_nine = list(range(1,10))
print(first_nine)

# Loop through list and print out correct ordinal
for num in first_nine:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")