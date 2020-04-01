import unittest
from test import Employee

class EmployeeTestCase(unittest.TestCase):
  """Test for Employee class in test.py"""

  def setUp(self):
    """Create an instance"""
    self.my_employee = Employee('Hiatt', 'Zhao', 70000)

  def test_give_default_raise(self):
    self.my_employee.give_raise()
    self.assertEqual(75000, self.my_employee.salary)
  
  def test_give_custom_raise(self):
    self.my_employee.give_raise(7000)
    self.assertEqual(77000, self.my_employee.salary)

unittest.main()