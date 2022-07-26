n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if len(str(abs(i)))==m:
        c+=1
print(c)