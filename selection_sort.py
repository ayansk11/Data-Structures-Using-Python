
# @author [Ayan Shaikh]
# @email [ayansk152@gmail.com]
# @create date 2023-06-29 22:45:15
# @modify date 2023-06-29 22:47:02
# @desc [Implementing Selection Sort Using Python Programming]


#            SELECTION SORT


#   The time complexity of Selection Sort is O(n^2) as there are two nested loops:

#       1) One loop to select an element in the array one by one = O(n)
#       2) Another loop to compare that element with every other element in the array = O(N)

#   Therefore overall Time Complexity = O(n) * O(n) = O(n*n) = O(n^2)


#     CASE             Time Complexity
#
#   Best Case	            O(n^2)
#   Average Case	     O(n^2)
#   Worst Case	            O(n^2)



import random
import time
import numpy as np

print("\nCreating an array of random numbers\n") 

arr = np.random.randint(10000, size = 10)       # creating a 1-D array of random numbers

print(arr)          # printing the unsorted array 
print("\n")
      

def selectionsort(arr):             #   function that will perform selection sort

    counter = 0                     #   setting a counter to count the number of swaps

    for i in range(len(arr)-1):               #   loop that will select an element in the array one by one

        for j in range(i+1, len(arr)-1):      #   loop that will compare the selected element with every other element in the array

            if arr[i] > arr[j]:               #   Swap if this condition is true

                counter = counter + 1
                arr[i],  arr[j] = arr[j], arr[i]        #   Swapping

    return arr, counter


tic = time.time()  # capture start time
search_result = selectionsort(arr)
toc = time.time()  # capture end time

print("\n"+"*****"*12+"\n")
print(arr)
print("\n"+"*****"*12)
print(f"\nNumber of swaps done: ", search_result[1])
print("\n"+"*****"*12) 
print(f"\nTime Taken: {1000*(toc-tic):.4f} ms")
print("\n"+"*****"*12) 
