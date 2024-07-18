from collections import deque

def dfs(level):
    if level==m:
        return
    for y, x in dots:
        index = dots.index((y, x))
        if v_dots[index] == 0:
            bfs(y, x)
            v_dots[index] = 1
            dfs(level+1)
            v_dots[index] = 0

def bfs(y, x):
    q = deque()
    q.append((y, x, 1))
    visited[y][x] = 1

    while q:
        y, x, level = q.popleft()
        for dy, dx in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ny, nx = dy+y, dx+x
            if 0<=ny<n and 0<=nx<n and arr[ny][nx]!=1 and (visited[ny][nx]==0 or visited[ny][nx]>level):
                q.append((ny, nx, level+1))
                visited[ny][nx] = level+1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)] # 방문 표시 배열
dots = [] # 병원을 받을 배열
ans = 0 # 바이러스 없애는데 걸리는 시간의 최솟값 구하기

for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            dots.append((i, j))
v_dots = [0] * len(dots) # dfs 함수에서 이용할 방문 배열 체크

dfs(0)

for i in range(n):
    for j in range(n):
        if (arr[i][j]==0 or arr[i][j]==2) and visited[i][j]==0:
            ans = -1
            break
        ans = max(visited[i][j], ans)

print(ans)