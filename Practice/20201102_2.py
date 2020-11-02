# <연습 문제2> 사용자로부터 자연수를 입력받아 자릿수를 출력하시오.

# <출력 결과>
# Enter an integer: 3452
# Number of digits: 4

# num = input('Enter an integer: ')
# print(f'Number of digits: {len(num)}')


num = (int)(input('Enter an integer: '))
digit = 0

while True:
    num /= 10
    num = (int)(num)
    digit += 1
    if (num <= 0): break

print(f'Number of digits: {digit}')