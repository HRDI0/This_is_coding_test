#서로소 집합 알고리즘 개선 코드 / 신장트리(크루스칼 알고리즘)

from sys import stdin
input = stdin.readline


#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면 루트노드를 찾을 때까지 재귀
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선의(union 연산의 개수) 개수 입력 받기
v, e = map(int, input().split())
parent = [0] *(v+1)

#부모 테이블에서 부모 노드를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i
##########################################
# #union 연산을 각각 수행
# for u in range(e):
#     a, b = map(int,input().split())
#     union_parent(parent, a, b)

# #각 원소가 속한 집합 출력
# print('각 원소가 속한 집합 출력')
# for p in range(1,v+1):
#     print(find_parent(parent,p),end=' ')

# print()
# #부모 테이블의 내용 출력
# for i in range(1,v+1):
#     print(parent[i],end=' ')
#############################################


#모든 간선을 담을 변수와 최종 비용을 담을 변수
edges = []
result = 0

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

#간선을 하나씩 확인하며
for line in edges:
    cost,a,b = line
    #사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result +=cost
print(result)