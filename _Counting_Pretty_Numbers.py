t=int(input())
for i  in range(t):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        while i:
            d=i%10
            break
        if d==2 or d==3 or d==9:
            c+=1
    print(c)