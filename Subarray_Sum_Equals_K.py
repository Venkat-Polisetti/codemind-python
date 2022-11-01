n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i+1,n+1):
        sum2=0
        for f in range(i,j):
            sum2+=a[f]
        if(sum2==k):
            c+=1
print(c)