cabinet = {1:"짱구", 2:"철수", 3:"영희", 4:"훈이", 5:"맹구"}

# print(cabinet[2])

# print(cabinet.get(3))
# print(cabinet.get(6, "사용 가능"))

# print(1 in cabinet)
# print(6 in cabinet)

# 새 손님
print(cabinet)
cabinet[1] = "닉"
cabinet[6] = "주디"
print(cabinet)

# 나간 손님
del cabinet[5]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # 모든 값 지우기
print(cabinet)