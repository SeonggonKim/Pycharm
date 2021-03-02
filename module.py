# 모듈(Module): 미리 작성된 함수 코드를 모아 놓은 파이썬 파일
import math
print(math.pow(3, 8))
print(math.sqrt(64))
print(math.gcd(72, 24))

import lib
print(lib.subtract(3, 4))

from lib import add
print(add(3, 7))