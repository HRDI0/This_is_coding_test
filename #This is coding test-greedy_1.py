#This is coding test.py
#큰수의 법칙
#다양한 N개의 숫자로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는 수가
#연속적으로 K번을 초과하여 더해지 수 없는 것이 이 법칙의 특징이다.
#예를 들어 2, 4, 5, 4, 6 으로 이루어진 배열이 있을 때, M = 8, K = 3 이라고 하자. 그렇다면
#6+6+6+5+6+6+6+5 = 46이 답이된다. 이때, 2번째 4와 4번째 4는 다른 값으로 구분된다.

#단순하게 푸는 방안
#가장 큰 수를 k번 더하고 두 번째 큰 수를 한번 더하는 것을 m번한다.

# n,m,k = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()
# first = num_list[-1]
# second = num_list[-2]
# sum = 0
# for i in range(1,m+1):
#     if i%k != 0:
#         sum += first
#     elif i%k == 0:
#         sum += second
# print(sum)

#시간초과를 관리한 방안
#문제에 예시의 경우 수가 더해지는 규칙은 6+6+6+5 가 두 번 행해지는 규칙을 가지고 있다.
#이때 위 반복되는 수열의 반복 횟수는 (더하는 횟수)/(같은 인덱스 더하기 횟수 제한 + 1) 즉, m / (k+1)이다.
#또한, 위 수열에서 가장 큰수가 더해지는 횟수는 (수열 반복 횟수)*(같은 인덱스 더하기 횟수 제한) 이므로 (m/(k+1)*k)가 된다.
#만약 m이 k+1로 나누어 떨어지지 않는 다면 나머지 값은 가장 큰수가 추가적으로 더해지는 횟수가 된다.
#결과적으로 공식은 ((m/(k+1))*k + (m%(k+1)) 이다.

n,m,k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
first = num_list[-1] * ((m//(k+1))*k+(m%(k+1)))
second = num_list[-2] * (m//(k+1))
sum = first + second
print(sum)


