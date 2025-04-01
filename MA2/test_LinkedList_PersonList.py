
"""
Unittests for the binary search tree methods
"""

import unittest

from bst import *
from linked_list import *



class Test(unittest.TestCase):

    def test_PersonList(self):
        print('\nTests PersonList')
        llist = LinkedList()
        llist.insert(Person('B', 2))
        llist.insert(Person('A', 1))
        self.assertEqual(str(llist), '(A:1, B:2)')
        llist.insert(Person('D', 4))
        self.assertEqual(str(llist), '(A:1, B:2, D:4)')
        llist.insert(Person('C', 3))
        self.assertEqual(str(llist), '(A:1, B:2, C:3, D:4)')


if __name__ == "__main__":
    unittest.main()
