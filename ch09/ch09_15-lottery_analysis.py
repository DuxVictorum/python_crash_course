# Builds on 09-14
from random import choice

# Initialize list of numbers and letters
nums = list(range(0,10))
letters = ['a', 'b', 'c', 'd', 'e']

list_of_nums_letters = nums
for letter in letters:
    list_of_nums_letters.append(letter)

# Generate winning lottery sequence of 4 numbers or letters
def pull_ticket():
    winning_ticket = ""
    for i in range(4):
        selection = choice(list_of_nums_letters)
        winning_ticket += str(selection)
    return winning_ticket
    
# Select my ticket
my_ticket = pull_ticket()
print(f"My ticket is {my_ticket}.")

# How many pulls until my ticket wins?
num_pulls = 0
while True:
    pull = pull_ticket()
    num_pulls += 1
    if pull == my_ticket:
        print(f"It only took {num_pulls} times to draw your ticket! :-)")
        break