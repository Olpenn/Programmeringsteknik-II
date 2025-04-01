""" linked_list.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""
class Person: #for Ex7
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr


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
        if not f: raise ValueError # Raise ValueError if the list is empty
        if not f.succ: # If there is one record, self.first needs to be set to None
            value = f.data
            self.first = None
        while f.succ.succ: # We want to stop at the second last record
            f = f.succ
        value = f.succ.data  # Store data in a temp variable and remove the pointer to the last record
        f.succ = None
        return value


    def remove(self, x):         # Ex3
        f = self.first
        if f.data == x: # First record is handled different
            self.first = f.succ
            return True
        while f: # Loop through the list
            if f.succ.data == x:
                f.succ = f.succ.succ
                return True
            f = f.succ
        return False
            


    def to_list(self):            # Ex4
        pass
    

    def __str__(self):            # Ex5
        pass

    def copy(self):
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 

    '''

    def copy(self):               # Ex6, Should be more efficient
        pass                      
    ''' Complexity for this implementation:

    '''


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:


if __name__ == '__main__':
    main()
