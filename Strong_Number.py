n=int(input())
temp=n
pd=1
sum=0
while n:
    d=n%10
    for i in range(1,d+1):
        pd*=i
    sum+=pd
    n//=10
    pd=1
if temp==sum:
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")