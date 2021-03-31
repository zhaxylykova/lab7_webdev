n = int(input())
array = list(map(int,input().strip().split()))[:n]
found = False
for i in range(1,n):
    if array[i] * array[i-1] > 0:
        found = True
        break
    else:
        found = False
if found == True:
    print("YES")
else:
    print("NO")