# it is a very useful simplification technique
# it builds a call stack, recusion tree
# complexity very BAD! 2^(height of the tree)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(40)) # 2^40