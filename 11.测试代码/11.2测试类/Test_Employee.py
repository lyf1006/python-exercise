import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Jack", "Smiths", 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 55000)

    def test_give_custome_raise(self):
        self.employee.give_raise(6000)
        self.assertEqual(self.employee.salary, 56000)

unittest.main()