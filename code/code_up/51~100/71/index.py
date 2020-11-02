# [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1(설명)


a = list(map(int, input().split(' ')))

for i in a:
    if i != 0:
        print(i)
    else:
        break
