t=int(input())
for i in range(t):
    a=int(input())
    c=0
    for i in range(1,int(a**0.5)+1):
        if (i*i)==a:
            print("True")
            c+=1
            break
    if c==0:
        print("False")