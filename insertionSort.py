#Patrick Madonna 2023

#Instertion Sort Algorithm is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
#Think of how you sort your cards in Uno
#we aasume that the first value is already sorted 

import numpy as np

def InsertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    

samplearr = np.random.randint(10000, size= 15)
InsertionSort(samplearr)
print(samplearr)