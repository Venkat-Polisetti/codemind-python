n=int(input())
pd=1
c=0
for i in range(n):
    if (i*(i+1))==n:
        print("YES")
        c+=1
        break
if c==0:
    print("NO")