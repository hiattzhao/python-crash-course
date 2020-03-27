#single line prompt
message = input('Enter your name: ')
print('Hello ' + message)

#multi-line prompt
prompt = 'Some long greeting...'
prompt += '\nWhat is your name? '
name = input(prompt)
print('Your name is ' + name)

#int()
people = input('How many people are in your dinner party? ')
if int(people) > 8:
  print('please wait')
else:
  print('your table is ready')

#modulo operator
number = input('Enter a number: ')
if int(number) % 10 == 0:
  print(number + ' is a multiple of 10')
else:
  print(number + ' is not a multiple of 10')

#using conditional
toppings = ''
while toppings != 'q':
  toppings = input('Enter pizza toppings (to quit, enter "q"): ')
  if toppings != 'q':
    print(toppings)

#using a flag
active = True
while active:
  toppings = input('Enter pizza toppings (to quit, enter "q"): ')
  if toppings == 'q':
    active = False
  else:
    print(toppings)

#using break
age = input('Enter your age: ')
age = int(age)
while True:
  if age < 3:
    print('ticket is free')
  elif age >= 3 and age <= 12:
    print('ticket is $10')
  elif age > 12:
    print('ticket is $15')
  break

#using dictionary with input
poll_active = True
poll = {}
while poll_active:
  name = input('What is your name? ')
  location = input('Where do you want to go? ')
  poll[name] = location

  repeat = input('Ask another user (y/n)? ')
  if repeat.lower() == 'n':
    poll_active = False

print('\n-----Poll Results----')
for key, value in poll.items():
  print(key + ' would like to go to ' + value)