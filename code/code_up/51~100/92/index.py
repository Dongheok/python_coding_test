# [기초-종합] 함께 문제 푸는 날(설명)

a, b, c = map(int, input().split(' '))

num = 0

while True:
    num += 1
    if num % a == 0 and num % b == 0 and num % c == 0:
        print(num)
        break
