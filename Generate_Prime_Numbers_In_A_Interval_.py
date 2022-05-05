n=int(input())
m=int(input())
for i in range(n+1,m+1):
    for j in range(2,int(i**1/2)+1):
        if(i%j==0):
            break
    else:
        print(i,end='
')