n=int(input())
sq=n*n
k=0
temp=n
while n:
    d=n%10
    k+=1
    n//=10
while sq:
    d=sq%pow(10,k)
    break
if d==temp:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")