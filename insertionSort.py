#Instertion Sort Algorithm is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
#Think of how you sort your cards in Uno
#we aasume that the first value is already sorted 

def InsertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    

samplearr = [9,5,1,4,3]
InsertionSort(samplearr)
print(samplearr)