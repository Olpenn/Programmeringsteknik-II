"""
Solutions to module 4 - A calculator
Student: 
Mail:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA4tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if not wtok.is_at_end():
        raise SyntaxError('Could not interpret syntax')
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if not wtok.is_name(): raise SyntaxError('Variable to assign value to is missing')
        variables[wtok.get_current()] = result
        wtok.next()
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ('+', '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        if wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in ('*', '/'):
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables) 
        if wtok.get_current() == '/':
            wtok.next()
            denomenator = factor(wtok, variables)
            if denomenator == 0: raise EvaluationError('Division by 0 not allowed')
            result = result / denomenator        
    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    functions_1 = {'cos': math.cos, 'sin': math.sin, 'exp': math.exp, 'log': log, 'fac': fac, 'fib': fib}
    functions_n = {'max': max, 'sum': sum}
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in functions_1:
        function = functions_1[wtok.get_current()]
        wtok.next()
        if wtok.get_current() != '(': raise SyntaxError('Expected () around argument')
        else:
            wtok.next()
            result = function(assignment(wtok, variables))
            if wtok.get_current() != ')': raise SyntaxError('Expected )')
            else: 
                wtok.next()

    elif wtok.get_current() in functions_n:
        function = functions_n[wtok.get_current()]
        wtok.next()
        result = function(arglist(wtok, variables))
        wtok.next()

    elif wtok.is_name():
        if wtok.get_current() not in variables: raise EvaluationError(f"variable {wtok.get_current()} not recognized")
        result = variables[wtok.get_current()]
        wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -1*factor(wtok, variables)

    else:
        raise SyntaxError(
            "Expected number, function or '('")  
    return result

def log(x):
    if x <= 0:
        raise EvaluationError(f'Argument {x} not vailid in logarithm function')
    else:
        return math.log(x)

def fac(x):
    if float(int(x)) != x:
        raise EvaluationError(f'Argument {x} not vailid in factorial function')
    else:
        return math.factorial(int(x))

def fib(x):
    if float(int(x)) != x or x < 0:
        raise EvaluationError(f'Argument {x} not valid in fibonacci function')
    x = int(x)
    if x == 0: return 0
    if x in (1,2): return 1
    a = b = 1 # a is the first fibonacci number, b is the second
    for x in range(x-2): # b is always the next fibonacci number compared to a, for x == 3 we want to loop once
        a,b = b,a+b
    return b

def arglist(wtok, variables):
    if wtok.get_current() != '(': raise SyntaxError('Expected () around argument(s)')
    else:
        arguments = []
        wtok.next()
        arguments.append(assignment(wtok, variables))
        while wtok.get_current() == ',':
            wtok.next()
            arguments.append(assignment(wtok, variables))
        if wtok.get_current() != ')': raise SyntaxError('Expected ) or ,')
        return arguments


def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA4init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        
        if wtok.get_current() == 'vars':
            print('Input\t: vars')
            for x in variables:
                print(f'{x}\t: {variables[x]}')
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ee:
                print('*** Evaluation error:', ee)
 


if __name__ == "__main__":
    main()
