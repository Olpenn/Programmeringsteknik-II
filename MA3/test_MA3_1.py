# https://docs.python.org/3/library/unittest.html
import unittest

from MA3 import *


class Test(unittest.TestCase):

    def test_approximate_pi(self):
                # test if the approximated pi is within the interval [2.78, 3.5]
        pi_a = approximate_pi(1000)
        self.assertLess(3.02, pi_a)
        self.assertLess(pi_a, 3.5)

        # test if the approximated pi is within the interval [3.10, 3.18]
        pi_a = approximate_pi(10000)
        print(pi_a)
        self.assertLess(3.10, pi_a)
        self.assertLess(pi_a, 3.18)

        # test if the approximated pi is within the interval [3.12, 3.16]
        pi_a = approximate_pi(100000)
        self.assertLess(3.12, pi_a)
        self.assertLess(pi_a, 3.16)

if __name__ == "__main__":
    unittest.main()
