# [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)


a = input()
num = ord(a)-96  # 102-96=6
# 0 1 2 3 4 5
for i in range(num):
    print(chr(97+i))
