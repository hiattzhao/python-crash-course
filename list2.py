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

#reverse back to original list
locations.reverse()
print(locations)

#permenantly sort list
locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

#length of list
print(len(locations))

#slice
print("the first three locations are: " + str(locations[:3]))
print("the middle three locations are: " + str(locations[1:4]))
print("the last three locations are: " + str(locations[-3:]))