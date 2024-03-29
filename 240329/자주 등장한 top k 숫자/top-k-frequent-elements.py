n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = dict()
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

dic = dict(sorted(dic.items(), key=lambda x:(x[1], x[0]), reverse=True))

dic = sorted(dic, key=lambda x:dic[x], reverse=True)
print(*dic[:k])

# rint(sorted(dic,key=lambda x:dic[x]))