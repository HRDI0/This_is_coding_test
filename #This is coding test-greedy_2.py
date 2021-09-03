#숫자 카드 게임
# N x M 크기의 카드가 주어진다. 이때 카드중 가장 큰 수의 카드를 뽑아야 하는데, 카드 뽑기에 규칙이 있다.
#선택할수 있는건 몇 번째 행인지만 선택할 수 있으며 선택한 행의 카드 중 가장 작은 수의 카드를 뽑아가야한다.
# 예를 들어
# 3 1 2
# 4 1 4
# 2 2 2
#가 있을 때 가장 큰 수 4가 있는 2번째 행을 고르게 된다면 해당 행의 가장 작은 수인 1을 뽑게 되는 것이다. 그러므로 가장 큰 수를 뽑으려면
# 3번째 행을 선택해 2를 뽑아가야한다.
# 카드들이 N x M 형태로 놓여 있을 때 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오
# 입력에는 N과 M이 한줄에 입려되고 그다음에는 크기에 맞춰 숫자들이 입력된다.

n,m = map(int, input().split())
result = 0
card_list = []
for i in range(n):
    card_list.append(list(map(int,input().split())))
for i in range(n):
    if result <= min(card_list[i]):
        result = min(card_list[i])
print(result)