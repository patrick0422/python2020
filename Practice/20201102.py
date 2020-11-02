# <연습문제 1> 양의 정수를 입력받아 약수를 출력하시오.

# <출력 결과>
# Enter a positive integer: 60
# Factors of 60 are: 1 2 3 4 5 6 10 12 15 20 30 60

while True:
    num = (int)(input('Enter a positive integer: '))
    if num > 0: break

print('Factors of 60 are: ')

i = 1
while (i <= num):
    if num % i == 0:
        print(f'{i} ', end='')
    i += 1
