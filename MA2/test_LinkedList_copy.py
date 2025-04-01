"""
Unittests LinkedList's copy
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def equal(l1, l2):
        pass

    def test_copy(self):
        print("\nTest LinkedList's copy")
        lst = LinkedList()
        cpy = lst.copy()
        self.assertEqual(
            cpy.first, None, msg='\n*** Copy of empty list is not working')
        self.assertNotEqual(lst, cpy, msg='\n*** Not a new LinkedList object')
        for x in [1, 1, 3, 7, 9, 2, 8]:
            lst.insert(x)
        cpy = lst.copy()
        self.assertNotEqual(lst, cpy, msg='\n*** Not a new LinkedList object')
        orig_node = lst.first
        copy_node = cpy.first
        while orig_node and copy_node:
            self.assertNotEqual(orig_node, copy_node, msg='\n*** Shared nodes')
            self.assertEqual(orig_node.data, copy_node.data,
                             msg='\n*** Not the same data')
            orig_node = orig_node.succ
            copy_node = copy_node.succ
        self.assertEqual(orig_node, copy_node,
                         msg='\n*** Original and copy of different length')


if __name__ == "__main__":
    unittest.main()
