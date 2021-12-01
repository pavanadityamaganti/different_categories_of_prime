from math import *
def fun(n):
    c=0
    ans=0
    sq=int(sqrt(n))
    for i in range(2,sq):
        if n%i==0:
            c+=1
        else:
            return "not a prime"
    if c==1:
        ans=n//2
        print(ans)
        if ans//2==0:
            return "not a safe prime"
        else:
            return "safe prime"
num=int(input())
print(fun(num))
