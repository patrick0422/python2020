# 1. 파일 쓰기
# f = open('새파일.txt', 'w') # 현재 폴더에 새파일.txt 가 있으면 열고 없으면 만든 후 엶.

# f.write('Hello File\n')
# f.write('안녕하세요.\n')
# f.close()

# 2. 반복문으로 5줄 파일에 작성하기
# f = open('새파일.txt', 'w', encoding='utf-8')
# for i in range(1, 6):
#     f.write(f'{i}번째 줄입니다.\n')
# f.close()

# 3. 파일에 내용 추가하기
# f = open('새파일.txt', 'a', encoding='utf-8')
# for i in range(6, 11):
#     f.write(f'{i}번째 줄입니다.\n')
# f.close()

# 4. 파일 한 줄 읽기
# f = open('새파일.txt', 'r', encoding='utf-8')
# print(f.readline())
# f.close()

# 5. 파일 여러 줄 읽기
# f = open('새파일.txt', 'r', encoding='utf-8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, end='')
# f.close()