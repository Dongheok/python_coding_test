# [기초-논리연산] 하나라도 참이면 참 출력하기(설명)


a, b = map(int, input().split(' '))

if a | b:
    print(1)
else:
    print(0)
