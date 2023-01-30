# Initialize a dictionary of favorite numbers
fav_numbers = {
    'Sarah': [24, 3, 983],
    'Steve': [12, 637_892],
    'Shania': [8],
    'Sarbanian': [2, 73, 8],
    'Sally': [42, 3.14159, 2]
}

# Print out their favorite numbers!
for person, fav_nums in fav_numbers.items():
    print(f"{person} likes: ", end='')
    for num in fav_nums:
        if len(fav_nums) == 1:
            print(f"{num}")
        elif len(fav_nums) == 2:
            print(f"{fav_nums[0]} and {fav_nums[1]}")
            break
        elif num == fav_nums[-1]:
            print(f"and {num}")
        else:
            print(f"{num}, ", end='')