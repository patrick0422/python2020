#region 매개 변수 없는 생성자

# class Calculator1:
#     # 생성자: 클래스 객체를 생성하는 함수
#     def __init__(self): # __init(self) = 생성자
#         self.result = 0
    
#     # 일반 함수
#     def add(self, num):
#         self.result += num
#         return self.result

# # 객체 생성
# calc1 = Calculator1()
# calc2 = Calculator1()

# print(calc1.add(1))
# print(calc1.add(2))
# print(calc1.add(3))
# print(calc1.add(4))

#endregion

#region 매개 변수 있는 생성자

# 덧셈 혹은 곱셈을 수행하는 객체
# class Calculator2:
#     def __init__(self, operator):
#         self.operator = operator

#     def Calc(self, *args): # *args = 여러개의 인자를 튜플로 받는 문자열
#         self.result = 0

#         if self.operator == 'add':
#             for i in args:
#                 self.result += i

#         elif self.operator == 'mul':
#             self.result = 1
#             for i in args:
#                 self.result *= i

#         return self.result

# calc3 = Calculator2('mul')
# calc4 = Calculator2('add')

# print(calc3.Calc(1, 2, 3, 4, 5))

# print(calc4.Calc(3, 6, 8, 9))

#endregion

#region 사칙연산 클래스

#생성자에 숫자 두 개를 받아서, 사칙연산 메소드를 수행하는 클래스 | add, sub, mul, div
# class Calculator3:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def add(self):
#         return self.x + self.y
#     def sub(self):
#         return self.x - self.y
#     def mul(self):
#         return self.x * self.y
#     def div(self):
#         return self.x / self.y

# calc5 = Calculator3(3, 5)

# print(calc5.add())
# print(calc5.sub())
# print(calc5.mul())
# print(calc5.div())

#endregion

#region 상속

# class ExtCalc(Calculator3):
#     def pow(self):
#         return self.x ** self.y

# eCalc = ExtCalc(2, 3)

# print(eCalc.pow())

#endregion

#region 메소드 오버라이딩

# class SafeCalc(Calculator3):
#     def div(self):
#         if self.y != 0:
#             return self.x / self.y
#         else:
#             return '0으로 나눌 수 없습니다.'

# calc = SafeCalc(5, 0)
# print(calc.div())

#endregion

#region 클래스 변수

class Family:
    lastname = '양'

    def __init__(self, firstname):
        self.firstname = firstname

taewoong = Family('태웅')
print(f'{taewoong.lastname}{taewoong.firstname}')

manchoon = Family('만춘')
print(f'{manchoon.lastname}{manchoon.firstname}')

#endregion
