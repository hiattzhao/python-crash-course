#get values from keys
gf = {
  'first_name': 'Diem',
  'last_name': 'Dinh',
  'age': 34,
  'city': 'Philadelphia',
  }

print(gf['first_name'] + ' ' +
  gf['last_name'] +
  ' is ' +
  str(gf['age']) +
  ' years old.'
  )

rivers = {
  'nile': 'egypt',
  'mississippi': 'united states',
  'yellow': 'china',
  }

#print keys and values
for river, country in rivers.items():
  print('The ' + river.title() + ' is in ' + country.title())

#print keys
for river in rivers.keys():
  print('The name of the river is ' + river.title())

#print values
for country in rivers.values():
  print('The country is ' + country.title())

#dictionary and list
favorite_languages = {  
  'Hiatt': 'python',
  'Diem': 'javascript',
  'Tim': 'swift',
  'Bill': 'c',
}

friends = ['tim', 'bill', 'sandra']

for friend in friends:
  if friend.title() in favorite_languages.keys():
    print(friend.title() + "'s favorite language is " + favorite_languages[friend.title()].title())
  else:
    print(friend.title() + ', please take the poll')

myself = {
  'first_name': 'Hiatt',
  'last_name': 'Zhao',
  'age': 35,
  'city': 'Philadelphia',
  }

#dictionaries in list
people = [myself, gf]

for person in people:
  print('person is ' + person['first_name'] + ' ' + person['last_name'])

mickey = {
  'kind': 'guinea pig',
  'owner': 'hiatt',
}

custer = {
  'kind': 'guinea pig',
  'owner': 'hiatt',
}

crayfish = {
  'kind': 'crayfish',
  'owner': 'diem',
}

pets = [mickey, custer, crayfish]

for pet in pets:
  print(pet['kind'] + ' belongs to ' + pet['owner'].title())

favorite_places = {
  'hiatt': ['us', 'china', 'france'],
  'diem': ['vietnam', 'us'],
}

#lists in dictionary
for name, places in favorite_places.items():
  print(name + "'s favorite places are: ")
  for place in places:
    print('\t'+ place.title())

#dictionaries in dictionary
cities = {
  'beijing': {
    'country': 'china',
    'ethnicity': 'Chinese',
    'color': 'red',
  },
  'new york city': {
    'country': 'us',
    'ethnicity': 'American',
    'color': 'blue',
  },
  'paris': {
    'country': 'france',
    'ethnicity': 'French',
    'color': 'white',
  }
}

for city, facts in cities.items():
  print(city.title() + ' has the following facts:')
  print(facts['country'].title() + "'s capital is " + city.title() + ' and they speak ' + facts['ethnicity'])
  for key, value in facts.items():
    print('\t' + key.title() + ' is ' + value.title())
