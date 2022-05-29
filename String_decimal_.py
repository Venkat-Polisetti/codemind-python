t=int(input())
for i in range(t):
    s=input()
    c=0
    for k in s:
        if k>='0' and k<='9':
            c+=1
    if c==len(s):
        print("True")
    else:
        print("False")