n=int(input())
a=list(map(int,input().split()))
k=sum(a)
avg=k//n
if avg in a:
    print("True")
else:
    print("False")