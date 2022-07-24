def sumSquare(n):
    s = dict()
    for i in range(n):
        if i * i > n:
            break
        s[i * i] = 1
        if (n - i * i) in s.keys():
            return True
    return False
n=int(input())
print(sumSquare(n))