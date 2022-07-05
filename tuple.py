#The tuple data type is almost identical to the list data type, except in two ways. First, tuples are typed with parentheses, ( and ), instead of square brackets, [ and ]. But the main way that tuples are different from lists is that tuples, like strings, are immutable. Tuples cannot have their values modified, appended, or removed.

foods = ('orange', 'noodles', 'rice', 'chicken', 'fish')
for food in foods:
  print(food)

#convert to tuple from a list
tuple(['cat', 'dog', 5]) #('cat', 'dog', 5)

#convert to list from a tuple
list(('cat', 'dog', 5)) #['cat', 'dog', 5]

list('hello') #['h', 'e', 'l', 'l', 'o']