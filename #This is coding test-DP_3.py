#DP
#문제
# N가지 종류의 화폐가 있다. 화폐들의 개수를 최소한으로 이용해서 가치의 합이 M원이 되도록 만들어라. 각 화폐는 몇 개라도 사용할 수 있다.

# a. 예를 들면.
# 2원, 3원 단위의 화폐가 있을 때 15원을 만들기 위해서는 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수다.

# b. 입력 조건
# 첫째 줄에 N, M이 주어진다
# 1 <= N <= 100
# 1 <= M <= 10,000
# 이후 N개 줄에 각 화폐의 가치가 주어진다.
# 화폐의 가치는 10,000보다 작거나 같은 자연수
# c. 출력 조건
# 첫째 줄에 경우의 수 X를 출력한다.
# 불가능할 때는 -1을 출력한다.

from sys import stdin

n,m = map(int, input().split())
coin_list = [int(stdin.readline()) for _ in range(n)]

dp = [10001] * (m+1)
dp[0] = 0
for coin in coin_list:
    for money in range(coin,len(dp)):
        if dp[money - coin] != 10001:
            dp[money] = min(dp[money],dp[money - coin] + 1)

print(dp[m] if dp[m] < 10001 else -1 )