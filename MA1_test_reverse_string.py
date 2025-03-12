# https://docs.python.org/3/library/unittest.html
import unittest

from MA1_solutions import *


class Test(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('1'), '1')
        self.assertEqual(reverse_string('1a'), 'a1')
        self.assertEqual(reverse_string('123456'), '654321')


if __name__ == "__main__":
    unittest.main()
