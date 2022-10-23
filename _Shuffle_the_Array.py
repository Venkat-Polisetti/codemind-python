n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
f=[]
for i in range(n//2):
    e.append(a[i])
for i in range(n//2,n):
    o.append(a[i])
for i in range(len(e)):
    f.append(e[i])
    f.append(o[i])
print(*f)
