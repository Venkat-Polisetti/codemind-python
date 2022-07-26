n=int(input())
a=list(map(int,input().split()))
c=0
h=0
for i in range(0,n-2,2):
    if (a[i]<a[i+1]) and (a[i+1]>a[i+2]):
        c+=1
    else:
        h=1
        break
if h==1:
    print("-1")
else:
    print(c)