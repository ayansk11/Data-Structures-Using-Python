
#@author [Ayan Shaikh]
#@email [ayansk152@gmail.com]
#@create date 2023-07-11 20:16:12
#@modify date 2023-07-11 20:25:02
#@desc [Implementing Insertion Sort Using Python Programming]


#            INSERTION SORT


#   The Overall Time Complexity = O(n) * O(n) = O(n*n) = O(n^2)


#     CASE             Time Complexity
#
#   Best Case	             O(n)
#   Average Case	    O(n^2)
#   Worst Case	            O(n^2)


import random
import time
import numpy as np

print("\nCreating an array of random numbers : \n") 

arr = np.random.randint(10000, size = 10)       # creating a 1-D array of random numbers

print(arr)          # printing the unsorted array 
print("\n")

def insertionsort(arr):

    counter = 0

    for i in range(1, len(arr)):

        curr_index = i

        while curr_index > 0 & arr[curr_index] < arr[curr_index - 1]:

            counter += 1

            arr[curr_index], arr[curr_index - 1] = arr[curr_index - 1], arr[curr_index]

            curr_index = curr_index - 1

    return counter

print("\nPerforming Insertion Sort on the Array..................\n")
tic = time.time()  # capture start time
result = insertionsort(arr)
toc = time.time()  # capture end time

print("\n"+"*****"*12+"\n\nPrinting the Sorted Array : \n")
print(arr)
print("\n"+"*****"*12)
print(f"\nNumber of swaps done: ", result)
print("\n"+"*****"*12) 
print(f"\nTime Taken: {1000*(toc-tic):.4f} ms")
print("\n"+"*****"*12) 
