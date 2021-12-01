def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def is_coprime(x,v):
    return gcd(x,y)==1
num1=int(input())
num2=int(input())
print(gcd(num1,num2))
