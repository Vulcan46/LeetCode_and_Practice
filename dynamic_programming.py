# This is Top Down DP using memoization:
# This approach is useful when we have repeating sub-problems.
# Stores the answers to the sub problems that we have already solved in memory.
# the recursion tree is traversed far less as we do not go the leaf level for every call stack item

def fib_memo(n):
    memo ={0:0,1:1,2:1}
    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1)+f(x-2)
        return memo[x]
    return f(n)

fib = []
def fib_list(n):
    memo = {1:[0],2:[0,1]}
    def f_list(x):
        if x in memo:
            return memo[x]
        if x-1 in memo:
            copy = memo[x-1][:]
        else:
            copy = f_list(x-1)

        copy.append(copy[-2]+copy[-1])

        memo[x] = copy[:]
        return copy
    return f_list(n)

#bottom up
def fib_bottom_up(n):
    prev,curr =0,1
    for i in range(2,n+1):
        prev, curr = curr,prev+curr
    return curr
print(fib_memo(6))

print(fib_list(6))


#THE BEST O(n)
print(fib_bottom_up(6))