n = int(input())
dic = dict()  # 딕셔너리를 반복문 밖에서 초기화

for _ in range(n):
    arr = input().split()
    command = arr[0]
    if command == 'add':
        key = int(arr[1])  # 키를 정수로 변환
        value = int(arr[2])  # 값도 정수로 변환
        dic[key] = value
    elif command == 'remove':
        key = int(arr[1])  # 키를 정수로 변환
        if key in dic:
            dic.pop(key)
    elif command == 'find':
        key = int(arr[1])  # 키를 정수로 변환
        if key in dic:
            print(dic[key])  # 딕셔너리에서 특정 키에 해당하는 값을 출력
        else:
            print('None')