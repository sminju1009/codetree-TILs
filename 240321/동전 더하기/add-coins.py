n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

cnt = 0
for i in range(n):
    cnt += k//arr[i]
    k = k%arr[i]

print(cnt)