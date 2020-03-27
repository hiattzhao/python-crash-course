guests = ['Hiatt', 'Diem', 'Mom', 'Dad']
print(guests)

#remove a guest
guests.remove('Hiatt')
print(guests)

#insert a guest
guests.insert(0, 'Hiatt2')
print(guests)

#add a guest at the end
guests.append('Lucas')
print(guests)

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