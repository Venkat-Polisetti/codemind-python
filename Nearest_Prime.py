t=int(input())
v1=0
v2=0
for s in range(t):
    a=int(input())
    b=a
    temp=a
    while a>1:
        for j in range(2,int(a**0.5)+1):
           if a%j==0:
                break
        else:
         v1=a
         break
        a=a-1
    while temp:
        for j in range(2,int(temp**0.5)+1):
            if temp%j==0:
                break
        else:
            v2=temp
            break
        temp+=1
    if (abs(v1-b))>(abs(b-v2)):
        print(v2)
    else:
        print(v1)