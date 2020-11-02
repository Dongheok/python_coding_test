# [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기(설명)


a, b, c = map(int, input().split(' '))

result = (a if a < b else b)
print(result if result < c else c)
