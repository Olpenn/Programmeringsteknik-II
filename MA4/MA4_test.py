
"""
This is a unit test för the calculator assignment.
In order to use the test BEFORE all requirements are implemented
you can comment out lines for unimplemneted features.

"""


import unittest
import math
from MA4 import *


variables_init = {"ans": 0.0, "E": math.e, "PI": math.pi}


class Test(unittest.TestCase):

    def test_statement(self):
        print('\n\nTesting basic arithemtic')
        variables = variables_init

        tests = {'1+2': 3., '2-1': 1., '2+1-2': 1., '2-2+1': 1., '2*3': 6., '4/2': 2.,
                 '8*2/2': 8., '8/2*2': 8., '(2+1)*2': 6., '2*(2+1)': 6., '(2+1)*(2+2)': 12.,
                 '6/(2*3)': 1., '-(-2-3)': 5., '1+2-2=x': 1., '2*x+4': 6., '2=x=y': 2.,
                 'x*y': 4., '(1=x)+(2=y)=z': 3.}

        for line, answer in tests.items():
            print(f'{line:20s} expects {answer}', end='\t')
            wtok = TokenizeWrapper(line)
            result = statement(wtok, variables)
            print(f'got {result}')
            self.assertEqual(result, answer)

    def test_functions(self):
        print('\n\nTesting functions')
        variables = variables_init
        tests = {'sin(PI)+1': 1.,
                 'sin(PI/2)+4': 5.,
                 'cos(PI)': -1.,
                 'log(E)': 1.,
                 'exp(7-2*3=x) - E': 0.,
                 'exp(log(3))': 3.,
                 '(sin(2)=x)*x + (cos(2)=y)*y': 1.
                 }
        for line, answer in tests.items():
            print(f'{line:30s} expects {answer:-8}', end='\t')
            wtok = TokenizeWrapper(line)
            result = statement(wtok, variables)
            print(f'got {round(result,15):-8}')
            self.assertAlmostEqual(result, answer)
        """
        print('Test that arglist returns a list of evaluated expressions')
        wtok = TokenizeWrapper('(1+3,2,3*4)')
        self.assertEqual(arglist(wtok, {}), [4, 2, 12])
        """

    def test_integer_functions(self):
        print('\n\nTesting functions returning int')
        variables = variables_init
        tests = {
            'fac(3)': 6,
            'fac(20)': 2432902008176640000,
            'fac(25)': 15511210043330985984000000,
            'fib(4)': 3,
            'fib(10)': 55,
            'fib(100)': 354224848179261915075,
            'fib(103)': 1500520536206896083277
        }

        for line, answer in tests.items():
            print(f'{line:10s} expects {answer:-27}', end=' ')
            wtok = TokenizeWrapper(line)
            result = statement(wtok, variables)
            print(f'got {round(result,25):-27}')
            self.assertEqual(result, answer)

    def test_exceptions(self):
        print('\n\nTesting exceptions')
        variables = variables_init

        tests = ['1+*2', 'sin 2', '((1)++)', '1=2',
                 '*1', '1=x+2', '2+3 4']

        for line in tests:
            print(f'{line:30s} expects SyntaxError', end=' \t \t ')
            wtok = TokenizeWrapper(line)
            with self.assertRaises(SyntaxError):
                result = statement(wtok, variables)
            print('Got it')

        line = '((1)'
        print(f'{line:30s} expects SyntaxError. Note: TokenError is fine, go ahead.', end=' \t \t ')
        wtok = TokenizeWrapper(line)
        with self.assertRaises(SyntaxError):
            result = statement(wtok, variables)
        print('Got it')

        tests = ['xxx', 'a+b', '1/(2*3-6)', 'log(-1)',"log(0)",
                 'fib(-1)', 'fac(1.5)', '1/sin(1-1)']
        for line in tests:
            print(f'{line:30s} expects EvaluationError', end=' \t \t ')
            wtok = TokenizeWrapper(line)
            with self.assertRaises(EvaluationError):
                result = statement(wtok, variables)
            print('Got it')


if __name__ == "__main__":
    print('\n\nThe testcode initializes variables to\n', variables_init)
    unittest.main()