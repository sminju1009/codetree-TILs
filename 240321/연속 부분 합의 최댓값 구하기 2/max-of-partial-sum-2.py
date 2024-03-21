n = int(input())
arr = list(map(int, input().split()))

# 원소가 최대일 때 구하기
sum_arr = 0
for i in range(n):
    sum_arr += arr[i]
    if sum_arr<0:
        sum_arr = arr[i]

print(sum_arr)