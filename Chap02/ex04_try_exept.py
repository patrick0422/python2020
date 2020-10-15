# 1. 에러 발생시 프로그램은 중지됨.
# n = 4 / 0

#region try, exept문 기본 구조
# try:
#     오류가 날 것 같은 실행 문장
# except 발생 에러 as 변수:
#     pass

# 2. try - except를 통해 에러가 발생해도 프로그램이 중지되지 않도록 함.
# try:
#     n = 4 / 0
# except:
#     pass

# 3. ZeroDivisionError 예외 처리
# try:
#     n = 4 / 0
# except ZeroDivisionError as err:
#     print(f'0으로 나눌 수 없습니다. : {err}')

# 4. IndexError 예외 처리
# try:
#     a = []
#     a[0] = 100
# except IndexError as err:
#     print(f'인덱싱 에러 발생 : {err}')

# 5. Exception 예외 처리
# try:
#     n = 4 / 0
#     a = []
#     a[0] = 100
# except Exception as err:
#     print(f'에러가 발생했습니다 : {err}') # 먼저 발생하는 에러 처리

# 6. try - except ~ finally
# 에러 발생 여부에 상관 없이 실행해야 하는 코드를 finally 안에 집어넣는다.
# try:
#     f = open('새파일.txt', mode='r', encoding='utf-8')
# except Exception as err:
#     print(f'에러 발생 : {err}')
# finally:
#     print('무조건 실행할 구문')

# 7. 여러개의 오류 처리
# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except ZeroDivisionError as err:
#     print(f'err : {err}')
# except IndexError as err:
#     print(f'err : {err}')
# except Exception as err:
#     print(f'err : {err}')


# print('마지막 코드')