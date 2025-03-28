"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    """ Ex1: Computes m*n using additions"""
    # Minimize recursive calls, make sure m >= n
    if m < n: m, n = n, m   # Swap algorithm
    
    # Base case
    if n == 0: return 0
        
    # Recursive call
    return m + multiply(m, n-1)


def harmonic(n: int) -> float:              
    """Ex2: Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    # Base case
    if n == 1: return 1
        
    # Recursive Call
    return 1/n + harmonic(n-1)


def get_binary(x: int) -> str:              
    """ Ex3: Returns the binary representation of x """
    # If the number is negative, write a '-' followed by the positve binary representation
    if x < 0: return '-' + get_binary(-x)
        
    # Recursive call, if the number is bigger than two, write the binary representation of half the number 
    # (rounded down) and append a string with the remainder
    if x // 2: return get_binary(x//2) + str(x%2)

    # Base case, if the number is smaller than 2, just return the number as a string 
    return str(x)

def reverse_string(s: str) -> str:        
    """Ex4: Returns the s reversed """
    if s: return reverse_string(s[1:]) + s[0] # Recursive call
    return ''   # Base case
    

def largest(a: iter):                     
    """Ex5: Returns the largest element in a"""
    N = len(a)

    # Base case
    if N == 1: return a[0] 

    # Recursive calls
    largest_first_half = largest(a[:N//2])
    largest_second_half = largest(a[N//2:])

    # Return the bigger of the two halves
    if largest_first_half > largest_second_half: return largest_first_half
    return largest_second_half

def count(x, s: list) -> int:                
    """Ex6: Counts the number of occurences of x on all levels in s """
    N = len(s)
        
    # Base case: List is of length smaller than 2
    if N == 0: return 0                                 # If there is no element, return 0
    if N == 1:
        elem = s[0]                                     # Assign the value of the first element to a variable.
        if elem == x: return 1                          # Check for match 
        if type(elem) == list: return count(x, elem)    # Check for nested matches
        return 0                                        #If there isn't a match nor elem is a list 

    # Recursive call: Add the count for the first and second half of the list.
    if N >= 2: return count(x, s[:N//2]) + count(x, s[N//2:])

def bricklek(f: str, t: str, h: str, n: int) -> str:  
    """Ex7: Returns a string of instruction ow to move the tiles """
    pass


def fib(n: int) -> int:                      
    """ For Ex9: Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print('\nCode that demonstates my implementations\n')
    print(count([1,2], []))
    print('\n\nCode for analysing fib and fib_mem\n')

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  
  
  
  
  Exercise 9: Time for Fibonacci:


  
  
  Exercise 10: Time for fib_mem:
  
  
  
  
  
  Exercise 11: Comparison sorting methods:
  
  
  
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  
  
"""
