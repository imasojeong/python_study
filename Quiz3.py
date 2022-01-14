site = "http://naver.com"
print(f"사이트 : {site}")

print("규칙 1 : http:// 부분 제외")
site = site.replace("http://", "")
print("규칙 1 적용 결과 => " + site)

index = site.index(".") # 점(.)의 위치 
print("규칙 2 : 처음 만나는 점(.) 이후 부분 제외")
site = site.replace(site[index:],"")
print("규칙 2 적용 결과 => " + site)

print("규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + \"!\"로 구성")
site = site[:3] + str(len(site)) + str(site.count('e')) + "!"
print("생성된 비밀번호 : " + site)