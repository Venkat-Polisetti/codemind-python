n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=[]
for i in a:
    if i in b and i not in k:
        k.append(i)
for i in b:
    if i in a and i not in k:
        k.append(i)
print(*k)