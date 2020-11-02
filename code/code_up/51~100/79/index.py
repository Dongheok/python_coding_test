# [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기

a = list(input().split(' '))

for i in a:
    print(i)
    if i == "q":
        break
