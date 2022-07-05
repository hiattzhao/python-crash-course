#Lists and strings are different in an important way. A list value is a mutable data type: it can have values added, removed, or changed. However, a string is immutable: it cannot be changed.

guests = ['Hiatt', 'Diem', 'Mom', 'Dad']
print(guests)

#index
guests[1]

#slices
guests[1:3]

#remove a guest
guests.remove('Hiatt')
print(guests)

#insert a guest
guests.insert(0, 'Hiatt2')
print(guests)

#add a guest at the end
guests.append('Lucas')
print(guests)

#remove a guest using remove()
#If the value appears multiple times in the list, only the first instance of the value will be removed.
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam #['cat', 'rat', 'elephant']

#remove a guest using pop
last_guest = guests.pop(-1)
print(guests)
print(last_guest)

#modify a guest
guests[2] = 'Mom2'
print(guests)

#delete a guest
del guests[2]
print(guests)

#The del statement is good to use when you know the index of the value you want to remove from the list. The remove() method is useful when you know the value you want to remove from the list.

locations = ['Japan', 'Hawaii', 'Thailand', 'Italy', 'Surprise Me!']
print(locations)

#temporary sorted list
print(sorted(locations))
print(locations)

print(sorted(locations, reverse=True))
print(locations)

#reverse list
locations.reverse()
print(locations)

#permenantly sort list, uppercase letters come before lowercase letters
locations.sort()
print(locations)

#If you need to sort the values in regular alphabetical order, pass str.lower for the key keyword argument in the sort() method call.
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam #['a', 'A', 'z', 'Z']

locations.sort(reverse=True)
print(locations)

#You cannot sort lists that have both number values and string values in them

#length of list
print(len(locations))

spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1] #elephant
spam[-3] #bat
spam[0:-1] #cat, bat, rat
spam[:2] #cat, bat
spam[1:] #bat, rat, elephant
spam[:] #cat, bat, rat, elephant

#list concatenation and replication
[1, 2, 3] + ['A', 'B', 'C'] #[1, 2, 3, 'A', 'B', 'C']
['X', 'Y', 'Z'] * 3 #['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + 
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  #list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

#in and not in operators
'howdy' in ['hello', 'hi', 'howdy', 'heyas'] #True

spam = ['hello', 'hi', 'howdy', 'heyas']
'howdy' not in spam #False

#multiple assigment trick (tuple unpacking)
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat #The number of variables and the length of the list must be exactly equal

#random.choice() and random.shuffle() Functions with Lists
import random
pets = ['Dog', 'Cat', 'Moose']
random.choice(pets) #'Dog'
#You can consider random.choice(someList) to be a shorter form of someList[random.randint(0, len(someList) – 1].

import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
people #['Carol', 'David', 'Alice', 'Bob']

#Finding a Value in a List with the index() Method
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') #0

#can use id() to get the reference
id('Howdy')
id(guests) #lists are mutable, has the same id after appending, etc. We call this “modifying the object "in-place.”

#copy module's copy() and deepcopy()
import copy
spam = ['A', 'B', 'C', 'D']
id(spam) #44684232

cheese = copy.copy(spam)
id(cheese) # cheese is a different list with different identity: 44685832

cheese[1] = 42
spam #['A', 'B', 'C', 'D']
cheese #['A', 42, 'C', 'D']