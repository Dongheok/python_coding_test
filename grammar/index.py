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


# 반올림
# import math

math.ceil(-3.14)  # -3
math.ceil(3.14)  # 4

rount(3.14, 1)  # 3.1 !! 1.00같은게 오면 1.0이 됨
# 그럴땐 이렇게 반올림 해줘야함print("%0.2f" % a)

# len(문자열) === 글자수

# 반내림

math.floor(3.14)  # 3
math.floor(-3.14)  # 4
math.trunc(-3.14)  # -3

# int()
int(a)  # 숫자화
int(a, 2)  # 2진수 => 10진수화
int(a, 8)  # 8진수 => 10진수화
int(a, 16)  # 16진수 => 16진수화

# 아스키코드 => 10진수
ord(a)
# 10진수 => 아스키코드
chr(a)

# 대문자 변환
string.upper()  # 전체변환
string.capitalize()  # 첫 글자
string.title()  # 공백기준 첫 글자
