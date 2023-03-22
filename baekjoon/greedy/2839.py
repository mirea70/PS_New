# 5로 나눌 수 있을 때까지 3 빼고, 봉지++
sugar = int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1
else:
    print(-1)