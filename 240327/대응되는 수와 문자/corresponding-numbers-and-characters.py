n, m = map(int, input().split())

# 딕셔너리를 사용하여 숫자와 문자열 간의 대응 관계를 저장
number_to_string = {}
string_to_number = {}

for i in range(1, n + 1):
    s = input().strip()
    number_to_string[i] = s
    string_to_number[s] = i

for _ in range(m):
    query = input().strip()
    if query.isdigit():  # 만약 쿼리가 숫자인 경우
        number = int(query)
        if number in number_to_string:  # 딕셔너리에 해당 숫자가 존재하는지 확인
            print(number_to_string[number])  # 대응되는 문자열 출력
    else:  # 만약 쿼리가 문자열인 경우
        if query in string_to_number:  # 딕셔너리에 해당 문자열이 존재하는지 확인
            print(string_to_number[query])  # 대응되는 숫자 출력