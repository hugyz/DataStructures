import sys

"""
Implement Merge Sort
"""


# helper method for merge_sort
# performs the comparisons and reassignments on the original array
def merge(arr, low, high):
    sorted_array = []
    i = j = 0
    
    # Merge the two arrays while maintaining sorted order
    while i < len(low) and j < len(high):
        if low[i] <= high[j]:
            sorted_array.append(low[i])
            i += 1
        else:
            sorted_array.append(high[j])
            j += 1
    
    # Add any remaining elements from the low or high array
    sorted_array.extend(low[i:])
    sorted_array.extend(high[j:])
    
    return sorted_array


# n log(n) sorting algorithm that behaves like a binary tree in its
# recursive-based method of splitting and sorting
def merge_sort(arr):
    # Base case: If the array has 1 or no elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half
    
    # Merge the two sorted halves
    return merge(arr, left_half, right_half)

arr = [8,2,7,6,9,3,4,1,0,5]
merge_sort(arr)
print(arr)
