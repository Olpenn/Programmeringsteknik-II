# https://docs.python.org/3/library/unittest.html
import unittest

from MA1_solutions import *


class Test(unittest.TestCase):

    def test_harmonic(self):
        print('\nTests harmonic')
        self.assertAlmostEqual(harmonic(1), 1.)
        self.assertAlmostEqual(harmonic(2), 1.5)
        self.assertAlmostEqual(harmonic(3), 1.5 + 1/3)
        self.assertAlmostEqual(harmonic(4), 1.5 + 1/3 + 1/4)


if __name__ == "__main__":
    unittest.main()
