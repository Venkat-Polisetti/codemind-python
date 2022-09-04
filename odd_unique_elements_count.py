n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i not in k and i%2==1:
        k.append(i)
print(len(k))