# https://docs.python.org/3/library/unittest.html
import unittest

from MA1_solutions import *


class Test(unittest.TestCase):

    def test_get_binary(self):
        print('\nTests positive numbers')
        self.assertEqual(get_binary(0), '0')
        self.assertEqual(get_binary(1), '1')
        self.assertEqual(get_binary(2), '10')
        self.assertEqual(get_binary(3), '11')
        self.assertEqual(get_binary(15), '1111')
        self.assertEqual(get_binary(16), '10000')
        print('OK\nTests negative numbers')
        self.assertEqual(get_binary(-1), '-1')    
        self.assertEqual(get_binary(-15), '-1111')
        self.assertEqual(get_binary(-16), '-10000')
        print('OK')
        return


if __name__ == "__main__":
    unittest.main()
