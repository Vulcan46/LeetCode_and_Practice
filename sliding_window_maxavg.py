def find_max_avg(arr,k):
    if k > len(arr) or k <= 0:
        return "Error"
    n=len(arr)
    sum = 0
    #initially we simply build the window, i.e. the 4 numbers average.
    for i in range(k):
        sum+=arr[i]
    max_avg = sum / k
    # every time we "slide" the window, we lose the 1st no. and add another
    for i in range(k,n):
        sum+=arr[i]
        sum-=arr[i-k]
        max_avg = max(max_avg, sum/k)

    return  max_avg

a = [2]

print(find_max_avg(a,0))

