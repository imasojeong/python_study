user = "kimsojeong"

print("이 계산기는 " + user + "의 사칙연산 계산기입니다.")

cnt = int(input("반복할 횟수를 입력하세요 : "))

for i in range(0,cnt):
    print(str(i+1) + "번째 실행입니다.")
    number1, number2 = map(int,input("계산하고 싶은 정수 두 값을 입력하세요 : ").split()) #split()는 공백으로 문자열 구분
    op = input("연산자를 선택하세요 : ")
    if(op=="+"):
        print(number1+number2)
    elif(op=="-"):
        print(number1-number2)
    elif(op=="*"):
        print(number1*number2)
    elif(op=="/"):
        print(number1/number2)
    else:
        print("잘못된 연산자입니다.")
if(cnt==i+1):
    print("계산이 종료되었습니다.")