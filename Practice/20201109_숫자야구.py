import random
import os

attempt = 0
limit = 35

print('***********************************************')
print('숫자 야구 게임을 시작합니다.')
print('***********************************************')

x = random.randint(1, 9)
y = random.randint(1, 9)
z = random.randint(1, 9)

while True:
    

    attempt += 1
    print(f'{attempt}번째 시도 : 3자리 숫자를 입력하세요 >> ')
    num = int(input())
    ux = int(num / 100)
    uy = int(num % 100 / 10)
    uz = int(num % 100 % 10)

    strike = 0
    ball = 0
    if ux == x:
        strike += 1
    if uy == y:
        strike += 1
    if uz == z:
        strike += 1
    
    if ux == y or ux == z:
        ball += 1
    if uy == x or uy == z:
        ball += 1
    if uz == x or uz == y:
        ball += 1

    print(f'{ux}, {uy}, {uz}')

    if strike == 3:
        print(f'정답입니다! {attempt}번만에 성공하셨습니다.')
        exit()
    else:
        print(f'{strike}스트라이크', end=' ')
        print(f'{ball}볼 입니다. ')
        print()
        