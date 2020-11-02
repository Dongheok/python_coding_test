# [기초-종합] 짝수 합 구하기(설명)

a = int(input())
result = 0
for i in range(a+1):
    if i % 2 == 0:
        result += i
print(result)
