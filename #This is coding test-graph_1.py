# #팀결성
# 학교에서 학생들에게 0번부터 N번까지의 번호를 부여했다. 
# 처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N+1 개의 팀이 존재한다. 
# 이때 선생님은 "팀 합치기" 연산과 "같은 팀 여부 확인" 연산을 사용할 수 있다.

# 1. "팀 합치기" 연산은 두 팀을 합치는 연산이다.

# 2. "같은 팀 여부 확인" 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.
 
# 선생님이 M개의 연산을 수행할 수 있을 때, "같은 팀 여부 확인" 연산에 대한 연산 결과를 출력하는 프로그램을 작성



# 입력 조건
# 첫째 줄에 N,M이 주어진다. M은 입력으로 주어지는 연산의 개수이다
# 다음 M개의 줄에는 각각의 연산이 주어진다.
# "팀 합치기" 연산은 0 a b  형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
# "같은 팀 여부 확인" 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다.
# a와 b는 N이하의 양의 정수이다.

# 출력 조건
# "같은 팀 여부 확인"연산에 대하여 한 줄에 하나씩 YES 혹은 NO 로 결과를 출력


from sys import stdin
input = stdin.readline

n,m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = parent[a]
    b = parent[b]

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]

for _ in range(m):
    comend, a, b = map(int, input().split())
    if comend == 0:
        union_parent(parent, a, b)
    elif comend == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else: print('NO')

