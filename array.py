number = input("배열에 들어갈 숫자를 입력하세요 : ").split() 
arr = list(number) 
arr.sort() #오름차순 정렬
for i in arr: #i의 초깃값은 0, 배열 arr의 크기가 될 때까지 반복
    print(int(i), end=" ") #공백을 두고 출력