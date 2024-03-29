# 뱀 출처다국어
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	128 MB	37918	15123	10014	38.099%
# 문제
#  'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 
#  뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 
# 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 
# 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

# 출력
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.



from collections import deque
from sys import stdin
input = stdin.readline

board = int(input())            #보드 크기
board_list = [[0]*(board+2) for _ in range((board+2))]
apple = int(input())            #사과 개수
location = deque()
for _ in range(apple):
    location.append(tuple(map(int,input().split())))

while location:
    ax,ay = location.popleft()
    board_list[ax][ay] = 1

num = int(input())      #방향 변환 횟수
turn = deque()
for _ in range(num):
    input_data = input().split()
    turn.append((int(input_data[0]),input_data[1]))      #n초 후 x 방향으로 이동 (L = 왼쪽, D = 오른쪽)
turn.append((1,'D'))
# #중요!
# 아래에 알고리즘에서는 action이라는 변수를 늘려가며 turn의 인덱스를 확인한다.
# 만약 뱀이 죽지않고 turn의 시간보다 더 오래 살게 되면 action 변수가 turn의 인덱스를 넘게 되어
# 인덱스 에러가 난다. 리스트나 큐같은 자료구조를 확인하는 인덱스 변수의 범위를 잘 정해놓아야 한다.
#.

# 방향 정보를 입력 받을 때, 시간 정보가 섞여서 들어 올수 있으니 시간 기준 정렬을 하는게 좋으나, 
# 현재 문제에서는 시간순으로 입력되는 것으로 보여 정렬하지 않고 진행한다.

# 뱀의 초기 위치 = (0,0)
# 뱀의 초기 길이 = 1
# 뱀의 초기 방향 X축 으로 +1만큼 이동 (행렬에서는 열을 따라 +1씩 이동.)

dx = [0,1,0,-1]     #동남서북
dy = [1,0,-1,0]
direction = 0       #방향 전환을 위한 인덱스 번호
time = 0            #진행하는 시간
action = 0          #방향 전환할 데이터를 뽑는 플래그
x,y = 1,1           #처음 위치
board_list[x][y] = 2        #뱀 표시
snake = deque()             #뱀 길이
snake.append((x,y))
while True:
    t, dr = turn[action][0], turn[action][1]
    if time == t:
        action+=1
        if dr == 'L':
            direction = (direction-1)%4
            nx = x + dx[direction]
            ny = y + dy[direction]
        elif dr == 'D':
            direction = (direction+1)%4
            nx = x + dx[direction]
            ny = y + dy[direction]
        if 1<=nx and nx<= board and 1<=ny and ny<= board and board_list[nx][ny] != 2:
            snake.append((nx,ny))   #맵의 끝이 아니고 뱀 몸통이 아니라면 몸을 늘려 1칸 전진
            if board_list[nx][ny] == 1:     #전진한 칸이 사과라면
                board_list[nx][ny] = 2      #몸길이를 1칸 늘림
            else:
                board_list[nx][ny] = 2
                px,py = snake.popleft()
                board_list[px][py] = 0
            x,y = nx,ny
            time +=1
        else:
            time+=1
            break
    else:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1<=nx and nx<= board and 1<=ny and ny<= board and board_list[nx][ny] != 2:
            snake.append((nx,ny))   #맵의 끝이 아니고 뱀 몸통이 아니라면 몸을 늘려 1칸 전진
            if board_list[nx][ny] == 1:     #전진한 칸이 사과라면
                board_list[nx][ny] = 2      #몸길이를 1칸 늘림
            else:
                board_list[nx][ny] = 2
                px,py = snake.popleft()
                board_list[px][py] = 0
            x,y = nx,ny            
            time+=1
        else:
            time+=1
            break
print(time)
            
