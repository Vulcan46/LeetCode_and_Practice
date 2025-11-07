#O(n^2) again
# The array is "divided" into 2 seactions, 1 is sorted and the other is not sorted.
# Every element traversed is plced in the correct position in the sorted section.
def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        for j in range(i,0,-1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break

    return a
print(insertion_sort([1,4 -9,0,11,2,1,6,-2,-10,39]))