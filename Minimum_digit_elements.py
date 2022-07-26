n=int(input())
a=list(map(int,input().split()))
k=min(a)
c=0
for i in a:
    if len(str(i))==len(str(k)):
        c+=1
print(c)