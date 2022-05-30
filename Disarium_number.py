n=int(input())
temp=n
temp1=n
sum=0
c=0
while n:
    d=n%10
    c+=1
    n//=10
while temp:
    d=temp%10
    sum+=pow(d,c)
    c=c-1
    temp//=10
if sum==temp1:
    print("True")
else:
    print("False")
    