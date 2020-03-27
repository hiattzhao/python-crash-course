#remove same items in a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
  pets.remove('cat')
print(pets)

#moving items from one list to another
sandwich_orders = ['salami', 'ham', 'turkey']
finished_sandwiches = []

for sandwich in sandwich_orders:
  print('I made your ' + sandwich + ' sandwich')
  finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
  print(finished_sandwich + ' sandwich is made')

#remove all salami
sandwich_orders = ['salami', 'ham', 'salami', 'turkey', 'salami',]
finished_sandwiches = []
print('all salami sandwiches ran out')

while 'salami' in sandwich_orders:
  sandwich_orders.remove('salami')

for sandwich in sandwich_orders:
  finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
  print(finished_sandwich + ' sandwich is made')