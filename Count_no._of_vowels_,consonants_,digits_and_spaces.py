s=input()
s=s.lower()
sp=0
dc=0
vc=0
cc=0
for i in s:
    if i==' ':
        sp+=1
    elif i>='0' and i<='9':
        dc+=1
    elif i in 'aeiou':
        vc+=1
    elif i not in 'aeiou':
        cc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",dc)
print("White spaces:",sp)