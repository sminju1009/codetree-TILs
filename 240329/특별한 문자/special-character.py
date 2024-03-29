a = input()
dic = dict()

for i in range(len(a)):
    if a[i] not in dic:
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1

ans = []
for key in dic:
    if dic[key]==1:
        ans.append(key)

if ans==[]:
    print("None")
else:
    print(ans[0])