# https://github.com/Diashroom/lab11-JP.git
# Partner 1: Jingjing
# Partner 2: Jingjing

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ########## PARTNER 2 TESTS ##########

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-4, -2), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-2, 10)

    ########## PARTNER 1 TESTS ##########

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 4), -4)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5)   # because div(a,b) = b/a
        self.assertAlmostEqual(div(3, 9), 3)
        self.assertAlmostEqual(div(4, 20), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)

        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()


