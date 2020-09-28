# 딕셔너리 추가하기
a = {1 : 'a'}
a[2] = 'b'
print(a)

a['name'] = 'Taewoong'
print(a)

a[3] = [1,2,3]
print(a)

# key값으로 value값 가져오기
print(a[1], a['name'], a[3])

#region 딕셔너리 관련 함수
print(a.keys()) # 자바의 해쉬맵의 keyset같은 느낌 list형으로 반환

for k in a.keys(): # 키값들을 모두 나열
    print(k, end=' ')
print()
print(list(a.keys())) # 키값들을 리스트로 변환

print(a.values()) # value 값들만 가져오기

# key, value 값 쌍으로 가져오기
print(a.items())

# 모두 지우기
a.clear()
print(a)

# key 값으로 value 값 얻기
print(a.get('name')) # 위에서 clear() 해서 None 리턴



#endregion
