n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    res = k - arr[i]
    if res in arr:
        cnt += 1

print(cnt//2)