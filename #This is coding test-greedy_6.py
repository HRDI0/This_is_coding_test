# # 곱하기 혹은 더하기
# 각 자리가 숫자(0~9)로만 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에'x' 혹은 '+'
# 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요. 
# 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 부터 순서대로 이루어 진다고 가정합니다.

# ex) 02984 -> ((((0 + 2) x 9) x 8) x 4) = 576

# 입력: 1<= s <= 20 길이의 문자열
# 출력: 최대 수.

n = input()
result_z = 0
result_o = 0
if n[0] == '0':
    result_z = 1
else:
    result_o = 1
# flag = 0
# for char in n:
#     if char =='1':
#         flag = 1
#     if char == '0' and flag == 1:
#         flag = 0
#         result_z +=1

# for char in n:
#     if char =='0':
#         flag = 0
#     if char == '1' and flag == 0:
#         flag = 1
#         result_o +=1

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i] == '0':
            result_z +=1
        else:
            result_o +=1

print(min(result_o,result_z))

    

    