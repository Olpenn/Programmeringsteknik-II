"""
Unittest for LinkedList's length
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_length(self):
        print("\nTests LinkedList's length")
        lst = LinkedList()
        self.assertEqual(lst.length(), 0, msg="Cant't handle empty lists")
        lst.insert(3)
        self.assertEqual(lst.length(), 1)
        self.assertEqual(lst.length(), 1, msg='Destroys self')
        lst.insert(2)
        self.assertEqual(lst.length(), 2, msg='Destroys self')


if __name__ == "__main__":
    unittest.main()
