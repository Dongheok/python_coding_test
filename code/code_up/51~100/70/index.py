# [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)


a = int(input())

if a in (12, 1, 2):
    print('winter')
elif a in (3, 4, 5):
    print('spring')
elif a in (6, 7, 8):
    print('summer')
else:
    print('fall')
