# 만들 수 없는 금액

# 동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있습니다. 
# 이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.
# 예를 들어, N = 5 이고, 각 동전이 각각 3, 5, 7원 짜리 동전이라고 가정합시다.
# 이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟 값은 1원입니다.

# 입력
# 5
# 3 2 1 1 9

# 출력
# 8

n = int(input())
coin_list = list(map(int, input().split()))

coin_list.sort(reverse= True)

# for target in range(1,1000001):
#     result = target
#     for coin in coin_list:
#         if target - coin >= 0:
#             target -=coin
#     if target != 0:
#         print(result)
#         break
target = 1
for x in coin_list:
    if target < x:
        break
    target += x
print(target)