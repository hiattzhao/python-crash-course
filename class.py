from class_restaurant import Restaurant #importing a single class
#import class_restaurant <-- import an entire module
from class_ice_cream_stand import IceCreamStand, Color #import multiple classes
#from class_ice_cream_stand import * <-- not recommended, can't tell which classes are imported

my_restaurant = Restaurant('Dan Dan', 'Chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('Ma Ma Mia', 'Italian')
your_restaurant.describe_restaurant()
print(your_restaurant.name + ' has served ' + str(your_restaurant.number_served) + ' customers')
your_restaurant.set_number_served(5)
print(your_restaurant.name + ' has served ' + str(your_restaurant.number_served) + ' customers')
your_restaurant.increment_number_served(10)
print(your_restaurant.name + ' has served ' + str(your_restaurant.number_served) + ' customers')



my_stand = IceCreamStand("Rita's", 'Ice Cream')
my_stand.describe_restaurant()
my_stand.display_flavors()

my_stand.color.show_colors()
