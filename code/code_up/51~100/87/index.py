# [기초-종합] 여기까지! 이제 그만~(설명)

a = int(input())
count = 0
for i in range(a+1):
    count += i
    if count >= a:
        print(count)
        break
