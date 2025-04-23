# https://docs.python.org/3/library/unittest.html
import unittest

from HighOrderFunctionChecker import check_higher_order_functions
from MA3 import *


class Test(unittest.TestCase):

    def test_sphere_volume(self):

        # test if the sphere volume is within the interval [3.02, 3.25]
        n = 100000
        d = 2
        app_vol = sphere_volume(n, d)
        self.assertLess(3.02, app_vol)
        self.assertLess(app_vol, 3.25)
        act_vol = hypersphere_exact(d)
        self.assertAlmostEqual(act_vol, 3.141592653589793)

        # test if the sphere volume is within the interval [1.2, 2.6]
        d = 11
        app_vol = sphere_volume(n, 11)
        self.assertLess(1.2, app_vol)
        self.assertLess(app_vol, 2.6)
        #act_vol = hypersphere_exact(d)
        #self.assertAlmostEqual(act_vol, 1.8841038793898994)

        file_path = "MA3.py"  # Replace with your actual file path
        found_higher_order = check_higher_order_functions(file_path)
        self.assertEqual(found_higher_order, True)


if __name__ == "__main__":
    unittest.main()
