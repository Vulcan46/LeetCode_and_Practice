# the most basic sorting algo O(n^2)
# you keep travesing until you perform no swaps, that is when flag becomes false.
def bubble_sort(a):
    flag = True
    n = len(a)
    while flag:
        flag = False
        for i in range(1,n):
            if a[i]<a[i-1]:
                flag = True
                a[i], a[i-1] = a[i-1], a[i]
    return a

print(bubble_sort([1,4 -9,0,11,2,1,6,-2,-10,39]))