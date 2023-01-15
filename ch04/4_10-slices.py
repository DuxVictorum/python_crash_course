# Initilize list of odd numbers up to 20
odd_nums = list(range(1,21,2))

# Fun with slices!
print(f"The first three numbers are: ",end='')
for num in odd_nums[:3]:
  print(f'{num}',end=' ')

print(f"\nThe middle three numbers are: ", end='')
for num in odd_nums[4:7]:
  print(f'{num}', end=' ')

print(f"\nThe last three numbers are: ", end='')
for num in odd_nums[-3:]:
  print(f'{num}', end=' ')