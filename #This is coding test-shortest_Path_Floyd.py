import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 각 노드에 연결 되어 있는 노드에 대한 정보를 담는 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]       #그래프를 표현한2차원 리스트로 구성

for a in range(1, n+1):                             #자기 자신과의 거리 0처리
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#모든 노드사이의 거리 (간선길이) 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())       # a 에서 b 로 가는 비용이 c 이다.
    graph[a][b] = c

#점화식의 따라 플로이드 워셜 알고리즘 수행 D_ab = min(D_ab,D_ak + D_kb)
# a에서 b로 가는 거리는 a와 b를 직접 가는 거리와 a - k - b 같이 k를 거쳐 가는 거리중 더 짧은 거리로 정한다.
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
    print()
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INF")
        else:
            print(graph[a][b],end = ' ')