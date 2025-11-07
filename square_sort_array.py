def square_sort_array(a):
    result = [0]*len(a)
    l = idx = 0
    r = len(a)-1
    while l<=r:
        if abs(a[l]) < abs(a[r]):
            result[idx] = a[r]**2
            idx+=1
            r-=1
        else:
            result[idx] = a[l] ** 2
            idx += 1
            l += 1
    return result[::-1]

arr = [-9,-2,4,5,8,9]

print(square_sort_array(arr))

