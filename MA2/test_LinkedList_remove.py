
"""
Unittests for the linked lists remove
"""

import unittest
from bst import *
from linked_list import *



class Test(unittest.TestCase):

    def test_remove(self):



        llst = LinkedList()
        print('\nTests remove')
        print('\nFirst, try to remove from empty list. Should return False.')
        self.assertEqual(llst.remove(9), False)

        print('.')
        plist = [1, 2, 2, 3, 5, 6, 6]
        removes = [[0, False, 'before first'], 
                   [4, False, 'in the middle'], 
                   [9, False, 'after last'], 
                   [3, True, 'In the middle'], 
                   [3, False, '3 should not be there'], 
                   [1, True, 'first element'],
                   [2, True, 'new first'],
                   [2, True, 'new first again'],
                   [2, False, '2 should not be there'],
                   [6, True, 'next last'],
                   [6, True, 'last'],
                   [5, True, 'the very last element'],
                   [5, False, '5 should not be there']
                   ]
        for x in plist:
            llst.insert(x)
        print('Testlist: ', plist)
        print('\nRemoves', end=' ')
        for x in removes:
            print(f'{x[0]}', end=' ')
            self.assertEqual(llst.remove(x[0]), x[1], x[2])
        print()
        self.assertEqual(llst.first, None, 'The list is not empty')
        return



if __name__ == "__main__":
    unittest.main()
