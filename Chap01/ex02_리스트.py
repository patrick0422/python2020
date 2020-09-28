#region 리스트의 인덱싱과 슬라이싱

# # 인덱싱 
# a = [1, 2, 3] 
# print(a[0], a[-1])

# a = [1, 2, 3, ['a', 'b', 'c']] # 리스트 안의 리스트
# print(a[-1][0]) # 리스트 안의 리스트 접근법

# # 슬라이싱
# a = [1,2,3,4,5]
# print(a[0:2]) # [1, 2]

#endregion

#region 리스트 수정과 삭제

# # 수정하기
# a = [1,2,3]
# a[2] = 4
# print(a) # [1,2,4]

# # 삭제하기
# del a[1]
# print(a) # [1,4]

#endregion

#region 리스트 관련 함수
# # 요소 추가하기
# a = [1,2,3]
# a.append(4) # 끝에 4를 붙이기
# print(a) # [1,2,3,4]

# a.insert(0, 5) # 인덱스 0 에 5를 넣어라
# print(a)

#endregion
