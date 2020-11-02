# [기초-종합] 3 6 9 게임의 왕이 되자!(설명)

a = int(input())
for i in range(1, a+1):
    if i % 3 == 0:
        print("X")
    else:
        print(i)
