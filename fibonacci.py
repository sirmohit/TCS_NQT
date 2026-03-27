def fibo(n):
    a = 0
    b = 1
    while n > 0:
        print(a,end = " ")
        a,b = b, a+b
        n = n-1