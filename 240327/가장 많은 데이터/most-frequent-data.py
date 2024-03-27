n = int(input())
dic = dict()
for _ in range(n):
    a = input()
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

maxi = 0
for key, value in dic.items():
    if dic[key]>maxi:
        maxi = dic[key]

print(maxi)