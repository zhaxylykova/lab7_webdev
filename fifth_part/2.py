def power(a,b):
    x = a ** b
    return x

a, b = input().split()
a = float(a)
b = int(b)
print(power(a,b))