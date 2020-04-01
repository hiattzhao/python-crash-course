def cities(city, country, population=''):
  """Return city, country"""
  if population:
    result = (city.title() + ', ' + country.title() + ' - ' + str(population))
  else:
    result = (city.title() + ', ' + country.title())
  return result

class Employee():
  """An Employee class"""
  def __init__(self, fname, lname, salary):
    """initialize attributes"""
    self.first_name = fname
    self.last_name = lname
    self.salary = salary

  def give_raise(self, amount=5000):
    self.salary += amount
