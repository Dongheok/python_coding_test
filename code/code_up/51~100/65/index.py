# [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)


a = list(map(int, input().split(' ')))

for i in a:
    if i % 2 == 0:
        print(i)
    else:
        pass
