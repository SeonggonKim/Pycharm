# input(): 사용자로부터 콘솔로 입력을 받는 함수
# int(): 정수 자료형으로 변환
# float(): 문자열, 정수 등의 자료형을 실수형으로 변환
# max(), min(): 시퀀스 자료형에 포함되어 있는 원소 중 최대 혹은 최소값
# bin(), hex(): 10진수 -> 2진수, 10진수 -> 16진수 변환
# round(): 반올림을 수행
# type(): 자료형의 종류

list = [ 1,2,3,4,4,5,5,10]
print(max(list))

print(bin(128))

print(round(123.456, 2))

Int = 1
Str = "문자열"
List = [1,2,3]
Tuple = (1,2,3)
Dict = {}
Dict["사과"] = "apple"

print(type(Int))
print(type(Str))
print(type(List))
print(type(Tuple))
print(type(Dict))
print(Dict)

user_input = input('정수를 입력하세요: ')
print("제곱:", int(user_input)**2)