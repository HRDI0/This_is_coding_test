# #커리큘럼
# 철수는 온라인으로 컴퓨터공학강의를 듣고 있다.

# 이때 각 온라인강의는 선수강의가 있을 수 있는데, 선수 강의가 있는 강의는 선수 강의를 먼저. 들어야만 해당강의를 들을 수 있다.

# 예를들어 '알고리즘’ 강의의 선수 강의로 '자료구조'가 존재한다면, ‘자료구조를 들은 이후에 ‘알고리즘' 강의를 들을 수 있다.

# 철수는 총 N개의 강의를 듣고자 한다. 모든 강의는 1번부터 N번까지의 번호를 가진다.

# 또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.

# 예를 들어 N=3일 때, 3번강의의 선수 강의로 1번과 2번강의가 있고, 1번과 2번강의는 선수강의가 없다고 가정하자.

# 그리고 각 강의에 대하여 강의 시간이 다음과 같다고 가정하자.

# 1번 강의: 30시간

# 2번 강의: 20시간

# 3번 강의: 40시간


# 이 경우 1번 강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지의 최소 시간은 20시간, 
# 3번 강의를 수강하기까지의 최소 시간은 70시간이다.

# 철수가 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 
# 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.

 

# 입력 조건
# 첫째줄에 철수가 듣고자 하는 강의의 수 N(1≤N≤500)이 주어진다.

# 다음 N개의 줄에는 각 강의의 강의 시간과 그. 강의를 듣기 위해 먼저 들어야하는 강의들의 번호가 자연수로 주어지며, 
# 각 자연수는 공백으로 구분한다. 이때 강의시간은 100,000이하의 자연수이다 .
# 각 강의번호는 1부터 N까지로 구성되며. 각줄은 -1로 끝난다.
 

# 출력 조건
# N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력한다


# 입력 예시
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
 

# 출력 예시
# 10
# 20
# 14
# 18
# 17

from collections import deque
from sys import stdin
import copy
input = stdin.readline

n = int(input())
time = [0] * (n+1) 
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]                          #시간 정보를 time 리스트에 담는다.
    for d in data[1:-1]:
        indegree[i] +=1                         #진입 차수 정보
        graph[d].append(i)                      #노드 d와 연결된 노드 번호를 추가


def topology():
    result = copy.deepcopy(time)            #선수강의 시간을 더하기 위한 리스트
                                            #기존의 time 리스트로 연산할 경우 A를 선수강의로 가지고 있는 
                                            # B 강의의 총 필요 강의시간이 변경될 경우 B강의를 선수강의로 가지고 있지만
                                            # A 강의는 선수 강의로 갖지 않는 강의의 강의 시간도 영향을 받기 때문에 
                                            # 따로 강의 시간을 연산하기 위한 리스트를 만든다.
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for g in graph[now]:
            result[g] = max(result[g], result[now]+time[g]) #이미 g 강의에 선수강의 시간이 더해졌거나
                                                            # now 강의에 선수강의 시간이 더해져 기존 기존보다 강의 시간이
                                                            #늘었을 수 있으므로 둘중 더 큰 시간을 채택한다.
            indegree[g] -=1
            if indegree[g] == 0:
                q.append(g)

    for i in range(1, n+1):
        print(result[i])

topology()