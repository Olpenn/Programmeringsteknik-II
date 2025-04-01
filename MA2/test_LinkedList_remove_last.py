# https://docs.python.org/3/library/unittest.html
"""
Unittests for the linked lists methods 

"""

import unittest

from bst import *
from linked_list import *



class Test(unittest.TestCase):

    def test_remove_last(self):
        print('\nTests LinkedList.remove_last')
        lst = LinkedList()
        for x in [3, 1, 2, 6]:
            lst.insert(x)

        self.assertEqual(lst.remove_last(), 6)
        self.assertEqual(lst.remove_last(), 3)
        self.assertEqual(lst.remove_last(), 2)
        self.assertEqual(lst.remove_last(), 1)
        self.assertEqual(lst.first, None)
        with self.assertRaises(ValueError):
            lst.remove_last()


if __name__ == "__main__":
    unittest.main()
