"""
Implement quicksort.
"""

# Quicksort: Divide and Conquer
# O(n log n)
# [5, 2, 6, 4, 1, 3]
def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)

        quicksort(arr, left, pivot-1)       #left
        quicksort(arr, pivot+1, right)      #right
    

def partition(arr, left, right) -> int:
    pivot = arr[right]
    index = left - 1

    for i in range(left, right):
        if arr[i] < pivot:
            index += 1
            swap(arr, i, index)
    
    swap(arr, right, index+1)
    return index+1

def swap(arr, i, j) -> tuple:
    arr[i], arr[j] = arr[j], arr[i]     #implicit tuple creation
    
arr = [5,2,6,4,1,3]
quicksort(arr, 0, len(arr)-1)
print(arr)
