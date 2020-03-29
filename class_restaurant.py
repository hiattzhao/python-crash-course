"""a class to represent a restaurant"""

class Restaurant():
  """A restaurant class"""
  def __init__(self, restaurant_name, cuisine_type):
    """initialize attributes"""
    self.name = restaurant_name
    self.type = cuisine_type
    self.number_served = 0

  """class methods"""
  def describe_restaurant(self):
    print(self.name + ' serves ' + self.type + ' cuisine')

  def open_restaurant(self):
    print(self.name + ' is open')

  def set_number_served(self, number):
    self.number_served = number

  def increment_number_served(self, inc_number):
    self.number_served += inc_number

