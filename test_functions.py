import unittest
from test import cities

class CitiesTestCase(unittest.TestCase):
  """Test for cities function in test.py"""

  def test_cities(self):
    city = cities('santiago', 'chile')
    self.assertEqual(city, 'Santiago, Chile')

  def test_cities_population(self):
    city = cities('santiago', 'chile', population=1000000)
    self.assertEqual(city, 'Santiago, Chile - 1000000')

unittest.main()