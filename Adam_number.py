n=int(input())
sq=0
sq1=0
temp=n
temp1=n
rev=0
rev1=0
sq=n*n
while n:
    d=n%10
    rev=rev*10+d
    n//=10
sq1=rev*rev
while sq1:
    d1=sq1%10
    rev1=rev1*10+d1
    sq1//=10
if rev1==sq:
    print("True")
else:
    print("False")
