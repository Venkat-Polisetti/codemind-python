n=int(input())
a=list(map(int,input().split()))
k=int(input())
t=list(map(int,input().split()))
if(sorted(a)==sorted(t)):
    print(True)
else:
    print(False)