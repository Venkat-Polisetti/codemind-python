n=int(input())
a=list(map(int,input().split()))
k=[]
max1=0
for i in a:
    if len(str(abs(i)))>max1:
        max1=len(str(abs(i)))
for i in a:
    if len(str(abs(i)))==max1:
        k.append(i)
print(*sorted(k))