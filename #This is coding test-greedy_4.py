# 모험가 길드
# 모험가 길드에서 모험가들을 모아 모험가 그룹을 만들려고 한다. 
# 이때 모험가들은 각각 공포도 X를 가지고 있는데 X만큼의 인원이 충족 되지 않으면 위기 상황을 맞이했을 때
# 제대로 대처하지 못한다고 한다. 모험가 길드에서는 모험가들의 공포도를 조사하여 떠날 수 있는 최대의 그룹 수를 알아내려 한다.

# 입력
# 5
# 2 3 1 2 2

# 출력
# 2

from sys import stdin
input = stdin.readline

n = int(input())
peple = list(map(int, input().split()))

peple.sort()
# count = 0
# for p in peple:
#     if len(peple) > p:
#         peple = peple[(p-1):-1]
#         count +=1
# print(count)

count = 0
result = 0
for p in peple:
    count +=1
    if count >= p:
        result +=1
        count = 0
print(result)