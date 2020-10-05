#region while문

# prompt = '''1. Add    2. Del    3. List    4. Quit
# Enter number: '''

# number = 0
# while number != 4:
#     print(prompt, end='')
#     number = int(input())
#endregion

#region for문 => for 변수 in 리스트/튜플/문자열
# 2-1. 전형적인 for문
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# 2-2. for문과 range 함수 => 숫자 리스트를 자동 생성하는 함수
# 1~100까지의 합계

# sum = 0

# for i in range(1, 101) :
#     sum = sum + i
# print(f'1부터 100까지의 합계는 {sum} 입니다.')

# 2-3. 구구단

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')

# 연습문제. 사용자가 입력한 단만 출력
i = int(input('정수 입력 >> '))

for j in range(1, 10):
    print(f'{i} * {j} = {i*j}')

#endregion