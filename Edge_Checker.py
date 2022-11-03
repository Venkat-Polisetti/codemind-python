x,y=map(int,input().split())
if(abs(x-y)==1):
    print("Yes")
elif((x==1 and y==10) or (x==10 and y==1)):
    print("Yes")
else:
    print("No")