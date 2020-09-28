# 변수가 저장한 메모리 주소값 확인하기
a = [1,2,3]
print(id(a))

#region 얕은복사 & 깊은복사

# 얕은 복사
b = a
print(id(b)) # 주소는 a와 같음

b.append(4) # a와 b가 가리키는 주소가 같음 a를 호출해도 b와 결과는 같다
print(a, b)
print(f'a is b : {a is b}') # True 리턴


# 깊은 복사
a = [1,2,3]
b = a[:] # a를 통채로 복사

print(a, b)
b[0] = 10
print(a, b) # a= [1,2,3] b= [10,2,3]
print(f'a is b : {a is b}') # False 리턴

#endregion

#region 변수를 만드는 여러가지 방법
a, b = ('python', 'life') # 튜플로 여러개의 변수에 값 대입 가능 a에는 python, b에는 life 대입
print(a, b)

a, b = 'node', 'js' # 튜플은 괄호 생략 가능
print(a, b)

[a, b] = ['python', 'life'] # 리스트로도 받을 수 있다
print(a, b)

a = b = 'node.js' # 이렇게도 가능

print(a, b)

#endregion
