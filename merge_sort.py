# array is divided reccursively
# until we get to the base case array which is an array of 1 element
# then these divided arrays are recursively merged and returned, passed as input throught the call stack
# any remaining elements of the left or right half are merged in each pass.
# O(n log n)

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n//2
    L = arr[:mid]
    R = arr[mid:]
    L = merge_sort(L)
    R = merge_sort(R)

    l_size, r_size = len(L), len(R)
    i,j =0, 0
    a_sorted = [0] * n
    k=0
    while i<l_size and j<r_size:
        if L[i]<R[j]:
            a_sorted[k] = L[i]
            i+=1
        else:
            a_sorted[k] = R[j]
            j+=1
        k+=1

    while i < l_size:
        a_sorted[k] = L[i]
        i+=1
        k+=1
    while j < r_size:
        a_sorted[k] = R[j]
        j+=1
        k+=1

    return a_sorted

print(merge_sort([1, 1, -5, 0, 6, -2, -10, 11, 2, 39]))