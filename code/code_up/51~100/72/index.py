# [기초-반복실행구조] 정수 입력받아 계속 출력하기(설명)


a = input()

b = list(map(int, input().split(' ')))

for i in b:
    print(i)
