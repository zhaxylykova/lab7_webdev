import math
n = int(input())
i = 2
min_del = 1
sqrt_n = math.sqrt(n)
while i <= sqrt_n:
    if n % i == 0:
        min_del = i
        break
    i += 1

if min_del == 1:
    print(n)
else:
    print(min_del)    
    