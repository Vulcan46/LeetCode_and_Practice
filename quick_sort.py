#O(n log n)
# a pivot element is chosen and the array elements are divided into elements lt pivot and gt pivot
# this is done recursively
# at the end the recursivly divided and sorted arrays are merged
def quick_sort(a):
    if len(a)<=1:
        return a
    p = a[-1]

    L =[x for x in a[:-1] if x<=p]
    R =[x for x in a[:-1] if x>p]
    L=quick_sort(L)
    R=quick_sort(R)
    return  L + [p] + R

print(quick_sort([1,4 -9,0,11,2,1,6,-2]))