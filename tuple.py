#tuples are immutable lists, cannot change the values in a tuple

foods = ('orange', 'noodles', 'rice', 'chicken', 'fish')
for food in foods:
  print(food)

#error
# foods[0] = 'apple'
# for food in foods:
#   print(food)

#reassigning a tuple
foods = ('apple', 'noodles', 'rice', 'chicken', 'fish')
for food in foods:
  print(food)