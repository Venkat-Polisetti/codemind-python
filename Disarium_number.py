import math
n=int(input())
temp=n
temp1=n
sum=0
k=0
c=0
while n!=0:
    d=n%10
    c+=1
    n=n//10
while temp!=0:
    d=temp%10
    k=pow(d,c)
    c-=1
    sum+=k
    temp=temp//10
if sum==temp1:
    print('True')
else:
    print('False')
    