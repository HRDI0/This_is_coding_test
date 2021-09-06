#위상 정렬
from collections import deque
from sys import stdin
input = stdin.readline

#노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
#진입 차수 초기화
indegree = [0] *(v+1)
#각 노드에 연결 된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)          #노드 a 에서 b로 이동가능
    #진입차수 1 증가
    indegree[b] +=1

#위상 정렬 함수
def topology_sort():
    result = [] #알고리즘 수행 결과를 담을 리스트
    q = deque() #큐 기능을 위한 deque사용

    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        #해당 노드와 연결된 노드들의 진입차수에서 -1을 함
        for n in graph[now]:
            indegree[n] -=1
            #새롭게 진입차수가 0이된 노드를 큐에 삽입
            if indegree[n] == 0:
                q.append(n)
    for r in result:
        print(r,end=' ')
topology_sort()