n=int(input())
c=0
for i in range(1,int(n**0.5)+1):
    if n==i*i:
        print("True")
        c+=1
        break
if c==0:
    print("False")