# 입력을 복수로 받을 때
a, b, c = input.split('')

# 문자열 포맷팅
# 01 정수
%d
# 02 문자열
%s
# 03 소수
%f
# 04 8진수
%o
# 05 16진수
%x
# 06 '%'
%%

# 출력 시 변수를 포합하여 출력할 때
# 01
print("I'm %s" % name)
print('', num[i]+"0"*(4-i), '')
# for문 시 index값과 value값 받기

for i, x in temp_list:
    print(i, x)  # 0 value
