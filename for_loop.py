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