# [기초-종합] 그림 파일 저장용량 계산하기(설명)

w, h, b = map(int, input().split(' '))

result = (w*h*b)/(8*1024*1024)

print("%0.2f MB" % result)
