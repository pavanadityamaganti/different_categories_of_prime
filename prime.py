from math import *
def fun(n):
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
num=int(input())
print(fun(num))
