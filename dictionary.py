supermarket = {"아이스크림": 1000, "과자": 1200, "음료수": 1000}
print("슈퍼마켓의 상품 항목은 다음과 같습니다.\n", supermarket)

print("상품 추가 : 1, 상품 가격 수정 : 2, 상품 삭제 : 3")

case = input("숫자를 입력하세요 : ")

if(case=="1"):
    productName = input("상품 이름을 입력하세요 : ")
    productCost = input("상품 가격을 입력하세요 : ")
    supermarket[productName] = productCost
    print(supermarket)
elif(case=="2"):
    productName = input("수정할 상품 이름을 입력하세요 : ")
    newProductCost = input("새로운 상품 가격을 입력하세요 : ")
    supermarket[productName] = newProductCost
    print(supermarket)
elif(case=="3"):
    productName = input("삭제할 상품 이름을 입력하세요 : ")
    del supermarket[productName]
    print(supermarket)
