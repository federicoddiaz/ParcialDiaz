def  2fib(n):
    a,b=0,1
    while a<n:
        print(a, end=' ')
        a,b=b,a+b
    print()
2fib(1000)
