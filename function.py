#"as" can be used as alias to prevent naming collision
import module as m #imports all functions
from module import favorite_book as fb #imports one function from the module

#from module import * <-- "*" imports all functions in a module

#using a module using alias
m.display_message()

#using a function inside a module
fb('The book of books')

#function without parameter
def display_message():
  """Display a message <- doctring"""
  print("I'm learning Python")

display_message()

#function with a parameter
def favorite_book(title):
  """Print my favorite book"""
  print('My favorite book is ' + title.title())

favorite_book('lord of the rings')

#positional arguments
def make_shirt(size, text):
  """Make a T shirt"""
  print('The shirt size is ' + str(size) + ' and the text is ' + text)

make_shirt(34, 'This is a shirt')

#keyword arguments
make_shirt(text='This is another shirt', size=37)

#dafault values
def make_another_shirt(size=35, text='I love python'):
  """Make another T shirt"""
  print('The shirt size is ' + str(size) + ' and the text is ' + text)

make_another_shirt()
make_another_shirt(24)
make_another_shirt(text='I love Java')

#returning from a function
def city_country(city, country):
  """Return a city and a country"""
  result = city.title() + ', ' + country.title()
  return result

location = city_country('beijing', 'china')
print(location)

#returning a dictionary
def make_album(artist_name, album_title, album_tracks=''):
  """Return an album in dictionary format"""
  album = {
    'artist': artist_name.title(),
    'album': album_title.title(),
    }

  if album_tracks:
    album['tracks'] = album_tracks

  return album

album = make_album('clash', 'sandinista', 10)
print(album)

#using function in a while loop with input
while True:
  print('***Press q to quit anytime***')
  
  artist = input('What is your favorite artist? ')
  if artist == 'q':
    break

  album = input('What is an album by that artist? ')
  if album == 'q':
    break

  result = make_album(artist, album)
  print(result)

#passing a list into a function
magicians = ['merlin', 'gandolf', 'david']

def show_magicians(magicians_list):
  """Return a list of magicians"""
  for magician in magicians_list:
    print(magician.title())

show_magicians(magicians)

great_magicians = []

def make_great(magicians_list, great_magicians_list):
  """Modify a list of great magicians"""
  while magicians_list:
    current_magician = magicians_list.pop()
    great_magicians_list.append(current_magician + ' the Great')

#calling a function using a copied list
make_great(magicians[:], great_magicians)

#show the new list and the original list
show_magicians(great_magicians)
show_magicians(magicians)
  
#arbitrary number of arguments
def make_sandwich(*items):
  for item in items:
    print(item)

make_sandwich('ham', 'cheese', 'bread')

#arbitrary number of key-value pair arguments
def build_profile(fname, lname, **info):
  profile = {}
  profile['first_name'] = fname
  profile['last_name'] = lname
  for key, value in info.items():
    profile[key] = value
  
  print(profile)

build_profile('hiatt', 'zhao', age=36, height=5.8)