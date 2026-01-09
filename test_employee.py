import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")

    # We can create stuff that will be used in several tests
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee('Daisuke', 'Sakuma', 50000)
        self.emp_2 = Employee('Gunwook', 'Park', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Daisuke.Sakuma@email.com')
        self.assertEqual(self.emp_2.email, 'Gunwook.Park@email.com')

        self.emp_1.last = "Sukuna"
        self.emp_2.first = "Matthew"

        self.assertEqual(self.emp_1.email, 'Daisuke.Sukuna@email.com')
        self.assertEqual(self.emp_2.email, 'Matthew.Park@email.com')


    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_2.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Park/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            
            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Sukuna/June')
            self.assertEqual(schedule, 'Bad Response!')




if __name__ == '__main__':
    unittest.main()