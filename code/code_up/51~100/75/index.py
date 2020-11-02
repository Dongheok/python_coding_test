# [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(설명)


a = int(input())

for i in range(a):  # 0 1 2 3 4
    print(a-1)
    if a-1 == 0:
        break
    a -= 1
