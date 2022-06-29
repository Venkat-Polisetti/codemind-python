n=int(input())
sd=0
pd=1
temp=n
temp1=0
while n!=0:
    d=n%10
    pd=n*n
    n=n//10
    temp1=pd
while pd!=0:
    t=pd%10
    sd+=t
    pd=pd//10
if sd==temp:
    print('Neon Number')
else:
    print('Not Neon Number')