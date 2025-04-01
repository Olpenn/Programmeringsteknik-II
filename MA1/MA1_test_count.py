# https://docs.python.org/3/library/unittest.html
import unittest

from MA1_solutions import *


class Test(unittest.TestCase):

    def test_count(self):
        ''' Reasonable tests
        1. search empty lists
        2. count first, last and interior elements
        3. search for a list
        4. check that sublists on several levels are searched
        5. search non existing elements
        6. check that the list searched is not destroyed
        '''
        print('\nTests count')
        self.assertEqual(count(1, []), 0)
        lst = [1, 'a', [[1, [1, 4]]], 7, 1, [1, 4], 1]
        self.assertEqual(count('a', lst), 1)
        self.assertEqual(count(1, lst), 6)
        self.assertEqual(count(4, lst), 2)
        self.assertEqual(count([1, 4], lst), 2)
        self.assertEqual(count('x', lst), 0)
        self.assertEqual(lst, [1, 'a', [[1, [1, 4]]], 7, 1, [1, 4], 1],
                         msg='count destroys the list')


if __name__ == "__main__":
    unittest.main()
