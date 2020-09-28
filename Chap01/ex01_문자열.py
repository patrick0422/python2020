#region 문자열

# food = 'Python\'s favorite food is perl'
# say = "\"Python is very easy.\" he says."

# # 여려줄의 문자열을 변수에 대입하고 싶을 때
# multiline = "Life is too short\nYou need Python"
# print(multiline)


# # 아래와 같이 하면 줄바꿈 문자 등 까지 포함 가능
# multiline = """
# Life is too short
# You need python
# """
# print(multiline)

# # 1. 문자열 연산하기
# head = 'Python'
# tail = ' is fun!'
# print(head + tail) # Python is fun!

# # 2. 문자열 곱하기
# print((head + '\n') * 5)

# # 3. 문자열 길이 구하기
# print(len(head))

#endregion

#region 문자열 인덱싱과 슬라이싱

# 1. 문자열 인덱싱
# str = 'Life is too short, You need Python'
# print(str[3]) 
# print(str[-1])
# print(str[-2])

# # 2. 문자열 슬라이싱
# print(str[0:6]) # 0~6 까지
# print(str[:6]) # 처음부터 6까지
# print(str[5:]) # 5번부터 끝까지
# print(str[19:-7])
# endregion

#region 문자열 포매팅(Formatting)
# print("I eat %d apples." % 3)
# print("I ate %d apples. so I was sick for %s days." % (3, 'three'))

# # format 함수를 이용한 포매팅
# print("I ate {0} apples." .format(3))
# print("I ate {0} apples. so I was sick for {1} days." .format(3, 'three'))

# # f 문자열 포매팅 (3.6 이상 버전부터 사용 가능)
# name = '홍길동'
# age = 30
# print(f'나의 이름은 {name} 입니다. 나이는 {age}살 입니다.')
# endregion

#region 문자열 관련 함수들
# # 문자 개수 세기(count)
# str = 'hobby'
# print(str.count('b')) # 들어있는 개수 반환

# # 위치 알려주기(find)
# str = 'Phython is the best choice'
# print(str.find('b')) # 인덱스 번호 반환
# print(str.find('h')) # 여러개면 첫번째
# print(str.find('k')) # 없으면 -1 반환

# # 대소문자 바꾸기
# print(str.upper()) # PHYTHON IS THE BEST CHOICE
# print(str.lower()) # phython is the best choice

# # 공백 지우기
# str = ' hi '
# print(str)
# print(str.lstrip()) # 왼쪽 공백 제거
# print(str.rstrip()) # 오른쪽 공백 제거
# print(str.strip()) # 양쪽 공백 제거

# # 문자열 바꾸기
# str = 'Life is too short'
# print(str.replace('short', 'long')) # str 안에서 왼쪽의 문자열을 찾아 오른쪽으로 치환

# # 문자열 나누기 => list 로 반환
# print(str.split())

# str2 = 'a:b:c:d'
# print(str2.split(':'))

#endregion