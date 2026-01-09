# Naming conventions for tests -> test_ and whatever it comes next

import unittest
import calc 

class TestCalc(unittest.TestCase):

    # If the method doesn't start with test_ it won't run
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

        # Let's test edge cases with negative numbers
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # param: result, function, parameters
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # or it can also be done as...
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


        


# Conditional so instead of running the python file, it runs through the unittest module
if __name__ == '__main__':
    unittest.main()