def fib(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a,b = b,a+b
    
obj = fib(15)
for i in fib(10):
    print(next(obj),end=" ")    # 0 1 1 2 3 5 8 13 21 34
    