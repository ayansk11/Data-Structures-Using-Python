import random
import time
import numpy as np

print("\nCreating an array of random numbers\n") 

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

tic = time.time()  # capture start time
result = insertionsort(arr)
toc = time.time()  # capture end time

print("\n"+"*****"*12+"\n")
print(arr)
print("\n"+"*****"*12)
print(f"\nNumber of swaps done: ", result)
print("\n"+"*****"*12) 
print(f"\nTime Taken: {1000*(toc-tic):.4f} ms")
print("\n"+"*****"*12) 
