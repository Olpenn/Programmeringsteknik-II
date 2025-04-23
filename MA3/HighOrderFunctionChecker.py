import ast

# List of known higher-order functions
higher_order_funcs = {"map", "filter", "reduce", "sorted"}

class HighOrderFunctionChecker(ast.NodeVisitor):
    def __init__(self):
        self.found_higher_order = False

    def visit_Call(self, node):
        # Check if the function being called is a higher-order function
        if isinstance(node.func, ast.Name) and node.func.id in higher_order_funcs:
            print(f"Higher-order function '{node.func.id}' found at line {node.lineno}")
            self.found_higher_order = True

        # Check for qualified function names like 'functools.reduce'
        if isinstance(node.func, ast.Attribute) and node.func.attr in higher_order_funcs:
            print(f"Higher-order function '{node.func.attr}' found at line {node.lineno} in module '{node.func.value.id}'")
            self.found_higher_order = True

        # Check if any argument passed is a lambda function
        for arg in node.args:
            if isinstance(arg, ast.Lambda):
                print(f"Lambda function used as argument in '{node.func.id if isinstance(node.func, ast.Name) else node.func.attr}' at line {node.lineno}")
                self.found_higher_order = True

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Check if any arguments are annotated as functions or take lambdas
        for arg in node.args.args:
            if isinstance(arg.annotation, ast.Name) and arg.annotation.id == 'function':
                print(f"Custom higher-order function '{node.name}' found at line {node.lineno}")
                self.found_higher_order = True

        # Check if lambda functions are inside a function definition
        for body_item in node.body:
            if isinstance(body_item, ast.Lambda):
                print(f"Lambda function defined inside function '{node.name}' at line {node.lineno}")
                self.found_higher_order = True

        self.generic_visit(node)

    def visit_Lambda(self, node):
        # Check standalone lambda expressions
        print(f"Lambda function found at line {node.lineno}")
        self.found_higher_order = True
        self.generic_visit(node)

    def visit_ListComp(self, node):
        # Check for list comprehensions
        print(f"List comprehension found at line {node.lineno}")
        self.found_higher_order = True
        self.generic_visit(node)

    def visit_SetComp(self, node):
        # Check for set comprehensions
        print(f"Set comprehension found at line {node.lineno}")
        self.found_higher_order = True
        self.generic_visit(node)

    def visit_DictComp(self, node):
        # Check for dictionary comprehensions
        print(f"Dictionary comprehension found at line {node.lineno}")
        self.found_higher_order = True
        self.generic_visit(node)

    def visit_GeneratorExp(self, node):
        # Check for generator comprehensions (expressions)
        print(f"Generator comprehension found at line {node.lineno}")
        self.found_higher_order = True
        self.generic_visit(node)

def check_higher_order_functions(file_path):
    try:
        with open(file_path, "r") as source_file:
            source_code = source_file.read()

        # Parse the file content
        tree = ast.parse(source_code)
        checker = HighOrderFunctionChecker()
        checker.visit(tree)

        if not checker.found_higher_order:
            print("No higher-order functions, lambdas, or comprehensions found.")
        return checker.found_higher_order
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False
    except SyntaxError as e:
        print(f"Syntax error in file '{file_path}': {e}")
        return False