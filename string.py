# 문자열 자료형 뒤집기: 슬라이싱 활용
# len(): 문자열의 길이를 출력
str = 'Hello World'
print(str[::-1])


# isalpha(): 특정한 문자열이 문자로만 이루어져 있는지 확인
# isdigit(): 특정한 문자열이 숫자로만 이루어져 있는지 확인
# isalnum(): 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
str1 = '김성곤'
print(str1.isalpha())


# join(): 여러 개의 문자열을 구분자와 함께 합치는 함수
list = ['Hello', 'Wolrd', '홍길동']
print('_'.join(list))


# sorted(): 각 문자를 정렬하는 함수
str = 'Hello World'
list = sorted(str)
print(list)


# split(): 문자열을 토큰에 따라서 분리하는 함수
str = "I wanna watch a movie."
list = str.split(' ')
print(list)


# find(): 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
print(str.find('like'))
print(str.find('a'))


# upper(): 문자열을 대문자로 변환해주는 함수
# lower(): 문자열을 소문자로 변환해주는 함수
a = 'hello world'
print(a.upper())


# strip(): 좌우로 특정한 문자열을 제거하는 함수 (lstrip = 왼쪽 공백, rstrip = 오른쪽 공백)
str = " Hello World "
print(str.strip(' '))


# eval(): 문자열 수식 계산해주는 함수
exp = "(203 + 705) *3 - (30/6)"
print(eval(exp))