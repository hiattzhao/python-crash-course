#lower
car = 'Honda'
print(car.lower() == 'honda')

#comparisons
num1 = 34
num2 = 35
print(num1 == num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

#and & or
if num1 < num2 and car.lower() == 'honda':
  print('true')

if num1 < num2 or car == 'honda':
  print('one of them is false')

#in & not
pizzas = ['Hawaiian', 'Meat Lover', 'Pepperoni']
if 'Hawaiian' in pizzas:
  print('My favorite pizza is in the list')
if 'Sausage' not in pizzas:
  print('My favorite pizza is NOT in the list')