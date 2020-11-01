# [기초-입출력] 년월일 입력 받아 형식 바꿔 출력하기(설명)

a, b, c = map(str, input().split('.'))

if len(a) == 3:
    a = "0"+a
if len(a) == 2:
    a = "0"*2+a
if len(a) == 1:
    a = "0"*3+a
if len(b) == 1:
    a = "0"+b
if len(c) == 1:
    a = "0"+c

print("%s-%s-%s" % (c, b, a))
