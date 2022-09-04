n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in range(a,b+1):
    if i in m:
        k.append(i)
if k==[]:
    print("-1")
else:
    print(min(k))