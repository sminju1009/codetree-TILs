from sys import stdin; input = stdin.readline
import heapq

def dijkstra(start=1):
    visited = [False]*(n+1)
    heap = []
    heapq.heappush(heap,(0,start))
    result[start] = 0

    while heap:
        v_cost, via = heapq.heappop(heap)
        if visited[via]: continue
        visited[via] = True

        if result[via] < v_cost: continue
        for next_, cost in adj[via]:
            cost += v_cost
            if result[next_] > cost:
                result[next_] = cost
                heapq.heappush(heap,(result[next_],next_))

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int,input().split())
    adj[s].append((e,w))
    


INF = float("inf")
result = [INF]*(n+1)
dijkstra()


for r in result[2:]:
    print(r) if r!= INF else -1