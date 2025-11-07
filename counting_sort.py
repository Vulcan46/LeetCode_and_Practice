# This example only considers positive numbers
# O(n + K) where k is the maximum element of the array
# we find the max and then make an array of size max+1
# since we are dealing with positive numbers, we simply count how many of a particular number there are
# and increment that index eqt to the number by 1 each time.
# once we have all the counts, we navigate the indexes with count>0, and make an array of the index values,
# which are infact the original elemants of the array
def counting_sort(arr):
    maxx = max(arr)
    counter = [0] * (maxx+1)

    for i in range(len(arr)):
        counter[arr[i]] +=1

    k=0
    for j in range(maxx+1):
        while counter[j]>0:
            arr[k] = j
            k+=1
            counter[j]-=1

    return  arr

print(counting_sort([1,4,9,0,11,2,1,6,2,10,39]))