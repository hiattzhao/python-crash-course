#using the json module
import json

filename = 'file.json'

#refactor
def get_stored_favorite_number(filename):
  """Get the favorite number from the file"""
  with open(filename) as file_object:
    fav_number = json.load(file_object)
    return fav_number

def get_new_favorite_number(filename):
  """Get a new favorite number"""
  number = input('What is your favorite number? ')
  with open(filename, 'w') as file_object:
    json.dump(str(number), file_object)

def check_favorite_number():
  number = get_stored_favorite_number(filename)
  if number:
    match = input('Is ' + number + ' your favorite number? (y/n)')
    if match == 'y':
      print('Great! Your favorite number is ' + number)
    else:
      get_new_favorite_number(filename)
  else:
    get_new_favorite_number(filename)


try:
  check_favorite_number()
  favorite_number = get_stored_favorite_number(filename)
except FileNotFoundError:
  get_new_favorite_number(filename)
else:
  print('Your favorite number is: ' + favorite_number)