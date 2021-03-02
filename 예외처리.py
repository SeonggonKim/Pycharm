try:
    print(3 / 0)
except Exception as a:
    print("Error!", a)
    print("0으로는 나눌 수 없습니다.")
else:
    print("예외 없이 성공적으로 실행되었습니다.")
finally:
    print("예외 처리를 마칩니다.")