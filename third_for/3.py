import math
a = int(input())
b = int(input())
for i in range(a,b+1):
    z = int(math.sqrt(i))
    if math.sqrt(i) == z:
        print(i, end=" ")
    
   