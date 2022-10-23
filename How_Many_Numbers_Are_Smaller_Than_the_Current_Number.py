n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in range(n):
    for j in range(n):
        if a[j]<a[i] and i!=j:
            c+=1
    b.append(c)
    c=0
print(*b)

    