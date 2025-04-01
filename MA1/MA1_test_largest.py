# https://docs.python.org/3/library/unittest.html
import unittest

from MA1_solutions import *


class Test(unittest.TestCase):

    def test_largest(self):
        print('\nTests largest')
        lst = [5, 3, 7, 11, 4]
        self.assertEqual(largest(lst), 11)
        self.assertEqual(lst, [5, 3, 7, 11, 4],
                         msg='largest destroys the list')
        self.assertEqual(largest(lst[0:1]), 5)
        self.assertEqual(largest(lst[0:2]), 5)
        self.assertEqual(largest(lst[0:3]), 7)
        self.assertEqual(largest([-1,-5,-3,-2,-4]), -1)
        self.assertEqual(lst, [5, 3, 7, 11, 4],
                         msg='largest destroys the list')


if __name__ == "__main__":
    unittest.main()
