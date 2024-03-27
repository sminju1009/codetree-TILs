n = int(input())
dic = dict()
for _ in range(n):
    a = input()
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

maxi = 0
for i, elem in enumerate(dic):
    if maxi<i:
        maxi = i+1

print(maxi)