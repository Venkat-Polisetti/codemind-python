n=int(input())
a=list(map(int,input().split()))
c=0
k=0
t=0
for i in range(n):
    c=0
    for j in range(i+1,n):
        if a[j]>a[i] and i!=j:
            c+=1
            break
        else:
            c+=1
        if j==n-1:
            c=0
    print(c,end=' ')