n=int(input())
a=0
b=1
c=0
for i in range(c,n-2):
    c=a+b
    if c==n:
        print('True')
        break
    a=b
    b=c
if c>n:
    print('False')