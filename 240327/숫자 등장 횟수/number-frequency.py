# 원소 개수 n, 질의의 수 m
n, m = map(int, input().split())
arr = list(map(int, input().split()))
lst = list(map(int, input().split()))

dic = dict()

for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

key = []
for i in range(m):
    if lst[i] not in dic:
        key.append(0)
    else:
        key.append(dic[lst[i]])

print(*key)