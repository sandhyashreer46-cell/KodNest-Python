#count from 5 4 3 2 1
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(5)

#faactorial
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(5))

#fibbonacci series
def fib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(5))

    

    