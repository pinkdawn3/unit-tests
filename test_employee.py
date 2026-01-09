import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):

        emp_1 = Employee('Daisuke', 'Sakuma', 50000)
        emp_2 = Employee('Gunwook', 'Park', 60000)

        self.assertEqual(emp_1.email, 'Daisuke.Sakuma@email.com')
        self.assertEqual(emp_2.email, 'Gunwook.Park@email.com')

        emp_1.last = "Sukuna"
        emp_2.first = "Matthew"

        self.assertEqual(emp_1.email, 'Daisuke.Sukuna@email.com')
        self.assertEqual(emp_2.email, 'Matthew.Park@email.com')


if __name__ == '__main__':
    unittest.main()