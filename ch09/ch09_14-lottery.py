from random import choice

# Initialize list of numbers and letters
nums = list(range(1,11))
letters = ['a', 'b', 'c', 'd', 'e']

list_of_nums_letters = nums
for letter in letters:
    list_of_nums_letters.append(letter)

# Generate winning lottery sequence of 4 numbers or letters
winning_ticket = ""
for i in range(4):
    selection = choice(list_of_nums_letters)
    winning_ticket += str(selection)
    
    # --> Below is my first attempt, but I refactored to get the above
    # if isinstance(selection,int):
    #     winning_ticket += str(selection)
    # else:
    #     winning_ticket += selection

# Print out the winning ticket
print(f'And the winning ticket is: {winning_ticket}')