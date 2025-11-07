from typing import List
def bi_search(arr: List, t):
    if not isinstance(arr, List):
        print("Wrong input format. Input must be an array")
        return
    l = 0
    r = len(arr) - 1

    # this formula is used to avoid integer overflow
    #since l+r may result in a larger number than what int can take..

    while l<=r:
        mid = l + ((r - l) // 2)
        if arr[mid] == t:
            print(f"{t} was found at {mid}")
            return
        elif t<arr[mid]:
            r=mid-1
        else:
            l=mid+1

    print(f"{t} is not in the array.")
    return


def rec_bi_search(arr, l, r, t):
    if not isinstance(arr, List):
        print("Wrong input format. Input must be an array")
        return
    if l>r:
        print(f"{t} is not in the array. ***")
        return
    mid = l + ((r - l) // 2)
    if arr[mid] == t:
        print(f"{t} was found at {mid} ***")
        return
    elif t < arr[mid]:
        rec_bi_search(arr,l,mid-1,t)
    else:
        rec_bi_search(arr,mid+1,r,t)

a = [-11,-2,0,2,7,9,10,44,56,66]
bi_search(a, 66)

rec_bi_search(a,0, len(a)-1,66)