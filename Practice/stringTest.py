file = open('D:/Coding/python/Practice/user.txt', 'r', encoding='utf-8')
name = file.readline()[-4:]
print(name, end="")
dof = file.readline()[-7:]
print(dof, end="")
pwd = file.readline()[-4:]
print(pwd, end="")
file.close()