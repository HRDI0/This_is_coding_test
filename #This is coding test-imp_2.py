#시각
#n을 입력 받고 00시 00분 00초 부터 n시 59분 59초 까지 3이 하나라도 포함되어 있는 경우의 수를 구하는 프로그램을 작성하시오
# 예) 2시 25분 30초 -> 3 포함
# 예) 10시 55분 49초 -> 3 포함 안됨.
n = int(input())
result = 0
for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i) + str(j) + str(k):
                result +=1
print(result)