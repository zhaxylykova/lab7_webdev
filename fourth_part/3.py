n = int(input())
array = list(map(int,input().strip().split()))[:n]
cnt = 0
for i in range(1,n):
    if array[i] > array[i-1]:
        cnt += 1
print(cnt)