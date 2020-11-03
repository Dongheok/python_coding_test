# [기초-종합] 3의 배수는 통과?(설명)

a = int(input())

for i in range(1, a+1):
    if i % 3 != 0:
        print(i)
