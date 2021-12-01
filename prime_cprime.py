from math import *
def fun(n):
    temp=n
    c=0
    ans=0
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return "not a prime"
        while temp:
            d=temp%10
            temp=temp//10
            ans=ans*10+d
        sq1=int(sqrt(ans))
        for i in range(2,sq1+1):
            if ans%i==0:
                return "prime and not a cprime"
            else:
                return "cprime"
num=int(input())
print(fun(num))
