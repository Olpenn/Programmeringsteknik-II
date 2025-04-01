"""
Solutions to module 1
Student: Olov Rahm
Mail: ollerahm50@gmail.com
Reviewed by: Jakob Frick
Reviewed date: 01/04-25
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
    
    # Base case, if the number is smaller than 2, just return the number as a string  
    if x < 2: return str(x)

    # Recursive call, if the number is bigger than two, write the binary representation of half the number 
    # (rounded down) and append a string with the remainder
    return get_binary(x//2) + str(x%2)

    
    

def reverse_string(s: str) -> str:        
    """Ex4: Returns the s reversed """
    # Base case, if string is empty or only one character long, return the string 
    if len(s) <= 1: return s   
    
    # Recursive call
    return reverse_string(s[1:]) + s[0] # Recursive call
    
    

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
    else: return largest_second_half

def count(x, s: list) -> int:                
    """Ex6: Counts the number of occurences of x on all levels in s """
    N = len(s)
        
    # Base case: List is of length 0 or 1
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
    if n == 0: return [] # Empty tower require no moves
    # Move all tiles from f to h, move the biggest tile to t, move the tiles from h to t
    return bricklek(f, h, t, n-1) + [f'{f}->{t}'] + bricklek(h, t, f, n-1)


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
    
def fib_mem(n):
    start = time.perf_counter()
    memory = {0:0, 1:1}  # Define memo in this scope to avoid global variables
    def _fib(n):
        if n not in memory:
            memory[n] = _fib(n-1) + _fib(n-2) # Use memoization if possible
        return memory[n]
    end = time.perf_counter()
    return _fib(n), end-start


def main():
    print('\nCode that demonstates my implementations\n')
    print(bricklek('f', 't', 'h', 0))
    print('\n\nCode for analysing fib and fib_mem\n')
    if True: # Set to True for fibonacci time complexity approximation (Exercise 9)
        def time_fib(n):
            # Function to time the fib function
            start = time.perf_counter()
            print(f'Running fib({n})...')
            fib(n)
            end = time.perf_counter()
            return end-start
        
        n_arr = [5*i for i in range(6)]
        t_arr = []
        for n in n_arr:
            t_arr.append(time_fib(n))
        print('t_arr', t_arr)

        # Ansatz is C * 1.618**n, find C
        def error2(C):
            err2 = 0
            for t, n in zip(t_arr, n_arr):
                err2 += t - C*1.618**n
            return err2
        
        def error_der(C):
            dC = 10**(-6)
            return (error2(C+dC) - error2(C-dC))/(2*dC)
            
        # Assume the derivative being increasing
        C_min = 0
        C_max = 10**(-3)
        i = 0
        while C_max-C_min > 10**(-6) and i < 100:
            C_mid = (C_max - C_min)/2 
            derivative = error_der(C_mid)
            print(C_max)
            if derivative < 0:
                C_min = C_mid
            else:
                C_max = C_mid
            print(C_mid)
            i += 1
            
        t_50 = C_mid*1.618**50 # n = 50
        t_100 = C_mid*1.618**50 # n = 100
        print(f'n = 50, t = {math.floor(t_50)}s = {math.floor(t_50/3600)}h')
        print(f'n = 100, t = {math.floor(t_100)}s = {math.floor(t_100/3600)}h = {math.floor(t_100/(3600*24*365.25))} years')
    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  
  The text tells us the number of operations in the tile game (t(n)) scales with the amount of tiles (n) as:
  t(n) = 2^n -1. If we assume one operation takes one second the game will last 2^50 -1 = 1125899906842623 seconds
  = 35677615 years
  
  
  Exercise 9: Time for Fibonacci:

  Calculating the time for fibonacci numbers 5,10,15,20,25,30,35 and then extrapolating using built-in optimizer
  with the model y = C*a^x gives a = 1.593 with variance 6.12e-06. Which is a bit lower than expected but this is
  explained by n being small. (These numbers vary rather much between runs as well)
  
  
  Exercise 10: Time for fib_mem:
  
  When implementing the memoization algorithm calculating the 100th fibonacci number takes 6.3e-06 seconds
  The number is: 354224848179261915075
  
  
  Exercise 11: Comparison sorting methods:
  
  Insersion sort is of complexity O(n^2). The numbers we're handling are ~10^3 and can hance be approximated as large.
  Then t(1000) = c*1000^2 = 1s. Then c = 10^-6 s. Hence we calculate:
  t(10^6) = 10^6 s ~ 11.5 days
  t(10^9) = 10^12 s ~ 31688 years

  Merge sort is of complexity O(nlog(n)). Same resoning can be done here; ansatz t(n) = c*nlog(n) (natural log is used
  even though the base is arbitrary).
  Then t(1000) = c*1000*ln(1000) = 1s. Then c = 0.00014476482730108395 s.
  t(10^6) = 2000 s ~ 33 min
  t(10^9) = 3000000 s ~ 35 days

  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  
  For algorithm A: t(n) = n
  For algorithm B: t(n) = c*n*log(n)
  t(10) = c*10*log(10) = 1s. Then c = 1/(10*log(10))
  When is n = n*log(n)/(10*log(10))?
  Algebra gives: 
  log(n) = 10*log(10)
  n = e^(10*log(10)) = e^(log(10^10)) = 10^10
  Answer: algorith A is faster than algorithm B when n > 10^10. For lower n, B is faster.
"""
