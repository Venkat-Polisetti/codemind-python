n=int(input())
temp=n
c=0
rev=0
t=0
h=0
k=0
while n:
    d=n%10
    rev=rev*10+d
    n//=10
for i in range(1,temp+1):
    if temp%i==0:
        c+=1
if c==2:
    t+=1
for s in range(1,rev+1):
    if rev%s==0:
        h+=1
if h==2:
    k+=1
if k>0 and t>0:
    print("circular prime")
elif k==0 and t>0:
    print("prime but not a circular prime")
else:
    print("not prime")