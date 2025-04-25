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

def approximate_pi(n): # Ex1
    print(f'Number of points: {n}')
    X = [random.uniform(-1,1) for _ in range(n)]
    Y = [random.uniform(-1,1) for _ in range(n)]
    R2 = [x**2 + y**2 for x,y in zip(X,Y)]
    COLOR = ['r' if r2 <= 1 else 'b' for r2 in R2]
    plt.figure()
    plt.xlim([-1,1])
    plt.ylim([-1,1])
    for x,y,color in zip(X,Y,COLOR):
        plt.scatter(x,y,color=color)
    plt.show()
    return X

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere 

    return 

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere 
    return

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
      #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    pass

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    return 
    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #Ex3
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    
    

if __name__ == '__main__':
	approximate_pi(10000)
    #main()
