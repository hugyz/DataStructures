"""
Implement selection sort.
"""

# Selection Sort: sorts the array by constantly finding the min
# O(n^2)
# [5, 2, 6, 4, 1, 3]
def selection_sort(arr):
    for i in range(len(arr)):
        low_index = i
        for j in range(i, len(arr)):
            if arr[low_index] > arr[j]: low_index = j
        if low_index != i: 
            temp = arr[i]
            arr[i] = arr[low_index]
            arr[low_index] = temp
                
    return arr

arr = [5,2,6,4,1,3]
selection_sort(arr)
print(arr)



"""
What i originally went for ---
unefficient, not selection sort due to the increase in swaps

def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
"""