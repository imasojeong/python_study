from random import *

# ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ID = list(range(1,21))
shuffle(ID)
print(ID)

print("-- 당첨자 발표 --")
winners = sample(ID,4)
chicken = winners[0]
print("치킨 당첨자 : " + str(chicken))
coffee = list(winners[1:])
print("커피 당첨자 : " + str(coffee))
print("-- 축하합니다 --")