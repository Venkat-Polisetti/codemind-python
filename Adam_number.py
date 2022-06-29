n=int(input())
rev=0
sd=0
d=n*n
while n:
    k=n%10
    n=n//10
    rev=rev*10+k
s=rev*rev
while s:
    a=s%10
    s=s//10
    sd=sd*10+a
if sd==d:
    print("True")
else:
    print('False')