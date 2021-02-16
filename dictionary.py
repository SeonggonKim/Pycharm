# 사전(Dictionary): 키와 값 한쌍을 원소로 가지는 자료형
dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'Effort'

for i, k in enumerate(dict):
    print("[인덱스:", i, "] 한글:", k, "/ 영어:", dict[k])

dict['안녕'] = 'Hi'
print(dict)

del dict['기적']
print(dict)

print("사전 자료형의 길이:", len(dict))

keys = dict.keys()
print("키:",keys)

key_list = list(keys)
print("키:",key_list)


def a(word):
    if word in dict:
        print(word, "은(는) 사전에 존재합니다.")
    else:
        print(word, "은(는) 사전에 존재하지 않습니다.")

a("안녕")
a("파이참")


scores = {}
scores['나동빈'] = 78
scores['이태일'] = 99
scores['박한울'] = 85
print(sorted(scores))
print(sorted(scores, reverse = True))