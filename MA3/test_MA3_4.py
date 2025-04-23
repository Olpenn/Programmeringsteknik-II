# https://docs.python.org/3/library/unittest.html
import unittest
from MA3 import *


class Test(unittest.TestCase):

    def test_sphere_volume_parallel2(self):
        n = 1000000
        d = 11
        np = 2
        start = pc()
        sphere_volume(n, d)
        stop = pc()
        seq = stop - start

        start = pc()
        app_vol = sphere_volume_parallel2(n, d, np)
        print(app_vol)
        stop = pc()
        par = stop - start

        self.assertLess(1.6, app_vol)
        self.assertLess(app_vol, 2.2)
        self.assertLess(par, seq)

if __name__ == "__main__":
    unittest.main()
