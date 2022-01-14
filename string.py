sentence = '작은 따옴표'
sentence2 = "큰 따옴표"
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence)
print(sentence2)
print(sentence3)

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 문자열의 0번째부터 2번째 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6번째 직전까지 
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지 
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째까지 (맨 뒷자리가 -1이 됨)

python = "Python is Amazing"
print(python.lower()) # 문자열 소문자로 변환
print(python.upper()) # 문자열 대문자로 변환
print(python[0].isupper()) # 대문자인지 확인
print(python[0].islower()) # 소문자인지 확인
print(len(python)) # 문자열 길이 
print(python.replace("Python", "Java")) # 문자열 대체

index = python.index("n") # 문자열에서 "n"의 위치 (찾는 문자가 없는 경우 오류 발생)
print(index)
index = python.index("n", index + 1) # index + 1의 위치부터 "n" 찾기
print(index)

print(python.find("Java")) # 원하는 값이 없을 때 -1 반환

print(python.count("n")) # 문자열에서 문자가 몇 번 포함되있는지