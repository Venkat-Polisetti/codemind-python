for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sum1=0
    c=0
    for i in range(n):
        sum1=0
        for j in range(i+1,n):
            sum1=a[i]+a[j]
            if sum1 in a:
                c+=1
    if c==0:
        print(-1)
    else:
        print(c)