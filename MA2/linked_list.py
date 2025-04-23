""" linked_list.py

Student: Olov Rahm
Mail: olra4479@student.uu.se
Reviewed by: Rafael
Date reviewed: 2025-04-23
"""
import time
class Person: #for Ex7
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __lt__(self, obj):
        if self.name < obj.name:
            return True
        return False
    
    def __le__(self, obj):
        if self.name <= obj.name:
            return True
        return False
    
    def __eq__(self, obj):
        if self.name == obj.name:
            return True
        return False
    
    def __str__(self):
        return f'{self.name}:{self.pnr}'

class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None
    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):          #   Ex1
        n = 0
        f = self.first
        while f:
            n += 1
            f = f.succ
        return n

    def mean(self):               
        pass

    def remove_last(self):       # Ex2
        f = self.first
        if f is None: raise ValueError  # Raise ValueError if the list is empty
        if f.succ is None:              # If there is one record, self.first needs to be set to None
            value = f.data
            self.first = None
            return value
        while f.succ.succ:              # We want to stop at the second last record, remove its pointer and return its successors data
            f = f.succ
        value = f.succ.data             # Store data in a temp variable and remove the pointer to the last record
        f.succ = None
        return value


    def remove(self, x):         # Ex3
        f = self.first
        if f is None: return False
        if f.data == x: # First record is handled different
            self.first = f.succ
            return True
        while f.succ is not None: # Loop through the list
            if f.succ.data == x:
                f.succ = f.succ.succ
                return True
            f = f.succ
        return False
            


    def to_list(self):            # Ex4

        def _to_list(node):
            # Recursive Helper function
            if node is not None: return [node.data] + _to_list(node.succ)
            else: return []

        return _to_list(self.first)
    

    def __str__(self):            # Ex5
        if self.length() == 0: 
            return '()'
        name = '('
        for record in self:
            name += f'{record}, '   # Add every item with ", " after
        return name[:-2] + ')'      # Remove the last ", " and add the closing parenthesis

    def copy(self):
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
    Since we need to go through the entire list for every record, it's O(n^2)
    '''

    def copy(self):               # Ex6, Should be more efficient
        result = LinkedList()
        values = reversed(self.to_list())
        for x in values:
            result.insert(x)
        return result
    ''' Complexity for this implementation:
        The three functions "to_list", "reversed" and the loop are all O(n) so the function is O(n)
    '''


def main():
    plist = LinkedList()
    print(plist.length())
    print(plist)

    # Test code:


if __name__ == '__main__':
    main()

"""
for record in iterable:

    iterator = iterable.__iter__()
    record = iterator.__next__()

yield keyword makes the function/method return the entire function/method as a generator and not only the variable directly after. 
Hence an object with the __next__() function is returned.   


"""