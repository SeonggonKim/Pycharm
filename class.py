# 클래스(Class): 반복되는 불필요한 소스코드를 최소화하면서 현실 세계의 사물을
#               컴퓨터 프로그래밍 상에서 쉽게 표현할 수 있도록 해주는 기술

# 인스턴스: 클래스로 정의된 객체를 프로그램에서 이용할 수 있게 만든 변수

# 클래스의 멤버: 클래스 내부에 포함되는 변수
# 클래스의 함수: 클래스 내부에 포함되는 함수, 메소드

class Car:
    # 클래스의 생성자
    def __init__(self, name, color):
        self.name = name     # 클래스의 멤버
        self.color = color   # 클래스의 멤버
    # 클래스의 메소드
    def show_info(self):
        print("이름:", self.name, "/ 색상:", self.color)
    # Setter 메소드
    def set_name(self, name):
        self.name = name

car1 = Car("소나타", "빨간색")
car1.show_info()
car2 = Car("아반떼", "검은색")
car2.show_info()
car2.set_name("BMW")

print(car1.name, "을(를) 구입했습니다.")
print(car2.name, "을(를) 구입했습니다.")


# 상속: 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다. [전투력:", self.power,"]")

marine = Unit("마린", 30)
marine.attack()

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

monster = Monster("저글링", 15, "초급")
monster.attack()