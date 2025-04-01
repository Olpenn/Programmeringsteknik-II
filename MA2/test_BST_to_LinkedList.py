# https://docs.python.org/3/library/unittest.html
"""
Unittests for the binary search tree methods

"""

import unittest

from bst import *
from linked_list import *

import random
import time


class Test(unittest.TestCase):

    def test_to_LinkedList(self):
        self.assertIsInstance(author, str, "Variable 'author' is not set")
        self.assertIsInstance(reviewer, str, "Variable 'reviewer' is not set" )
        self.assertNotEqual(author,'Your name', 'Your name is missing!')
        print(f"\nTests the method 'to_LinkedList' in BST written by {author}. Reviewer: {reviewer}") 

        bst = BST()
        lst = LinkedList()
        for x in [5, 3, 8, 1, 4, 6, 9, 2, 7]:
            bst.insert(x)
            lst.insert(x)
        self.assertEqual(str(bst.to_LinkedList()), str(lst))

        print('\nChecking the complexity')

        measured_time = []
        test_set = (2000, 4000, 8000)
        for n in test_set:
            bst = BST()
            for x in range(n):
                bst.insert(random.random())
            tstart = time.perf_counter()
            ll = bst.to_LinkedList()
            measured_time.append(time.perf_counter() - tstart)

        print('  Size   Time   Factor ')
        for i in range(0, len(test_set)):
            print(f'{test_set[i]:6d} {measured_time[i]: 6.2f}', end=' ')
            if i > 0:
                print(f'{measured_time[i]/measured_time[i-1]:6.1f}')
            else:
                print()
        self.assertLess(measured_time[-1]/measured_time[-2], 2.6,
                        '\n\n*** Probably Theta(n^2) instead of Theta(n)')
        print('Complexity probably Therta(n) which it should be')


if __name__ == "__main__":
    unittest.main()
