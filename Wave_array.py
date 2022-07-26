n=int(input())
a=list(map(int,input().split()))
h=0
for i in range(0,n-2,2):
    if ((a[i]<a[i+1]) and (a[i+1]>a[i+2])) or ((a[i]>a[i+1]) and (a[i+1]<a[i+2])):
        continue
    else:
        h=1
        break
if h==1:
    print("no")
else:
    print("yes")