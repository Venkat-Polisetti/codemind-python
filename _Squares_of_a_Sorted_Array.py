a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    c.append(i*i)
c.sort()
print(*c)