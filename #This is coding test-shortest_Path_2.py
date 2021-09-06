# 메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다. 
# 각 도시의 번호와 통로가 설치도어 있는 정보가 주어졌을 때, 
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 
# 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

# 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
# 둘째 줄부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X(특정 도시), Y(다른 특정 도시), Z(메시지가 전달되는 시간)

# 입력 예시
# 3 2 1
# 1 2 4
# 1 3 2

# 출력 예시
# 2 4

import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9)
node, line, start = map(int,input().split())
graph = [[]for _ in range(node+1)]
distance =[INF] * (node +1)

for _ in range(line):
    from_a, to_b, time = map(int, input().split())
    graph[from_a].append((to_b,time))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

count = 0
max_dist = 0
for d in distance:
    if d != INF:
        count +=1
        #max_dist += d
        max_dist = max(max_dist,d)      #왜 max()이느냐. 전보를 동시에 전달하기때문에 a -> b 2초 a-> c 4초 라면
                                        #a -> c 까지 4초동안 2초 걸리는 a->b는 이미 처리되기 때문이다.
                                        #그렇기 때문에 동시에 처리되는 문제의 경우 총 거리 = 최대 거리가 될수 있는것
                                        #문제를 잘 읽자..
print(count - 1,max_dist,sep=' ')