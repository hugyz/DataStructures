"""
Implement insertion sort.
"""

# O(n) -- best case O(n^2) -- worse case
# sorting algorithm that sorts by creating a constantly growing arr of sorted elements
# and comparing each new one against ones in sorted arr
def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else: break


arr = [6, 5, 3, 1, 8, 7, 2, 4]
insertion_sort(arr)
print(arr)

"""
What I originally went for:

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[j] > arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
"""