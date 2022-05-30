n,x=map(int,input().split())
temp=n
temp1=n
c=0
diff=0
while n:
    d=n%10
    c+=1
    n//=10
while temp:
    d=temp%pow(10,x)
    e=temp1//pow(10,(c-x))
    temp//=10
    break
diff=abs(e-d)
print(diff)
