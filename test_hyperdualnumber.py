import unittest

# Import the class to be tested
from HyperDualNumber import HyperDualNumber as hdn

class Test_HyperDualNumber(unittest.TestCase):
    """Unit tests for the class 'HyperDualNumber'.

    Usage: python -m unittest -v this_file.py

    Any function starting with 'test_' will be considered as a test case.
    """

    # Initiate x as HyperDualNumber
    x = hdn(5.0, eps1=1, eps2=1)

    def test_add_hdn_and_float(self):
        a = self.x + 3
        self.assertEqual(a.real, 8.0)

    def test_add_hdn_and_hdn(self):
        a = self.x + self.x
        self.assertEqual(a.real, 10.0)

    def test_add_float_and_hdn(self):
        a = 3 + self.x
        self.assertEqual(a.real, 8.0)

    def test_sub_hdn_and_float(self):
        a = self.x - 3
        self.assertEqual(a.real, 2.0)

    def test_sub_hdn_and_hdn(self):
        a = self.x - self.x
        self.assertEqual(a.real, 0.0)

    def test_sub_float_and_hdn(self):
        a = 3 - self.x
        self.assertEqual(a.real, -2.0)

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

    def test_pow_hdn_and_float(self):
        a = self.x**3
        self.assertEqual(a.real, 125.0)
        self.assertEqual(a.eps1, 75.0)
        self.assertEqual(a.eps2, 75.0)
        self.assertEqual(a.eps1eps2, 30.0)


if __name__ == '__main__':
    unittest.main()
