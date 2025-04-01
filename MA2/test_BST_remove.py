"""
Unittests for the binary search tree methods
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_remove(self):
        self.assertIsInstance(author, str, "Variable 'author' is not set")
        self.assertIsInstance(reviewer, str, "Variable 'reviewer' is not set" )
        self.assertNotEqual(author,'Your name', 'Your name is missing!')
        print(f"\nTests the method 'remove' in BST written by {author}. Reviewer: {reviewer}") 

        def is_bst(node):
            if node is None:
                return True
            elif node.left and node.left.key > node.key:
                return False
            elif node.right and node.right.key < node.key:
                return False
            else:
                return is_bst(node.left) and is_bst(node.right)

        print('\nTests BST remove')
        bst = BST()
        lst = [10, 5, 3, 8, 1, 4, 6, 9, 2, 7]
        print('Insert order: ', lst)        
        for x in lst:   
            bst.insert(x)
        print(f'Initial tree : {bst}')
        removes = [2, 1, 4, 6, 5, 3, 7, 8, 9, 10]
        for x in removes:
            bst.remove(x)
            print(f'After remove {x}: {bst}')
            self.assertTrue(is_bst(bst.root), f'Not a BST: {bst}')
        return
    
        bst.remove(2)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 2: {bst}')
        self.assertEqual(str(bst), '<1, 3, 4, 5, 6, 7, 8, 9, 10>')
        bst.remove(1)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 1: {bst}')
        self.assertEqual(str(bst), '<3, 4, 5, 6, 7, 8, 9, 10>')
        bst.remove(4)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 4: {bst}')
        self.assertEqual(str(bst), '<3, 5, 6, 7, 8, 9, 10>')
        bst.remove(6)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 6: {bst}')
        self.assertEqual(str(bst), '<3, 5, 7, 8, 9, 10>')
        bst.remove(2)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 2: {bst}')
        self.assertEqual(str(bst), '<3, 5, 7, 8, 9, 10>')
        bst.remove(5)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 5: {bst}')
        self.assertEqual(str(bst), '<3, 7, 8, 9, 10>')
        bst.remove(3)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 3: {bst}')
        self.assertEqual(str(bst), '<7, 8, 9, 10>')
        bst.remove(7)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 7: {bst}')
        self.assertEqual(str(bst), '<8, 9, 10>')
        bst.remove(8)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 8: {bst}')
        self.assertEqual(str(bst), '<9, 10>')
        bst.remove(9)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 8: {bst}')
        self.assertEqual(str(bst), '<10>')
        bst.remove(10)
        self.assertTrue(is_bst(bst.root), f'Not a BST after remove 10: {bst}')
        self.assertEqual(str(bst), '<>')


if __name__ == "__main__":
    unittest.main()
