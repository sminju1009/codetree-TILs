def dfs(level, start):
    if level == m:
        print(*answer)
        return
    for i in range(start, n):
        answer.append(arr[i])
        dfs(level + 1, i + 1)
        answer.pop(-1)

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
answer = []

dfs(0, 0)