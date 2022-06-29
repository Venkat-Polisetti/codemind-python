x=int(input())
k=0
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        k=k+i
print(k)