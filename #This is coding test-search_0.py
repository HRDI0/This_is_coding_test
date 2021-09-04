#DFS, BFS
#사전 학습

#스택과 큐

# stack = []      #스택은 별도의 라이브러리가 불필요함. FILO 선입 후출 방식.
# #삽입(5) - 삽입(2) - 삭제() - 삽입(3)
# stack.append(5)
# print(stack)
# stack.append(2)
# print(stack)
# stack.pop()
# print(stack)
# stack.append(3)
# print(stack)

# from collections import deque

# # 큐 구현을 위해 deque() 라이브러리 사용
# queue = deque()
# #삽입(5) - 삽입(3) - 삭제() - 삽입(2)
# queue.append(5)
# print(queue)
# queue.append(3)
# print(queue)
# queue.popleft()
# print(queue)
# queue.append(2)
# print(queue)


#DFS #BFS

def dfs(graph, v, visited):
    #현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque
def bfs(graph, start, visited):
    #현재 노드와 인접한 노드 방문 처리
    queue = deque([start])
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end=' ')
        #해당 원소에 연결된, 아직 방문하지 않은 원소들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph) #총 노드의 개수

print('DFS')
dfs(graph, 1, visited) 
print()

visited = [False] * len(graph) #총 노드의 개수
print('BFS')
bfs(graph,1,visited)