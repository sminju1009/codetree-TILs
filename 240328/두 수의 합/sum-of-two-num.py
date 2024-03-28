n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if i!=j and arr[i]+arr[j]==m:
                cnt += 1

print(cnt)