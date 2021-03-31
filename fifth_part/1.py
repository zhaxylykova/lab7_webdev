def minimal(a,b,c,d):
    x = min(a,b,c,d)
    return x

a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print(minimal(a,b,c,d))
