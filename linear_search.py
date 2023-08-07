
#   @author [Ayan Shaikh]
#   @email [ayansk152@gmail.com]
#   @create date 2023-06-21 22:08:33
#   @modify date 2023-08-08 01:43:31
#   @desc [Implementing Linear Search in Python]



#           LINEAR SEARCH


#     CASE             Time Complexity
#
#   Best Case	            O(1)
#   Average Case	        O(n)
#   Worst Case	            O(n)



import random                                   # importing built-in random module. The random module provides functions to generate random numbers and perform random operations. 
import time                                     # importing built-in time module which provides various functions related to time and timing. It can be used for tasks like measuring the time taken by a piece of code to execute or introducing delays in your program.
import numpy as np                              # importing the third-party library numpy and giving it the alias np. numpy is a powerful library for numerical computations in Python. It provides support for working with large, multi-dimensional arrays and matrices, along with a wide range of mathematical functions to operate on these arrays efficiently.


print("\nCreating an array of random numbers\n") 

arr = np.random.randint(10000, size = 10)       # creating a 1-D array of random numbers

print(arr)          # printing the list 
print("\n")

counter = 0

def linearsearch(search_for, arr, counter):     # Defining the function that will perform linear search (iteratively)

    for i in range(len(arr)):

        counter = counter + 1

        if search_for == arr[i]:

            return i, counter

    return -1, counter

search_for = int(input("Enter the number you want to search: "))
        
tic = time.time()  # capture start time
search_result = linearsearch(search_for, arr, counter)          # Calling the linearsearch function that we defined above 
toc = time.time()  # capture end time

if search_result[0] == -1:                                      # printing the result
    
    print("\n"+"*****"*12)
    print(f"\nNumber {search_for} not found in the list\n")
    print("*****"*12)
    print(f"\nNumber of iterations done: ", search_result[1])
    print("\n"+"*****"*12) 
    
else:
    print("\n"+"*****"*12)
    print(f"\nNumber {search_for} found at index position {search_result[0]} in the list\n")
    print("*****"*12)
    print(f"\nNumber of iterations it took to find the number: ", search_result[1])
    print("\n"+"*****"*12) 

print(f"\nTime Taken: {1000*(toc-tic):.4f} ms")
print("\n"+"*****"*12) 
