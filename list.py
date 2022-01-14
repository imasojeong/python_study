# subway = [10,20,30]
# print(subway)

subway = ["최우식", "김다미", "김성철"]
print(subway)

# 최우식이 몇 번째 칸에 타고 있는가?
print(str(subway.index("최우식")) + "번째 칸에 탑습 중입니다.")

# 김소정이 다음 정류장에서 다음 칸에 탐
subway.append("김소정") # 맨 뒤에 추가
print(subway)

# 최웅을 김다미 / 김성철 사이에 태워봄
subway.insert(2,"최웅")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print("내린 사람 : "+ subway.pop())
print(subway)

num_list = [5,2,4,3,1]
num_list.sort() # 오름차순 정렬
print(num_list)

num_list.reverse() # 순서 뒤집기
print(num_list)

num_list.extend(subway) # 리스트 확장
print(num_list)

num_list.clear()
print(num_list)

subway.sort()
print(subway)