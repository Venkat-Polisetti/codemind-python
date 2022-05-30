a=int(input())
b=int(input())
sum=0
sum1=0
for i in range(1,a):
    if a%i==0:
        sum+=i
for k in range(1,b):
    if b%k==0:
        sum1+=k
if sum1==a and sum==b:
    print("Amicable")
else:
    print("Not Amicable")