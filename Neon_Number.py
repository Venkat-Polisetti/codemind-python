n=int(input())
sq=n*n
sd=0
while sq:
    d=sq%10
    sd+=d
    sq//=10
if sd==n:
    print("Neon Number")
else:
    print("Not Neon Number")