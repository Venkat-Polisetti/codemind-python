n=int(input())
a=list(map(int,input().split()))
t=[]
for i in a:
    i=str(i)
    t.append(len(i))
for i in a:
    if len(str(i))==max(t):
        print(i,end=' ')