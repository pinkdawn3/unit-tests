# Naming conventions for tests -> test_ and whatever it comes next

import unittest
import calc 

class TestCalc(unittest.TestCase):

    # If the method doesn't start with test_ it won't run
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()