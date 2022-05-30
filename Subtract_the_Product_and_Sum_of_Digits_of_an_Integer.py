n=int(input())
sd=0
pd=1
while n:
    d=n%10
    sd+=d
    pd*=d
    n//=10
print(abs(pd-sd))