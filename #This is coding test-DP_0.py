#DP
#1로 만들기
#정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
# X가 5로 나누어 떨어지면, 5로 나눈다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# X에서 1을 뺀다.
# 
# 정수 X가 주어졌을때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 예를 들어 정수가 26이면 다으모가 같이 계산해서 3번의 연산이 최솟값이다.
# 1. 26 -1 = 25
# 2. 25 / 5 = 5
# 3. 5 / 5 = 1
# 
# 입력 : 첫째 줄에 정수 X가 주어진다 (1<= X <= 30000)
# 출력 : 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
# 

x = int(input())

dp = [0] * 30001

for i in range(2, x+1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i //2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i //3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i],dp[i //5] + 1)

print(dp[x])