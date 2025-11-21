import unittest
from safe_division import safe_division

class TestSafeDivision(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(safe_division(10, 2), 5)
    def test_zero_divisor(self):
        self.assertIsNone(safe_division(10, 0))
    def test_negative(self):
        self.assertEqual(safe_division(-8, 2), -4)
    def test_both_negative(self):
        self.assertEqual(safe_division(-12, -3), 4)
    def test_float(self):
        self.assertAlmostEqual(safe_division(7, 4), 1.75)
    def test_zero_numerator(self):
        self.assertEqual(safe_division(0, 5), 0)
    def test_zero_zero(self):
        self.assertIsNone(safe_division(0, 0))

if __name__ == '__main__':
    unittest.main()