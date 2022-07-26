n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
   print(len(str(abs(i))),end=' ')