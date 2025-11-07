#O(n^2) again.
# We select elements from the remaining array. Each  index position is decided in i to n passes.
# here i goes from 0 to n an j goes from i to n since anything before i^th index is selected
def selection_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            if a[j]<a[i]:
                a[j], a[i] = a[i], a[j]
    return a
print(selection_sort([1,4,-9,0,11,2,1,6,-2,-10,39]))