n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in a:
    if i==b:
        print(a.index(i),len(a)-1-a[::-1].index(b),end=' ')
        c+=1
        break
if c==0:
    print("-1 -1")