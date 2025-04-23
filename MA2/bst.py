""" bst.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k): # given function
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None
    
    def contains(self, k):
        def _contains(r, k):
            if r is None: return False      # If the node doesn't exist, return False
            elif r.key == k: return True    # If the node has the target as key, return True
            elif k < r.key: return _contains(r.left, k) # If smaller, search the left
            else: return _contains(r.right, k)  # If bigger, search the right
        
        return _contains(self.root, k)

    # def contains(self, k) # Ex8: write recursive contains

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                 #        Ex9     
        def _height(r):
            if r is None: return 0
            else: return 1 + max(_height(r.left), _height(r.right))
        
        return _height(self.root)

    def __str__(self):                #     Ex10       
        if self.size() == 0: return '<>'
        string = '<'
        for record in self: string += f'{record}, '
        string = string[:-2] + '>'
        return string


    def to_list(self):                      #   Ex11   
        arr = []
        for record in self: arr += [record]
        return arr
    """
    Complexity of to_list: O(n)
    """

    def to_LinkedList(self):                 #     Ex12
        linkedlist = LinkedList()
        list = reversed(self.to_list())
        for record in list: linkedlist.insert(record)
        return linkedlist
    """
    Complexity of _LinkedList: O(n)
    """
    
    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Ex13
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                node = r.right  # Find the smallest key in the right subtree
                while node.left is not None:
                    node = node.left
                smallest_right = node.key 
                r.key = smallest_right  # Put that key in this node
                r.right = self._remove(r.right, smallest_right) # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above



def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print(t)

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")


if __name__ == "__main__":
    main()


"""
Ex14: What is the generator good for?
==============================

1. computing size?      Yes!    for record in self: size += 1
2. computing height?    No!     Records are not enough info to compute height 
3. contains?            No!     The usage of the generator results in O(n), not O(log n)
4. insert?              No!     We need to use the tree structure, not the records
5. remove?              No!     We need to modify the tree structure, access to the records are not useful

"""
