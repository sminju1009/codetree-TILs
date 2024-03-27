n, m = map(int, input().split())

dic = dict()

for i in range(n):
    string = input()
    dic[string] = str(i + 1)

for _ in range(m):
    query = input()
    if query.isdigit():  # 만약 쿼리가 숫자인 경우
        number = int(query)
        for key, value in dic.items():
            if value == query:
                print(key)
                break
    else:  # 만약 쿼리가 문자열인 경우
        print(dic.get(query, 'None'))