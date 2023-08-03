'''Python Selection Sort Algorithm by Patrick Madonna'''
import random

def selectionSort(array):
    min = 0
    #you have to use len() as an array itself is not iterable
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array [min]:
                min = j
        #swapping the elements happens here
        temp = array[min]
        array[min] = array[i]
        array[i] = temp

array = []

for i in range(1,11):
    array.append(random.randint(0,1000))

print("Unsorted Array:\n{}\n".format(array))
selectionSort(array)
print("Sorted Array:\n{}\n".format(array))

