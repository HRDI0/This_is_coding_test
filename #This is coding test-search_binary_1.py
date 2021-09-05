#부품찾기
#부품 목록중에 필요한 부품이 있는지 확인한다.
#단, 부품 목록의 길이 N은 1<= N <= 1,000,000 이다.
# 필요 부품 목록 M의 길이는 1<= M <= 100,000 이다.
from sys import stdin
n = int(stdin.readline())
n_list = list(map(int,stdin.readline().split()))    #부품 목록

m = int(stdin.readline())
m_list = list(map(int,stdin.readline().split()))    #필요 부품 목록

def bs(data_list, target, start, end):              #이진 탐색 - 부품 목록의 길이가 최대 100만이기 때문에 이진 탐색 사용
    if start > end:
        return None
    mid = (start + end) //2
    if data_list[mid] == target:
        return mid
    elif data_list[mid] > target:
        return bs(data_list, target, start, mid -1)
    elif data_list[mid] < target:
        return bs(data_list, target, mid +1, end)

n_list.sort()                                      #이진탐색할 리스트는 정렬 되어 있어야 한다.
for parts in m_list: 
    result = bs(n_list, parts, 0, len(n_list) - 1)
    if result != None:
        print('YES',end = ' ')
    else: print('NO', end = ' ')