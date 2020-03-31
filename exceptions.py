#try-except-else block
while True:
  num1 = input('Enter a number to add or "q" to quit: ')
  if num1 == 'q':
    break

  num2 = input('Enter another number to add or "q" to quit: ')
  if num2 == 'q':
    break

  try:
    answer = float(num1) + float(num2)
  except ValueError:
    print('Both inputs must be numbers!')
  else:
    print(answer)

#file not found error
try:
  with open('no_file.txt') as file_object:
    contents = file_object.read()
except FileNotFoundError:
  print('File not found')

#silent fail
try:
  with open('no_file.txt') as file_object:
    contents = file_object.read()
except FileNotFoundError:
  pass