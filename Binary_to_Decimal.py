def binaryToDecimal(binary):
	binary1 = binary
	deci, i, n = 0, 0, 0
	while(binary != 0):
		dec = binary % 10
		deci = deci + dec * pow(2, i)
		binary = binary//10
		i += 1
	print(deci)
q=int(input())
for i in range(q):
    n=int(input())
    binaryToDecimal(n)
