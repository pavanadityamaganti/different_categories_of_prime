from math import *
def s_r(numb):
    return int(sqrt(numb))
def fun(n):
    sq=s_r(n)
    for i in range(2,sq+1):
        if n%i==0:
            return "not a prime"
    while n:
        d=n%10
        n=n//10
        sq1=s_r(d)
        for i in range(2,sq1+1):
            if d%i==0:
                return "prime not a mega prime"
    else:
        return "mega prime"
num=int(input())
print(fun(num))
