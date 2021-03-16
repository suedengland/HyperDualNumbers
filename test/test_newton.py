import unittest

# Import the module to be tested
from hyperdualnumber import find_min_newton

class Test_Newton(unittest.TestCase):
    """Unit tests for the function 'find_min_newton'.

    Usage from root directory of this package:
      python -m unittest test.test_newton -v
      python -m unittest discover -v

    Omit the '-v' flag, if you do not want verbose output.

    Any function starting with 'test_' will be considered as a test case.
    """

    def test_rosenbrock_2d(self):
        x0 = [-3.0, 4.0]

        f = ''
        for l in range(len(x0)-1):
            f += f' + 100*(x[{l+1}] - x[{l}]**2)**2 + (1 - x[{l}])**2'

        xmin, flag, _, tp = find_min_newton(f, x0)

        self.assertTrue(flag)  # Check convergence
        # Check for minimum at [1.0, 1.0]
        self.assertEqual(tp, 'minimum')
        [self.assertAlmostEqual(xmin.tolist()[i], 1.0, delta=1e-10) for i in range(len(xmin))]


    def test_rosenbrock_3d(self):
        x0 = [-3.0, 4.0, 5.0]

        f = ''
        for l in range(len(x0)-1):
            f += f' + 100*(x[{l+1}] - x[{l}]**2)**2 + (1 - x[{l}])**2'

        xmin, flag, _, tp = find_min_newton(f, x0)

        self.assertTrue(flag)  # Check convergence
        # Check for minimum at [1.0, 1.0, 1.0]
        self.assertEqual(tp, 'minimum')
        [self.assertAlmostEqual(xmin.tolist()[i], 1.0, delta=1e-10) for i in range(len(xmin))]


    def test_saddle_point_2d(self):
        x0 = [-3.0, 4.0]
        f = 'x[0]**2 - x[1]**2'
        xmin, flag, _, tp = find_min_newton(f, x0)

        self.assertTrue(flag)  # Check convergence
        # Check for saddle point at [0.0, 0.0]
        self.assertEqual(tp, 'saddle point')
        self.assertListEqual(xmin.tolist(), [0.0, 0.0])


if __name__ == '__main__':
    unittest.main()
