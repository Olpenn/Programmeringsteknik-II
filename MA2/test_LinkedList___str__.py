
"""
Unittests for the binary search tree methods
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test___str__(self):
        print('\nTests __str__')
        llist = LinkedList()
        self.assertEqual(str(llist), '()')
        llist.insert(3)
        self.assertEqual(str(llist), '(3)')
        llist.insert(2)
        self.assertEqual(str(llist), '(2, 3)')
        llist.insert(4)
        self.assertEqual(str(llist), '(2, 3, 4)')


if __name__ == "__main__":
    unittest.main()
