x=int(input())
k=0
l=list(map(int,input().split()))
for i in range(x):
    if i%2==0:
        k=k+l[i]
print(k)