import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
#시작 노드 입력.
start = int(input())
# 각 노드에 연결 되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]       #구현하기 쉽도록 노드 번호 = 리스트 번호가 되도록 n+1 하여 만든다.
#최단 거리 테이블 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())       # a 에서 b 로 가는 비용이 c 이다.
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:            #큐가 비어있지 않다면
        dist, now  = heapq.heappop(q)     # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:         #이미 처리된 노드라면 무시 
            continue
        for i in graph[now]:        #현재 노드와 연결된 인접한 노드 확인
            cost = dist +i[1]       #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    #접근이 불가능한 노드가 있는 경우
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])      # 도달할 수 있는 거리를 출력.
