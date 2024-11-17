from random import Random
import time

"""
Implement Bubble Sort. 
"""
#constant swaps between neighbors
# O(n^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1): #(optimized)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

start = time.time()
r = Random()
arr = []
for i in range(10000):
    # 0 to one mill
    arr.append(r.randint(0, 1000000))

print (bubble_sort(arr))
end = time.time()

print(end-start)
