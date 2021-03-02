# open(): 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w
# read(): 파일 객체로부터 모든 내용을 읽는 함수입니다.
f = open("input.txt", "r", encoding="UTF-8")
f.seek(9)           #몇 바이트부터 글자를 읽을지 설정
data = f.read()
print(data)
f.close()


# readline(): 파일 객체로부터 한 줄씩 문자열을 읽는 함수입니다.
# readlines(): 전체 내용을 한 번에 리스트 담는 함수입니다.
f = open("input.txt", "r", encoding="UTF-8")
list = f.readlines()
print(list)

for i, data in enumerate(list):
    print("%d번째 줄: %s" %(i + 1, data), end = '')
f.close()
print()

f = open("input.txt", "r", encoding="UTF-8")
count = 0
while count < 3:
    data = f.readline()
    count = count + 1
    print("%d번째 줄: %s" %(count, data), end = '')
print()
f.close()


def process(filename):
    with open(filename, "r") as f:
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
        return dict

dict = process("input.txt")
print(dict)

# 빈도수를 기준으로 내림차순 정렬
dict = sorted(dict.items(), key = lambda a:a[1], reverse = True)
print(dict)


for data, count in dict:
    if data == '\n' or data ==' ':
        continue
    print("[%c]: %d번 출현" %(data, count))