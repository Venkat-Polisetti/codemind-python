s=input()
s=s.split()
sum1=0
sum2=0
for i in s:
    sum1+=ord(min(i))
    sum2+=ord(max(i))
print(abs(sum1-sum2))