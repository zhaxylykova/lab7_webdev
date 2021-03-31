n = int(input())
array = list(map(int,input().strip().split()))[:n]
for i in range(n):
    if array[i] % 2 == 0:
        print(array[i], end=" ")