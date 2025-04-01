# https://docs.python.org/3/library/unittest.html
import unittest

from MA1_solutions import *


class Test(unittest.TestCase):

    def test_bricklek(self):
        print('\nTests bricklek')
        res = bricklek('f', 't', 'h', 0)
        self.assertEqual(res, [])
        res = bricklek('f', 't', 'h', 1)
        self.assertEqual(res, ['f->t'])
        res = bricklek('f', 't', 'h', 2)
        self.assertEqual(res, ['f->h', 'f->t', 'h->t'])
        res = bricklek('f', 't', 'h', 3)
        self.assertEqual(res, ['f->t', 'f->h', 't->h',
                               'f->t', 'h->f', 'h->t', 'f->t'])
        res = bricklek('f', 't', 'h', 4)
        self.assertEqual(res,
                         ['f->h', 'f->t', 'h->t', 'f->h', 't->f', 't->h', 'f->h', 'f->t',
                          'h->t', 'h->f', 't->f', 'h->t', 'f->h', 'f->t', 'h->t'])


if __name__ == "__main__":
    unittest.main()
