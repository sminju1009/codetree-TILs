n, m = map(int, input().split())

dic = dict()

for i in range(n):
    a = input()
    dic[a] = str(i+1)

for i in range(m):
    a = input()
    for key, value in dic.items():
        if key==a:
            print(value)
        elif value==a:
            print(key)