from class_restaurant import Restaurant

"""an ice cream stand class that's a child class of a restaurant class"""
class IceCreamStand(Restaurant):
  def __init__(self, restaurant_name, cuisine_type):

    """Initialize attributes of the parent class"""
    super().__init__(restaurant_name, cuisine_type)

    """Add new attriute"""
    self.flavors = ['vanilla', 'chocolate', 'strawberry']

    """Add instance as an attribute"""
    self.color = Color()

  """Add new method"""
  def display_flavors(self):
    for flavor in self.flavors:
      print(flavor)

#inheritance
class Color():
  def __init__(self):
    self.colors = ['red', 'white', 'blue']
  
  def show_colors(self):
    for color in self.colors:
      print(color)

