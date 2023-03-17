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
    winning_ticket += choice(list_of_nums_letters)

print(winning_ticket)