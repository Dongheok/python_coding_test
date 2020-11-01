# [기초-입출력] 정수 1개 입력받아 나누어 출력하기(설명)

temp = list(input())
temp_len = len(temp)

for i in range(5):
    result = int(temp[i])*10**(temp_len-i-1)
    print("[%s]" % result)

# temp = input()
# temp_list = list(temp)
# temp_len = len(temp)

# for i, x in enumerate(temp_list):
#     num = int(x)
#     gob = int(temp_len) - int(i)-1
#     print('[', num*10**gob, ']')
