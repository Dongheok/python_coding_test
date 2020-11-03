# [기초-1차원배열] 이상한 출석 번호 부르기1(설명)

n = int(input())
array = list(map(int, input().split()))
all = [0]*23
for i in array:
    all[i-1] += 1
for j in all:
    print(j, end=" ")
