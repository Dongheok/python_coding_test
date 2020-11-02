# [기초-종합] 언제까지 더해야 할까?

a = int(input())
result = 0
for i in range(a):
    result += i
    if result >= a:
        print(i)
        break
