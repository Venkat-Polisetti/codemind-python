n=int(input())
a=list(map(int,input().split()))
c=0
k=0
if n<3:
    print("no")
else:
    for i in range(0,n-2,1):
        if (a[i]+a[i+1])==a[i+2]:
            c+=1
        else:
            k=1
            print("no")
            break
    if k==0:
        print("yes")