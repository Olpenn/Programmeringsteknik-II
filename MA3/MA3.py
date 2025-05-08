""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
import numpy as np
import functools

def approximate_pi(n): # Ex1
    print(f'Number of points: {n}')
    X = [random.uniform(-1,1) for _ in range(n)]
    Y = [random.uniform(-1,1) for _ in range(n)]
    R2 = [x**2 + y**2 for x,y in zip(X,Y)]
    COLOR = ['r' if r2 <= 1 else 'b' for r2 in R2]
    pi = 4*COLOR.count('r')/n
    if __name__ == '__main__':
        plt.figure(figsize=(10,10))
        plt.title(f'n: {n}, Estimation of pi: {pi}', size=30)
        plt.xlim([-1,1])
        plt.ylim([-1,1])
        for x,y,color in zip(X,Y,COLOR):
            plt.scatter(x,y,color=color)
        plt.savefig(f'MA3/pi_estimation_{n}.png')
    # plt.show()
    print(pi)
    return pi

def sphere_volume(n,d):
    # sphere_volume requested in Exercise 2
    COORDINATES = [(random.uniform(-1,1) for _ in range(d)) for _ in range(n)]  # Create a tuple of the d coordinates for each point (n times)
    R2 = map(lambda coordinates: sum(x_i**2 for x_i in coordinates), COORDINATES)   # Calculate R2 using comprehension, lambda and map
    in_circle = filter(lambda r2: r2 <= 1, R2)  # Filter out the points within one unit of the origin.
    npoints_in_circle = sum(1 for _ in in_circle)   # Filter is a generator, loop through and count how many elements are there
    return 2**d * npoints_in_circle/n

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere 
    return m.pi**(d/2)/m.gamma(d/2+1)

def sphere_volume_average(n, d): #Ex3, 10 loops average
    # n is the number of points
    # d is the number of dimensions of the sphere
    results = []
    for _ in range(10):
        volume = sphere_volume(n, d)
        results.append(volume)
    return mean(results)

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    # n is the number of points
    # d is the number of dimensions of the sphere
    # np is the number of processes
    with future.ProcessPoolExecutor() as executor:
        futures = [executor.submit(sphere_volume, n, d) for _ in range(np)]
        results = [f.result() for f in futures]
    return mean(results)

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    # n is the number of points
    # d is the number of dimensions of the sphere
    # np is the number of processes
    n_split = n//np
    with future.ProcessPoolExecutor() as executor:
        futures = [executor.submit(sphere_volume, n_split, d) for _ in range(np)]
        results = [f.result() for f in futures]
    return mean(results)


    
def main():
    Ex = 4 #Choose Exercise

    if Ex == 1:
        dots = [1000, 10000, 100000]
        for n in dots:
            approximate_pi(n)

    elif Ex == 2:
        n = 100000
        d = 2
        print(f"Approximated volume of {d} dimentional sphere = {sphere_volume(n,d)}")
        print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

        n = 100000
        d = 11
        print(f"Approximated volume of {d} dimentional sphere = {sphere_volume(n,d)}")
        print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    elif Ex == 3:
        n = 100000
        d = 11
        start = pc()
        sphere_volume_average(n,d)
        stop = pc()
        print(f"Ex3: Sequential time of d={d} and n={n}: {stop-start}s")
    
        start = pc()
        sphere_volume_parallel1(n,d)
        stop = pc()
        print(f"Ex3: Parallell time of d={d} and n={n}: {stop-start}s")

    elif Ex == 4:
        n = 1000000
        d = 11
        start = pc()
        sphere_volume(n,d)
        stop = pc()
        print(f"Ex4: Sequential time of d={d} and n={n}: {stop-start}s")
 
        start = pc()
        sphere_volume_parallel2(n,d)
        stop = pc()
        print(f"Ex4: Parallell time of d={d} and n={n}: {stop-start}s")

if __name__ == '__main__':
    main()
    


"""
def map(f, iterable):
    map = map_item()
    for record in iterable:
        map.add(f(record))
    return map

def functools.reduce(f, iterable):
    #require that f has 2 inputs
    if len(iterable) == 0: raise TypeError
    elif len(iterable) == 1: return iterable[0]
    elif len(iterable) == 2: return f(iterable[0], iterable[1])
    else: return f(functools.reduce(iterable[:-1]), iterable[-1])

def filter(f, iterable):
    for record in iterable:
        if not f(record)
            iterable.remove(record)
    return iterable
"""

"""
Answer to exersize 2:

sphere_volume(100000, 2) = 3.13704
hypersphere_exact(2) =  3.141592

sphere_volume(100000, 11) = 2.00704
hypersphere_exact(11) =  1.884103
"""

"""
Answer to exersize 3:

The time for the sequential computation is ca. 9.4s (at home computer)
The time for the parallell computation is ca. 4.5s (at home computer)

On my home computer with 4 cores, the results pop out 4 at a time (as expected).
This means it is 3 iterations instead of 10 which means ca. 30% the time.
The time is however ca. 50% of the sequential time. I dont know what explains the difference.
Probably initializing the threading

"""

"""
Answe to exersize 4:

The time for the sequential computation is ca. 8.7s (at home computer)
The time for the parallell computation is ca. 4.2s (at home computer)

That is about double as fast!

"""