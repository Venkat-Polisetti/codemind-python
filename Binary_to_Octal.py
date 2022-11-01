for i in range(int(input())):
    s=int(input())
    s=str(s)
    s='0b'+s
    b=int(s,2)
    t=oct(b)
    t=str(t)
    print(t[2:])