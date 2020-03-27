#if else
alien_color = 'red'

if alien_color == 'red':
  print('player earned 5 points')
elif alien_color == 'green':
  print('player earned 4 points')
else:
  print('player earned 3 points')

#if elif
age = 35

if age < 2:
  stage = 'baby'
elif age >= 2 and age < 4:
  stage = 'toddler'
elif age >= 4 and age < 13:
  stage = 'kid'
elif age >= 13 and age < 20:
  stage = 'teenages'
elif age >= 20 and age < 65:
  stage = 'adult'
elif age >= 65:
  stage = 'elder'

print('person is ' + stage)

#conditionals in list
usernames = ['hiatt', 'zhao', 'diem', 'dinh', 'admin']
for username in usernames:
  if username == 'admin':
    print('Hello admin, would you like to see a status report?')
  else:
    print('Hello ' + username + ', would you like to login?')

#test for empty list
users = []
if users:
  print('users is not empty')
else:
  print('users is an empty list')

#check item from one list in another list
current_users = ['hiatt', 'ed', 'sameer', 'diem', 'admin']
new_users = ['hiatt', 'diem', 'john']

for new_user in new_users:
  if new_user in current_users:
    print(new_user + ' is already a current user')
  else:
    print(new_user + ' is available')

#another if elif else 
numbers = range(1, 10)
for number in numbers:
  if number == 1:
    print(str(number) + 'st')
  elif number == 2:
    print(str(number) + 'nd')
  elif number == 3:
    print(str(number) + 'rd')
  else:
    print(str(number) + 'th')