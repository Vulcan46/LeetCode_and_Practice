def get_superset(i):
    if i==n:
        #appends a copy of the temporary result.
        res.append(temp_res[:])
        return
    # do not add curr element:
    get_superset(i+1)

    # add current element:
    temp_res.append(arr[i])
    get_superset(i+1)
    # the sub-problem for the next element is created. Now we will remove the element.
    # it will be added to the final res when we reach final index.
    temp_res.pop()

arr = [1,3,5,7]
res, temp_res = [], []
n = len(arr)
get_superset(0)
print(res)

