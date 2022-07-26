def prime(k):
    if k==1:
        return 0
    else:
        for j in range(2,int(k**0.5)+1):
            if k%j==0:
                return 0
        else:
            return 1
         
n=int(input())
a=list(map(int,input().split()))
min1=a.index(min(a))
max1=a.index(max(a))
c=0
if min1<max1:
    for i in range(min1,max1+1):
        if prime(a[i]):
            c+=1
else:
    for i in range(max1,min1+1):
        k=a[i]
        if prime(k):
            c+=1
print(c)