from math import *
def sqr(n):
    sq=int(sqrt(n))
    return sq
def isprime(n):
    if n==1:
        return False
    sq=sqr(n)
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
def fun(n):
    if n==2:
        return "it is a Prime not a good prime"
    if n==3:
        return "it is a prime not a good prime"
    if isprime(n):
        print("prime")
        i=2
        while True:
            if isprime(n-i):
                pp=n-i
                break
            i+=2
        i=2
        while True:
            if isprime(n+i):
                np=n+i
                break
            i+=2
        a=np-n
        b=n-pp
        if a==b:
            return "balanced prime"
        else:
            return "not a balanced prime"
    else:
        return "not a prime"
    
num=int(input())
print(fun(num))
