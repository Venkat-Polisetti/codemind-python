t=int(input())
for i in range(t):
    a=int(input())
    temp=a
    rev=0
    while a:
        d=a%10
        rev=rev*10+d
        a//=10
    if rev==temp:
        print("True")
    else:
        print("False")