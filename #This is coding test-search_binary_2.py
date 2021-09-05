#떡볶이 떡 만들기
#서로 다른 길이의 떡을 한줄로 나열하여 한번에 절단했을 때, 손님이 원하는 길이만큼의 떡을 잘라서 제공해야한다.
#떡의 길이는 최대 10억이며, 손님이 요청한 떡의 길이는 최대 20억이다.
from sys import stdin
n,m= map(int, stdin.readline().split())             #떡의 개수와 손님이 요청한 떡의 총 길이
n_list = list(map(int,stdin.readline().split()))    #떡 각각의 길이


def bs(data_list, target, start, end):              #이진 탐색 - 요구 길이와 리스트 길이가 각각 10억, 20억 단위기때문에
    while start <= end:
        request = 0
        mid = (start + end) //2
        for line in data_list:
            if line > mid:
                request += (line - mid)
        if request == target:
            return mid
        elif request < target:
            end = mid -1
        elif request > target:
            start = mid + 1

print(bs(n_list, m, 0, max(n_list)))
