# <연습 문제3> Up&Down 게임 만들기

# <출력 결과>
# 숫자를 입력하세요: 30

# 정답입니다.
# 30보다 큽니다.
# 30보다 작습니다.

import random

target = random.randint(1, 100)

count = 0

while True:
    userInput = (int)(input('숫자를 입력하세요: '))
    if userInput == target:
        print(f'정답입니다, {count - 1}번 시도하셨습니다.')
        break
    elif userInput > target:
        print(f'{userInput}보다 작습니다.')
    else:
        print(f'{userInput}보다 큽니다.')
    count += 1