
#   @author [Ayan Shaikh]
#   @email [ayansk152@gmail.com]
#   @create date 2023-06-22 00:58:01
#   @modify date 2023-06-29 19:45:39
#   @desc [Implementing Binary Search Using Recursion in Python]


#               BINARY SEARCH


#     CASE                 Time Complexity
#      
#   Best Case	                O(1)
#   Average Case	           O(logn)
#   Worst Case	               O(logn)



import random                                   # importing built-in random module. The random module provides functions to generate random numbers and perform random operations. 
import time                                     # importing built-in time module which provides various functions related to time and timing. It can be used for tasks like measuring the time taken by a piece of code to execute or introducing delays in your program.
import numpy as np                              # importing the third-party library numpy and giving it the alias np. numpy is a powerful library for numerical computations in Python. It provides support for working with large, multi-dimensional arrays and matrices, along with a wide range of mathematical functions to operate on these arrays efficiently.

print("\nCreating an array of random numbers\n") 

arr = np.random.randint(10000, size = 10)       # creating a 1-D array of random numbers

arr.sort()          # sorting the array in an ascending order
print(arr)          # printing the list 
print("\n")
      
counter = 0             # setting a counter to count the number of iterations

low = 0                   # initially low will be zero
high = len(arr) - 1       

def binarysearch(search_for, arr, low, high, counter):       # defining the function that will perform binary search (recurrsively)

    if low <= high:                         # condtion to prevent the code from going into infinite loop

        mid = (low + high) // 2             # condition to find mid
       
        if search_for > arr[mid]:           # If element is greater than mid, then it can only be present in the right subarray   
            counter = counter + 1
            return binarysearch(search_for, arr, mid + 1, high, counter)
        
        elif search_for < arr[mid]:         # If element is smaller than mid, then it can only be present in the left subarray
            counter = counter + 1
            return binarysearch(search_for, arr, low, mid - 1, counter)
        
        elif search_for == arr[mid]:        # If element itself is present at the middle 
            counter = counter + 1
            return mid, counter
    else:                                   # Element is not present in the array                  
        return -1, counter


search_for = int(input("Enter the number you want to search: "))

tic = time.time()  # capture start time
search_result = binarysearch(search_for, arr, low, high, counter)                   # Calling the binarysearch function we defined above
toc = time.time()  # capture end time

if search_result[0] == -1:                                                          # Printing the results
    
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