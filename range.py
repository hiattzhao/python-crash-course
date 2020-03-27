numbers = []
for value in range(1,21):
#  print(value)
  numbers.append(value)

print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#list comprehension
odd_numbers = [value for value in range(1,21,2)]
print(odd_numbers)

#cubes
cubes = [value**3 for value in range(1,21)]
print(cubes)