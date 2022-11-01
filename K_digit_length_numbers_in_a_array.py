n,k=map(int,input().split())
a=list(map(int,input().split()))
#print(k,a)
c=0
for i in a:
    if(len(str(abs(i)))==k):
        c+=1
print(c)