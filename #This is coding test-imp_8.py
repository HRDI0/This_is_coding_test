# 문제 설명
# 고고학자인 "튜브"는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 
# 그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 
# 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 
# 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

# 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 
# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 
# 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
# lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
# M은 항상 N 이하입니다.
# key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
# 0은 홈 부분, 1은 돌기 부분을 나타냅니다.

# 입출력 예
#               key	                                      lock	                        result
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	        [[1, 1, 1], [1, 1, 0], [1, 0, 1]]       	true

import copy
def turnkey(key):
    temp = copy.deepcopy(key)
    n = len(key)
    for i in range(n):
        for j in range(n):   
            key[j][n-i-1] = temp[i][j]
    return key

def extend_lock(input_key, input_lock):
    #n, m = len(input_key), len(input_lock)
    #extend = [[0]*((n*2)+m)]*((n*2)+m)             
    #이유는 이해가 안가지만 이렇게 만들면 0번줄과 나머지 줄의 인덱스가 동기화되어 있다. [0][1]변경시 [n][1]까지 다 바뀜 
    m = len(input_lock)
    extend = [[0]*(m*3) for _ in range(m*3)]
    for i in range(m):
        for j in range(m):
            extend[i+m][j+m] = input_lock[i][j]
    return extend

def check_lock(iex_lock):
    m = len(iex_lock) //3
    for lx in range(m,m*2):
        for ly in range(m,m*2):
            if iex_lock[lx][ly] !=1:
                return False
    return True


def solution(key, lock):
    answer = False
    n,m = len(key),len(lock)
    ex_lock = extend_lock(key,lock)
    temp = copy.deepcopy(ex_lock)
    for i in range(4):      
        key = turnkey(key)
        for lx in range(m*2):
            for ly in range(m*2):
                for kx in range(n):
                    for ky in range(n):
                        ex_lock[lx+kx][ly+ky] += key[kx][ky]
                if check_lock(ex_lock):
                    answer = True
                ex_lock = copy.deepcopy(temp)
    return answer
    
key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
print(solution(key,lock))