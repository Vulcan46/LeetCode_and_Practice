# Heap s and priority queues are the same thing.
# max or min element at root or index 1(if done with an array


#O(n) time, if array already exists then O(1) space
import heapq
def min_heapify(arr):
    # sift down : start at 1 level above leaf node level, swap parents
    heapq.heapify(arr)
    return arr

def max_heapify(arr):
    arr = [-x for x in arr]
    heapq.heapify(arr)
    arr = [-x for x in arr]
    return arr
#extract min or max O(log n)
def heap_pop(arr):
    return heapq.heappop(arr)


#add to the heap O(log n)
def heap_push(arr,x):
    heapq.heappush(arr,x)
    return arr

# O(n log n)
def heap_sort(arr):
    arr = min_heapify(arr)
    n = len(arr)
    new_arr = [0]*n
    for i in range(n):
        new_arr[i] = heap_pop(arr)
    return new_arr

a = [-3,-14,0,9,2,1,99]
print(min_heapify(a))
print(heap_sort(a))