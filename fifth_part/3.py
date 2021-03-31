def xor(x, y):
    return x^y

a, b = input().split()
a = int(a)
b = int(b)
if xor(a,b) == True:
    print(1)
else:
    print(0)