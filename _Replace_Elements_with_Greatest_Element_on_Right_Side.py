n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    a[i]=max(a[i+1:n])
for i in range(n):
    a[n-1]=-1
for i in a:
    print(i,end=" ")