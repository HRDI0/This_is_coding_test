# 볼링공 고르기

# a, b 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다.
# 볼링공을 총 n개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여됩니다.
# 또한 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주 합니다. 볼링 공의 무게는 1부터 m까지 자연수의 형태로 존재합니다.
# 예를 들어 n이 5이고 m이 3이면 각각의 무게가 차례대로 1,3,2,3,2일 때 각 공의 번호가 차례대로 1~5번까지 부여됩니다.
# 이때 두 사람이 고를 수 있는 볼링공 번호의 조합을 구하면 다음과 같습니다.

# (1, 2) (1, 3) (1, 4) (1, 5) (2, 3) (2, 5) (3, 4) (4, 5)

# 결과적으로 두사람이 공을 고르는 경우의 수는 8가지 입니다. 
# n개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.

# 중복 허용 경우의 수.
# 무게가 a인 공의 개수 * 무게가 a가 아닌 공의 개수 = 무게가 a인 공을 선택 했을 때 조합이 될수 있는 경우의 수

n,m = map(int, input().split())
weight_list = list(map(int, input().split()))

# result = 0
# for i in range(len(weight_list)):
#     for j in range(len(weight_list)):
#         if i != j and weight_list[i] != weight_list[j]:
#             result +=1
# print(result//2)
result = 0
w = [0] * (m +1)     #무게가 1부터 m까지인 공들의 개수를 센다.
for ball in weight_list:
    w[ball] +=1

for i in range(1,m+1):
    n -= w[i]
    result += n * w[i]
print(result)

