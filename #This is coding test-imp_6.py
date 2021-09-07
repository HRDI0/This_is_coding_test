#문자열 재정렬
#알파벳 대문자와 숫자(0~9)가 섞여서 입력된다. 이때 모든 알파벳을 오름차순으로 출력한후 모든 숫자를 더한 값을 뒤에 출력한다.

word = input()
alpha = []
num = 0
for char in word:
    if char.isalpha():
        alpha.append(char)
    else:
        num +=int(char)
alpha = sorted(alpha)
# print(''.join(alpha),num,sep='')      #숫자가 없는 경우 이렇게 하면 뒤에 0이 출력된다.

if num != 0:        
    alpha.append(str(num))
print(''.join(alpha))
