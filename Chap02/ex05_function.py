#region 1. 사용자 정의 함수 2
# c = 10
# def add(a, b):
#     global c
#     c = a + b
#     return c

# print('합계 : ', add(3, 4))
# print('c = ', c)

# def subtract(a, b):
#     return a - b;

# print(subtract(5, 10))
# print(subtract(b = 5, a = 10))

#endregion

#region 2. 사용자 정의 함수 2
# 사용자에게 원의 반지름(정수)와 원주율(실수)를 입력받아 형변환값을 알려주는 함수
# def get_input_value(msg, casting):
#     '''
#     사용자에게 msg 문자열을 출력하고, 입력받은 값을 casting 형태로 변환하여 반환하는 함수.

#     Args:
#         msg(str): input()으로 출력할 문자열
#         casting(class): 사용자에게 입력받은 자료형

#     Return:
#         value(casting된 value): 사용자가 입력한 값을 캐스팅하여 반환
#     '''

#     while True:
#         try:
#             value = casting(input(msg)) 
#             return value
#         except:
#             continue

# radius = get_input_value('정수 반지름을 입력하세요 >> ', int)
# PI = get_input_value('원주율을 입력하세요 >> ', float)

# print(type(radius))
# print(type(PI))

#endregion

#region 3. 매개변수가 몇 개가 될지 모를 때 (가변 매개변수)
# 3-1. 인자를 모두 더하는 함수
# def add_many(*args):
#     sum = 0
#     print('args : ', args)
#     for i in args:
#         sum += i
#     return sum

# print('sum : ', add_many(1, 2))
# print('sum : ', add_many(1, 2, 3, 4, 5))

# 3-2. 연산자를 더하기와 곱하기로 구분하여 인자를 모두 계산하는 함수
# def add_mul(op, *args):
#     if op == 'add':
#         result = 0
#         for i in args:
#             result += i
#         return result

#     elif op == 'mul':
#         result = 1
#         for i in args:
#             result *= i
#         return result

# print(add_mul('add', 1,2,3,4,5))
# print(add_mul('mul', 1,2,3,4,5))

#endregion

#region 4. 키워드 파라미터 kwargs
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a = 1)
# print_kwargs(name = '홍길동', age = 3)

#endregion

#region 5. Python 함수는 1급 객체
# 5-1. 함수를 변수에 저장 가능
# def hello():
#     print('hello')
# hi = hello
# hello()
# hi() # hi = hello
# print(type(hi)) # = function

# 5-2. 사칙연산 함수
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b

# def calc(func, a, b):
#     print(f'{func.__name__} 계산 결과 : {func(a, b)}')

# calc(add, 5, 3)
# calc(sub, 3, 4)

#endregion

#region 6. 함수의 결과값은 언제나 하나
# def add_mul(a, b):
#     return a + b, a * b

# print(add_mul(5, 10))
# sum, mul = add_mul(5, 10)
# print(f'sum = {sum}, mul = {mul}')

#endregion

#region 7. 람다(lambda)식
add = lambda a, b: a + b
sub = lambda a, b: a - b
def calc(op, func, a, b):
    print(f'{a}와 {b}의 {op} 결과 : {func(a,b)}')

calc('덧셈', add, 5, 10)
calc('뺄셈', sub, 5, 10)
calc('곱셈', lambda a, b: a * b, 5, 10)
calc('나눗셈', lambda a, b: a / b, 5, 10)

#endregion
