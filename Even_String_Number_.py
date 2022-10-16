s=list(input())
odd,even=[],[]
for i in s:
    if i>='0' and i<='9':
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
if(len(even)==0):
    print(-1)
else:
    even=list(sorted(set(even)))
    odd=list(sorted(set(odd)))
    l=even[0]
    even.remove(l)
    f=list(reversed(sorted(odd+even)))
    f.append(l)
    print(*f,sep='')