# [기초-종합] 빛 섞어 색 만들기(설명)

a, b, c = map(int, input().split(' '))
count = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            count += 1
            print(i, j, k)
print(count)
