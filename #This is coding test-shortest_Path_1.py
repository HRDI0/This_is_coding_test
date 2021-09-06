# 공중 미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 토앻 연결되어 있다. 
# 연결된 2개의 회사는 양방향으로 이동할 수 있다. 도로가 연결되어 있다면 1만큼의 시간으로 이동할 수 있다. 
# A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다. 이때 A는 가능한 한 빠르게 이동하고자 한다. 
# A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

# 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M
# 둘째 줄부터 M + 1번째 줄에는 연결된 두 회사의 번호
# M + 2번째 줄에는 X와 K
# X번 회사에 도달할 수 없다면 -1 출력

# 입력 예시 1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 출력 예시 1
# 3

# 입력 예시 2
# 4 2
# 1 3
# 2 4
# 3 4

# 출력 예시
# -1

from sys import stdin
input = stdin.readline
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1                     #각 회사간 거리는 1이다.
    graph[b][a] = 1                     #각 회사는 서로 연결 되어있다.

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

x,k = map(int,input().split())
if graph[1][k] + graph[k][x] > INF:                     #회사 1번에서 시작해서 k 회사를 거쳐 x회사까지 가는 최단경로
    print(-1)
else: print(graph[1][k] + graph[k][x])


