'''vow=['a','e','i','o','u']
a=list(input())
b=[a[0]]
c=0
for i in range(1,len(a)):
    if(b[c] in vow)and(a[i] in vow):
        continue
    elif(b[c] not in vow)and(a[i] not in vow):
        continue
    else:
        b.append(a[i])
        c+=1
s=''
for i in b:
    if i in vow:
        s+='V'
        continue
    s+='C'
print(s)'''
s=input()
v='aeiou'
y=''
x=''    #whereabouts
ans=''         #cvcvcvc
for i in range(len(s)):
    if s[i] not in v:  
        if len (y)!=0:
            ans+='V'
            y=''
        x+=s[i]
    else:
        if len(x)!=0:
            x=''
            ans+='C'
        y+=s[i]
if(len(x)!=0):
    ans+='C'
elif(len(y)!=0):
    ans+='V'
print(ans)
