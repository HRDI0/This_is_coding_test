#이진 탐색 알고리즘
# 이론
# 어떠한 값의 범위( ex)1~ 100)이나 '정렬된'리스트의 중간(값)을 기준으로 데이터를 둘로 나누어 탐색한다.
# 예를 들어 정수 4를 찾아야 한다면 1~100의 중간인 50을 4와 비교한다.
# 50은 4보다 크기 떄문에 최대값일 50이상의 값과 중간값인 50을 제외하고 1~49부터 탐색을 시작한다.
# 데이터가 반씩 줄어든다는 점에서 퀵정렬과 비슷하다.

#재귀적 구현
def binary_search(input_list, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    if input_list[mid] == target:
        return mid
    elif input_list[mid] > target:
        return binary_search(input_list, target, start, mid -1)
    elif input_list[mid] < target:
        return binary_search(input_list, target, mid +1, end)

target = int(input())
input_list = [1,3,5,7,9,11,13]
result = binary_search(input_list, target, 0, len(input_list)-1)

if result == None:
    print("찾는 원소가 리스트에 없습니다.")
else:
    print(result+1,sep="\n")


#반복적 구현은... 대충알지? 재귀 부분이 반복문으로 구성되면 됨. 
# while start <= end: 로 시작해서 나머지 로직은 같음.