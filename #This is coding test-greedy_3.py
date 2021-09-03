# 어떠한 수 N이 1이 될 때까지 음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 
# 단, 두번째 연산은 N이 K로 나누어떨어질 때만 선택 할 수있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# 이때 두 과정을 수행해야 하는 최소 횟수를 구하라.

# 단순 풀이
# n, k = map(int,input().split())
# count = 0
# while(1):
#     if n == 1:
#         break
#     if n % k == 0:
#         n /= k
#     else:
#         n -= 1
#     count +=1

# print(count)

#수학적 풀이
#n을 k로 나눈 값 * k 는 즉 k로 나눠지는 수이다. 그렇다면 n - ((n // k) * k)의 값만큼 빼야 k로 나누어 떨어지는 수가 되는 것이다.
#그러므로 n - ((n // k) * k) 는 즉 1씩 빼야 하는 횟수가 된다.
#1씩 빼야 하는 횟수를 count에 더하고, n을 k로 나눠 나머지를 버린후 count에 1을 더해 나눈 횟수를 추가한다.
# 위 과정을 반복하면서 n이 k보다 작아지면 더이상 k로 나누어 떨어지지 않기 때문에 남겨진 n은 전부 1씩 빼야한다.
# 반대로 남겨진 n에서 1을 빼면 1씩 빼야하는 횟수가 된다.
# 그러므로 count + (남겨진 n - 1)이 최소 수행 횟수가 된다.
n, k = map(int,input().split())
count = 0
while(1):
    div_num = (n//k) *k
    count += (n - div_num)
    n = div_num
    if n < k:
        break
    n //= k
    count +=1
count += (n - 1)   
print(count)