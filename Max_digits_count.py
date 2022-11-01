n=int(input())
a=list(map(int,input().split()))
k=0
max1=0
for i in a:
    if len(str(abs(i)))>max1:
        max1=len(str(abs(i)))
for i in a:
    if len(str(abs(i)))==max1:
       k+=1 
print(k)