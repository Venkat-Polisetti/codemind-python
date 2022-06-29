m,n=map(int,input().split())
i=1
gcd=0
for i in range(1,m+1):
    if n%i==0 and m%i==0:
        gcd=i
    i+=1
print(gcd) 