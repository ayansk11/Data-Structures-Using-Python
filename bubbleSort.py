#Patrick Madonna 2023
#Time Complexity O(n^2)
import numpy as np

def bubbleSort(arr):
    l = len(arr)
    isSwapped = False
    for i in range(l-1): # in this test scenero it should go from 0-8
        for x in range(0,l-i-1):
            if arr[x] > arr[x+1]:
                isSwapped = True
                arr[x], arr [x+1] = arr[x+1], arr[x] # this takes 3 and 2 and switches them to 2 and 3
        if not isSwapped:
            #this should be called if there are no swaps.
            return "This is already in order"
    return "This is the sorted array:{}".format(arr)


arr = np.random.randint(10000, size = 10)
print(bubbleSort(arr))

sortedArr = np.array([1,2,3,4,5,6], np.int32)
print(bubbleSort(sortedArr))