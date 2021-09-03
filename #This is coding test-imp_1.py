#상하좌우
#N x N 지도가 있다. 이때 무조건 첫 번째 타일에서 시작하며 좌표는 1,1 이다.
#첫 번째 줄에 N이 주어지며 두 번째 줄에는 L, R, U, D로 이루어진 명령어가 입력된다.
#각각 LEFT, RIGHT, UP, DOWN이며 한칸씩 이름 방향대로 이동한다. 
#만약 이동 중 지도 끝을 넘게 되면 해당 명령은 무시한다.
#명령이 끝났을 때에 좌표를 출력하라.

n = int(input())
commands = input().split()
x, y = 1,1
movement = ['L','R','U','D']
y_stance = [-1,1,0,0]
x_stance = [0,0,-1,1]
for command in commands:
    for i in range(len(movement)):
        if command == movement[i]:
            nx = x + x_stance[i]
            ny = y + y_stance[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny
print(x,y)