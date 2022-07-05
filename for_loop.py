pizzas = ['Hawaiian', 'Meat Lover', 'Pepperoni']

for pizza in pizzas:
    print('I like ' + pizza + ' pizza')

print('I like pizzas')

#copy list
friend_pizzas = pizzas[:]

pizzas.append('cheese')
friend_pizzas.append('four cheese')

print(pizzas)
print(friend_pizzas)

#loops with lists
for i in range(4):
    print(i) #0, 1, 2, 3

#same as...
for i in [0, 1, 2, 3]:
    print(i)

#A common Python technique is to use range(len(someList)) with a for loop to iterate over the indexes of a list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#enumerate() function with lists - Instead of using the range(len(someList)) technique with a for loop to obtain the integer index of the items in the list, you can call the enumerate() function instead
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

