n=int(input())
pd=1
sd=0
while n:
    d=n%10
    pd*=d
    sd+=d
    n//=10
if sd==pd:
    print("Spy Number")
else:
    print("Not Spy Number")