# 문제
# 현재 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 
# 이때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 예시
# 10

from collections import deque

n,m = map(int, input().split())
maize = []
for _ in range(n):
    maize.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maize[nx][ny] == 0:
                continue
            if maize[nx][ny] == 1:
                maize[nx][ny] = maize[x][y] +1
                queue.append((nx,ny))
    return maize[-1][-1]

print(bfs(0,0))