#위에서 아래로
#기본 정렬 라이브러리 활용 예제

from sys import stdin
n = int(input())
num_list = [int(stdin.readline()) for _ in range(n)]
num_list = sorted(num_list, reverse= True)
print(num_list)


#성적이 낮은 학생 순으로 출력하기
#입력 : 홍길동 70
#       김민수 100  ...

#출력 : 홍길동 김민수 ...
n = int(input())
arr = []
for _ in range(n):
    input_data = input().split()
    arr.append((input_data[0],int(input_data[1])))
sorted(arr, key= lambda x:x[1])
for _ in arr:
    print(_[0], end= ' ')


#두 배열의 값을 m번 교환해서 a 배열의 합을 최대로 만들기
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
for _ in range(m):
    if a[_] < b[-1-_]:
        a[_], b[-1-_] = b[-1-_], a[_]

print(sum(a))