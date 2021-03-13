import unittest

# Import the class to be tested
from hyperdualnumber import HyperDualNumber as hdn
from hyperdualnumber import hdlog, hdexp

class Test_HyperDualNumber(unittest.TestCase):
    """Unit tests for the class 'HyperDualNumber'.

    Usage from root directory of this package:
      python -m unittest test.test_hyperdualnumber -v
      python -m unittest discover -v

    Omit the '-v' flag, if you do not want verbose output.

    Any function starting with 'test_' will be considered as a test case.
    """

    # Initiate x as HyperDualNumber
    x = hdn(5.0, eps1=1, eps2=1)


    # Addition
    def test_add_hdn_and_float(self):
        a = self.x + 3
        self.assertEqual(a.real, 8.0)

    def test_add_hdn_and_hdn(self):
        a = self.x + self.x
        self.assertEqual(a.real, 10.0)

    def test_add_float_and_hdn(self):
        a = 3 + self.x
        self.assertEqual(a.real, 8.0)


    # Subtraction
    def test_sub_hdn_and_float(self):
        a = self.x - 3
        self.assertEqual(a.real, 2.0)

    def test_sub_hdn_and_hdn(self):
        a = self.x - self.x
        self.assertEqual(a.real, 0.0)

    def test_sub_float_and_hdn(self):
        a = 3 - self.x
        self.assertEqual(a.real, -2.0)


    # Multiplication
    def test_mul_hdn_and_float(self):
        a = self.x*3
        self.assertEqual(a.real, 15.0)
        self.assertEqual(a.eps1, 3.0)
        self.assertEqual(a.eps2, 3.0)

    def test_mul_hdn_and_hdn(self):
        a = self.x*self.x
        self.assertEqual(a.real, 25.0)
        self.assertEqual(a.eps1, 10.0)
        self.assertEqual(a.eps2, 10.0)
        self.assertEqual(a.eps1eps2, 2.0)

    def test_mul_float_and_hdn(self):
        a = 3*self.x
        self.assertEqual(a.real, 15.0)
        self.assertEqual(a.eps1, 3.0)
        self.assertEqual(a.eps2, 3.0)
        self.assertEqual(a.eps1eps2, 0.0)


    # Power
    def test_pow_hdn_and_float(self):
        a = self.x**3
        self.assertEqual(a.real, 125.0)
        self.assertEqual(a.eps1, 75.0)
        self.assertEqual(a.eps2, 75.0)
        self.assertEqual(a.eps1eps2, 30.0)


    # Comparisons
    # ==
    def test_eq_hdn_and_hdn(self):
        a = hdn(5, eps1=1, eps2=1)
        self.assertTrue(a == self.x)

    def test_eq_hdn_and_float(self):
        self.assertTrue(self.x == 5)

    def test_eq_float_and__hdn(self):
        self.assertTrue(5 == self.x)

    # !=
    def test_neq_hdn_and_hdn(self):
        a = hdn(6, eps1=1, eps2=1)
        self.assertTrue(a != self.x)

    def test_neq_hdn_and_float(self):
        self.assertTrue(self.x != 7)

    def test_neq_float_and_hdn(self):
        self.assertTrue(7 != self.x)

    # <
    def test_lt_hdn_and_hdn(self):
        a = hdn(6, eps1=1, eps2=1)
        self.assertTrue(self.x < a)

    def test_lt_hdn_and_float(self):
        self.assertTrue(self.x < 10)

    def test_lt_float_and_hdn(self):
        self.assertTrue(2 < self.x)

    # >
    def test_gt_hdn_and_hdn(self):
        a = hdn(6, eps1=1, eps2=1)
        self.assertTrue(a > self.x)

    def test_gt_hdn_and_float(self):
        self.assertTrue(self.x > 2)

    def test_gt_float_and_hdn(self):
        self.assertTrue(7 > self.x)

    # <=
    def test_le_hdn_and_hdn(self):
        a = hdn(6, eps1=1, eps2=1)
        b = hdn(5, eps1=1, eps2=1)
        self.assertTrue(self.x <= a)
        self.assertTrue(self.x <= b)

    def test_le_hdn_and_float(self):
        self.assertTrue(self.x <= 6)
        self.assertTrue(self.x <= 5)

    def test_le_float_and_hdn(self):
        self.assertTrue(4 <= self.x)
        self.assertTrue(5 <= self.x)

    # >=
    def test_ge_hdn_and_hdn(self):
        a = hdn(3, eps1=1, eps2=1)
        b = hdn(5, eps1=1, eps2=1)
        self.assertTrue(self.x >= a)
        self.assertTrue(self.x >= b)

    def test_ge_hdn_and_float(self):
        self.assertTrue(self.x >= -3)
        self.assertTrue(self.x >= 5)

    def test_ge_float_and_hdn(self):
        self.assertTrue(200 >= self.x)
        self.assertTrue(5 >= self.x)


    # Logarithm
    def test_hdlog(self):
        import math

        # Initiate y as HyperDualNumber
        y = hdn(math.exp(1), eps1=1, eps2=1)

        a = hdlog(y)
        self.assertEqual(a.real, 1.0)
        self.assertEqual(a.eps1, 1/math.exp(1))
        self.assertEqual(a.eps2, 1/math.exp(1))
        self.assertEqual(a.eps1eps2, -1.0/math.exp(1)**2)


    # Exponential function
    def test_hdexp(self):
        import math
        a = hdexp(self.x)
        self.assertEqual(a.real, math.exp(5))
        self.assertEqual(a.eps1, math.exp(5))
        self.assertEqual(a.eps2, math.exp(5))
        self.assertEqual(a.eps1eps2, math.exp(5))


if __name__ == '__main__':
    unittest.main()
