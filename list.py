# index(): 리스트 내 특정한 원소의 인덱스를 찾기
list = ['김성곤', '서민석', '이가람', '김슬아']
print(list.index('서민석'))


# reverse(): 리스트의 원소를 뒤집기
list = [1,2,3]
list.reverse()
print(list)
print(list[::-1])


# sum(): 리스트의 모든 원소의 합
list = [1,2,3]
print(sum(list))
del(list)


# range(): 특정 범위를 지정
# list(): 특정 범위의 원소를 가지는 리스트를 반환
my_range = range(5, 10)
list = list(my_range)
print(list)


# all(): 리스트의 모든 원소가 참인지 판별
# any(): 리스트의 원소 중 하나라도 참인지 판별
list = [True, False, True]
print(all(list))
del(list)


# enumarate(): 리스트에서 인덱스와 원소를 함께 추출
my_list = ['나동빈', '강종구', '이태일', '박한울', '이상욱']
result = list(enumerate(my_list))
print(result)

for i, k in enumerate(my_list):
    print("인덱스:", i, "/ 값:", k)


# sort(): 리스트의 원소를 정렬
my_list = ['나동빈', '강종구', '이태일', '박한울', '이상욱']
my_list.sort()
print(my_list)


# count(): 특정한 원소의 개수를 추출
my_list = ['나동빈', '강종구', '이태일', '이태일', '이상욱']
print(my_list.count('이태일'))


# del(): 리스트의 특정 원소를 제거
my_list = ['123', '456', '789']
del(my_list[0:2])
print(my_list)


# insert(): 리스트에 특정 원소를 삽입
my_list = ['123', '456', '789']
my_list.insert(3, -1)
print(my_list)


# append(): 리스트의 가장 마지막 원소로서 원소를 삽입
my_list = ['123', '456', '789']
my_list.append('100')
print(my_list)