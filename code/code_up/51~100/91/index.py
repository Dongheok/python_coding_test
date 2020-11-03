
# [기초-종합] 수 나열하기3

a, m, d, n = map(int, input().split(' '))
result = 1
while result != n:
    a = a*m+d
    result += 1

print(a)
