#DP
#개미 전사
# 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다. 
# 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.

# 입력 예시
# 4
# 1 3 1 5

# 출력 예시
# 8

n = int(input())
n_list = list(map(int, input().split()))

dp = [0] * n

dp[0] = n_list[0]
dp[1] = max(n_list[0],n_list[1])

for i in range(2,n):
    dp[i] = max(dp[i-1],(dp[i-2]+n_list[i]))
print(dp[-1])