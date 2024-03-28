n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = dict()
cnt = 0

for i in range(n):
    res = k - arr[i]
    if res in dic:
        cnt += dic[res]
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

print(cnt)