# 내장함수는 외부 모듈과 달리 import가 필요없다.

# type(Object) => 자료형 반환
print(type("abcd")) 
print(type([])) 

# id(Object) => 객체의 주소값 반환
a = 3
print(id(a))

# pow(x, y) => x의 y제곱 값 반환
print(pow(3, 4))

# sum(iterable) => 합계 반환
print(sum((1,2,3,4,5)), sum([1,2,3]))

# max(열거형 자료), min(열거형 자료) => 최대 / 최솟값 반환
print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))

# round(number) => 반올림수 반환
print(round(4.6))
print(round(4.2))

# eval(계산 가능한 문자열) => 문자열을 계산한 결과 반환
print(eval('1+2'))

#list(열거형 자료) => 리스트 반환
print(list('python'))
print(list((1,2,3)))

# enumerate() => 열거형 자료형을 입력받아 인덱스 값과 자료를 반환
for i, char in enumerate('python'):
    print(i, char)

#filter(함수, 열거형 자료) => 열거형 자료가 주어진 함수에서 실행되었을때 참인 값만 반환
def positive(n): # 일반 함수
    return n > 0

pos = lambda n: n>0 # lambda 함수

print(list(filter(lambda n: n > 0, [-1,2,0,3,-7,4,3])))

# map(함수, 열거형 자료) => 함수가 수행한 결과를 반환
def dub(n):
    return n*2
print(list(map(dub, [1,2,3,4,5])))

print(list(map(lambda n: n*2, [1,2,3,4,5])))


# range([시작점], stop, [간격]) => 입력받은 숫자에서 반복 가능한 객체 반환
print(list(range(5))) # 0 ~ 5
print(list(range(1, 5))) # 1 ~ 5
print(list(range(1, 10, 2))) # 1 ~ 10, 간격 : 2

# sorted(열거형 자료)
print(sorted([4, 1, 3 ,2]))
print(sorted('qwertyuiopasdfghjklzxcvbnm'))