# https://docs.python.org/3/library/unittest.html
"""
Unittest for to_list
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_to_list(self):
        print('\nTests LinkedList to_list method')
        lst = LinkedList()
        self.assertEqual(lst.to_list(), [])
        lst.insert(1)
        self.assertEqual(lst.to_list(), [1])
        self.assertEqual(lst.to_list(), [1], msg="Destroys self")
        for x in [1, 2, 6]:
            lst.insert(x)
        self.assertEqual(lst.to_list(), [1, 1, 2, 6])
        self.assertEqual(lst.to_list(), [1, 1, 2, 6], msg="Destroys self")


if __name__ == "__main__":
    unittest.main()
